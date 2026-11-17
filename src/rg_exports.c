/*
 * Windows-Export-Schicht fuer den RepackGuard-Kern.
 * Duenne Wrapper, damit C# per P/Invoke dieselbe Struktur nutzen kann.
 */
#include "rg_core.h"

#ifdef _WIN32
#  define EXPORT __declspec(dllexport)
#else
#  define EXPORT
#endif

EXPORT int rg_analyze_win(const rg_event_t *ev, int n,
                          long long window_sec, rg_report_t *out)
{
    return rg_analyze(ev, (size_t)n, window_sec, out);
}

EXPORT const char *rg_version_win(void)
{
    return rg_version();
}
