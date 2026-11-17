// Verbindet die C#-Seite mit der C-DLL und prueft den realen Vorfall.
using System.Diagnostics;
using RepackGuard.Tray;

static RgEvent Ev(long ts, int id, string path, string threat, int did) => new()
{
    ts = ts, event_id = id, path = path, threat = threat, did_execute = did,
    user = "TEST"
};

Console.WriteLine("RepackGuard — DLL-/Interop-Test");
Console.WriteLine("Kern-Version: " + Native.Version());

// Genau der Vorfall vom 14.11.2026
var incident = new[]
{
    Ev(1794933835, 1116, @"C:\Program Files (x86)\DODI-Repacks\...\steam_api64.dll", "Trojan:Win32/Occamy!rfn", 1),
    Ev(1794933855, 1117, @"C:\Program Files (x86)\DODI-Repacks\...\steam_api64.dll", "Trojan:Win32/Occamy!rfn", 1),
    Ev(1794934124, 1009, "Trojan:Win32/Occamy!rfn", "", 0),
    Ev(1794934125, 5007, @"HKLM\...\Exclusions\...\steam_api64.dll", "Trojan:Win32/Occamy!rfn", 0),
};
int alarm = Native.rg_analyze_win(incident, incident.Length, 86400, out var rep);
Console.WriteLine($"Vorfall -> alarm={alarm} reaktiviert={rep.repack_reactivated} ausnahme={rep.exclusion_set}");
Console.WriteLine("  " + rep.detail);

// Kontrollfall: nur Erkennung
var clean = new[]
{
    Ev(1000, 1116, @"C:\Spiel\game.dll", "Trojan:Win32/X!rfn", 1),
    Ev(1010, 1117, @"C:\Spiel\game.dll", "Trojan:Win32/X!rfn", 1),
};
int alarm2 = Native.rg_analyze_win(clean, clean.Length, 86400, out _);
Console.WriteLine($"Kontrolle -> alarm={alarm2}");

bool ok = alarm == 1 && rep.repack_reactivated == 1 && rep.exclusion_set == 1 && alarm2 == 0;
Console.WriteLine(ok ? "INTEROP OK" : "INTEROP FEHLER");
return ok ? 0 : 1;
