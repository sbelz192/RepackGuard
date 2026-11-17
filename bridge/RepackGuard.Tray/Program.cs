using System.Diagnostics;
using System.Diagnostics.Eventing.Reader;
using System.Text.RegularExpressions;
using System.Windows.Forms;
using RepackGuard.Tray;

namespace RepackGuard.Tray;

public sealed class TrayApp : ApplicationContext
{
    private readonly NotifyIcon _tray;
    private readonly List<RgEvent> _events = new();
    private readonly object _lock = new();
    private EventLogWatcher? _watcher;
    private readonly string _query =
        "*[System[(EventID=1116 or EventID=1117 or EventID=1009 or EventID=5007)]]";

    public TrayApp()
    {
        _tray = new NotifyIcon
        {
            Icon = new System.Drawing.Icon("icon.ico"),
            Text = "RepackGuard " + Native.Version(),
            Visible = true,
            ContextMenuStrip = BuildMenu()
        };
        _tray.DoubleClick += (_, _) => ShowStatus();

        try { StartWatcher(); }
        catch (Exception ex) { Warn("Eventlog nicht lesbar", ex.Message + "\n(RepackGuard braucht ggf. Adminrechte.)"); }
    }

    private ContextMenuStrip BuildMenu()
    {
        var m = new ContextMenuStrip();
        m.Items.Add("Status", null, (_, _) => ShowStatus());
        m.Items.Add("Sofortmassnahmen", null, (_, _) => ShowIncident());
        m.Items.Add(new ToolStripSeparator());
        m.Items.Add("Beenden", null, (_, _) => Application.Exit());
        return m;
    }

    private void StartWatcher()
    {
        var q = new EventLogQuery("Microsoft-Windows-Windows Defender/Operational", PathType.LogName, _query);
        _watcher = new EventLogWatcher(q);
        _watcher.EventRecordWritten += OnDefenderEvent;
        _watcher.Enabled = true;
        _tray.ShowBalloonTip(2500, "RepackGuard aktiv",
            "Ueberwacht den Defender auf Repack-Manipulationen.", ToolTipIcon.Info);
    }

    private void OnDefenderEvent(object? sender, EventRecordWrittenEventArgs e)
    {
        try
        {
            using var r = e.EventRecord;
            if (r == null) return;
            var ev = Parse(r);
            lock (_lock)
            {
                _events.Add(ev);
                if (_events.Count > 400) _events.RemoveRange(0, _events.Count - 400);
            }
            Evaluate();
        }
        catch { /* Einzelereignisse duerfen den Dienst nicht beenden */ }
    }

    private static RgEvent Parse(EventRecord r)
    {
        string msg = "";
        try { msg = r.FormatDescription() ?? ""; } catch { }

        // Best-effort-Parsing der Defender-Nachricht
        string threat = Regex.Match(msg, @"name=([^&]+)").Groups[1].Value.Trim();
        if (threat.Length == 0)
            threat = Regex.Match(msg, @"Name:\s*([^\r\n]+)").Groups[1].Value.Trim();

        string path = Regex.Match(msg, @"file:_([^\s%]+)").Groups[1].Value.Trim();
        if (path.Length == 0)
            path = threat.Length > 0 ? threat : msg.Replace("\n", " ").Replace("\r", " ");

        int did = r.Id is 1116 or 1117 ? 1 : 0;
        if (Regex.IsMatch(msg, @"DidThreatExecute[^0-9]*[1-9]", RegexOptions.IgnoreCase)) did = 1;

        return new RgEvent
        {
            ts = new DateTimeOffset(r.TimeCreated.GetValueOrDefault().ToUniversalTime()).ToUnixTimeSeconds(),
            event_id = r.Id,
            user = r.UserId?.Value ?? "",
            path = Trunc(path, 511),
            threat = Trunc(threat, 127),
            did_execute = did
        };
    }

    private static string Trunc(string s, int n) => s.Length > n ? s[..n] : s;

    private void Evaluate()
    {
        RgEvent[] snapshot;
        lock (_lock) { snapshot = _events.ToArray(); }

        try
        {
            int alarm = Native.rg_analyze_win(snapshot, snapshot.Length, 86400, out var rep);
            if (alarm == 1) ShowIncident(rep);
        }
        catch (Exception ex)
        {
            _tray.ShowBalloonTip(3000, "RepackGuard Fehler", ex.Message, ToolTipIcon.Error);
        }
    }

    private void ShowStatus()
    {
        lock (_lock)
        {
            MessageBox.Show(
                $"RepackGuard {Native.Version()}\n" +
                $"Gespeicherte Defender-Ereignisse: {_events.Count}\n" +
                $"Watcher: {(_watcher?.Enabled == true ? "aktiv" : "inaktiv (Admin fehlt?)")}\n\n" +
                "Kern: " + Native.Version(),
                "RepackGuard — Status", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }

    private void ShowIncident() => ShowIncident(default);

    private void ShowIncident(RgReport rep)
    {
        var text = !string.IsNullOrEmpty(rep.threat)
            ? $"Erkannt: {rep.threat}\n\n{rep.detail}"
            : "Verdaechtige Defender-Manipulation erkannt.";
        var res = MessageBox.Show(
            text + "\n\nSOFORTMASSNAHMEN:\n" +
            "1. Discord: Einstellungen -> Alle Geraete abmelden\n" +
            "2. Passwoerter aendern (vom sauberen Geraet)\n" +
            "3. Vollstaendigen Virenscan starten\n\n" +
            "Details im Eventlog: Microsoft-Windows-Windows Defender/Operational",
            "RepackGuard — ALARM", MessageBoxButtons.OK, MessageBoxIcon.Warning);
    }

    private void Warn(string title, string msg) =>
        _tray.ShowBalloonTip(4000, title, msg, ToolTipIcon.Warning);

    protected override void Dispose(bool disposing)
    {
        if (disposing)
        {
            _watcher?.Dispose();
            _tray.Dispose();
        }
        base.Dispose(disposing);
    }
}

internal static class Program
{
    [STAThread]
    private static void Main()
    {
        ApplicationConfiguration.Initialize();
        using var app = new TrayApp();
        Application.Run(app);
    }
}
