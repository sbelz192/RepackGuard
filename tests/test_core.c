/*
 * Test den Kern direkt (kein Dateizugriff).
 * Kompiliert mit: gcc tests/test_core.c src/rg_core.c -o test_core
 */
#include "../src/rg_core.h"

#include <stdio.h>
#include <string.h>

static int failures = 0;

static void expect(const char *name, int got, int want)
{
    if (got == want) {
        printf("  ok   %s\n", name);
    } else {
        printf("  FEHL %s (erwartet %d, bekam %d)\n", name, want, got);
        failures++;
    }
}

static rg_event_t ev(long long ts, int id, const char *path,
                      const char *threat, int did)
{
    rg_event_t e;
    memset(&e, 0, sizeof(e));
    e.ts = ts;
    e.event_id = id;
    snprintf(e.path, sizeof(e.path), "%s", path ? path : "");
    snprintf(e.threat, sizeof(e.threat), "%s", threat ? threat : "");
    e.did_execute = did;
    return e;
}

int main(void)
{
    rg_report_t r;
    rg_event_t e[4];

    printf("RepackGuard %s — Kern-Tests\n", rg_version());

    /* Fall 1: der reale Vorfall (Erkennung -> Restore -> Ausnahme) */
    e[0] = ev(1794933835, 1116, "steam_api64.dll", "Trojan:Win32/Occamy!rfn", 1);
    e[1] = ev(1794933855, 1117, "steam_api64.dll", "Trojan:Win32/Occamy!rfn", 1);
    e[2] = ev(1794934124, 1009, "Trojan:Win32/Occamy!rfn", "", 0);
    e[3] = ev(1794934125, 5007, "HKLM\\...\\Exclusions\\...\\steam_api64.dll",
              "Trojan:Win32/Occamy!rfn", 0);
    expect("Vorfall: Alarm", rg_analyze(e, 4, 86400, &r), 1);
    expect("Vorfall: reaktiviert", r.repack_reactivated, 1);
    expect("Vorfall: Ausnahme", r.exclusion_set, 1);
    expect("Vorfall: ausgefuehrt", r.threat_executed, 1);

    /* Fall 2: Erkennung, aber keine Wiederherstellung */
    e[0] = ev(1000, 1116, "game.dll", "Trojan:Win32/X!rfn", 1);
    e[1] = ev(1010, 1117, "game.dll", "Trojan:Win32/X!rfn", 1);
    expect("Nur Erkennung: kein Alarm", rg_analyze(e, 2, 86400, &r), 0);
    expect("Nur Erkennung: nicht reaktiviert", r.repack_reactivated, 0);

    /* Fall 3: Ausnahme ohne jede Bedrohung */
    e[0] = ev(5000, 5007, "HKLM\\...\\Exclusions\\...\\foo.dll", "", 0);
    expect("Ausnahme allein: kein Alarm", rg_analyze(e, 1, 86400, &r), 0);

    /* Fall 4: Restore, aber zu weit zurueck (ausser Fenster) */
    e[0] = ev(0,    1116, "steam_api64.dll", "Trojan:Win32/Occamy!rfn", 1);
    e[1] = ev(90000, 1009, "Trojan:Win32/Occamy!rfn", "", 0);
    expect("Restore ausser Fenster: kein Alarm", rg_analyze(e, 2, 3600, &r), 0);

    printf("%s: %d Fehler\n", failures ? "FEHLER" : "ALLE OK", failures);
    return failures ? 1 : 0;
}
