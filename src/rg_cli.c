/*
 * rg_cli — liest ein TSV mit Defender-Ereignissen und lasst den Kern analysieren.
 *
 * TSV-Spalten (Reihenfolge):
 *   ts  event_id  user  path  threat  did_execute
 *
 * Ausgabe: Report (Text). Exit-Code 1 bei Alarm, 0 sonst.
 */
#include "rg_core.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_EVENTS 4096

static int read_events(const char *path, rg_event_t *ev, int max)
{
    FILE *f;
    char line[2048];
    int n = 0;

    f = fopen(path, "r");
    if (!f) {
        fprintf(stderr, "Kann Datei nicht oeffnen: %s\n", path);
        return -1;
    }

    while (fgets(line, sizeof(line), f) && n < max) {
        char *fields[6];
        int nf = 0;
        char *p = line;
        char *start = line;

        /* Splitten per Tab, aber path darf Tabs nicht enthalten */
        fields[nf++] = start;
        while (*p) {
            if (*p == '\t') { *p = '\0'; if (nf < 6) fields[nf++] = p + 1; }
            else if (*p == '\n' || *p == '\r') { *p = '\0'; break; }
            p++;
        }
        (void)start;

        if (nf < 5) continue;

        memset(&ev[n], 0, sizeof(ev[n]));
        ev[n].ts = atoll(fields[0]);
        ev[n].event_id = atoi(fields[1]);
        snprintf(ev[n].user, sizeof(ev[n].user), "%s", fields[2]);
        snprintf(ev[n].path, sizeof(ev[n].path), "%s", fields[3]);
        snprintf(ev[n].threat, sizeof(ev[n].threat), "%s", fields[4]);
        ev[n].did_execute = (nf >= 6) ? atoi(fields[5]) : 0;
        n++;
    }

    fclose(f);
    return n;
}

int main(int argc, char **argv)
{
    rg_event_t *ev;
    rg_report_t rep;
    int n;
    long long window = 86400;
    int alarm;
    int rc = 0;

    if (argc < 2) {
        fprintf(stderr, "Verwendung: %s <events.tsv> [fenster_sek]\n", argv[0]);
        return 2;
    }
    if (argc >= 3) window = atoll(argv[2]);

    /* Heap, nicht Stack: 4096 * ~800 Byte waeren ~3 MB. */
    ev = (rg_event_t *)calloc(MAX_EVENTS, sizeof(rg_event_t));
    if (!ev) {
        fprintf(stderr, "Kein Speicher.\n");
        return 2;
    }

    n = read_events(argv[1], ev, MAX_EVENTS);
    if (n < 0) { rc = 2; goto done; }

    alarm = rg_analyze(ev, (size_t)n, window, &rep);

    printf("RepackGuard %s\n", rg_version());
    printf("Ereignisse: %d, Fenster: %lld s\n", n, window);
    printf("Bedrohung ausgefuehrt: %s (%s)\n",
           rep.threat_executed ? "ja" : "nein", rep.threat);
    printf("Repack reaktiviert:    %s\n", rep.repack_reactivated ? "ja" : "nein");
    printf("Ausnahme gesetzt:      %s\n", rep.exclusion_set ? "ja" : "nein");
    printf("Detail: %s\n", rep.detail);
    printf("ERGEBNIS: %s\n", alarm ? "ALARM" : "ok");

    rc = alarm ? 1 : 0;

done:
    free(ev);
    return rc;
}
