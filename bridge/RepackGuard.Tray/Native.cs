using System.Runtime.InteropServices;

namespace RepackGuard.Tray;

// Layout muss exakt src/rg_core.h entsprechen.
[StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
public struct RgEvent
{
    public long ts;
    public int event_id;
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 128)] public string user;
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 512)] public string path;
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 128)] public string threat;
    public int did_execute;
}

[StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
public struct RgReport
{
    public int repack_reactivated;
    public int exclusion_set;
    public int threat_executed;
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 128)] public string threat;
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 512)] public string detail;
}

public static class Native
{
    [DllImport("rg_core.dll", CallingConvention = CallingConvention.Cdecl)]
    public static extern int rg_analyze_win([In] RgEvent[] ev, int n, long windowSec, out RgReport output);

    [DllImport("rg_core.dll", CallingConvention = CallingConvention.Cdecl)]
    public static extern IntPtr rg_version_win();

    public static string Version()
    {
        try { return Marshal.PtrToStringAnsi(rg_version_win()) ?? "?"; }
        catch { return "?"; }
    }
}
