#include "rg_core.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define RG_VER "0.1.0"

/* Defender-Ereignis-IDs */
#define EV_THREAT_DETECTED 1116  /* Schadsoftware erkannt */
#define EV_THREAT_REMOVED  1117  /* Aktion ausgefuehrt (Quarantaeune) */
#define EV_QUARANTINE_RESTORE 1009 /* aus Quarantaeune wiederhergestellt */
#define EV_CONFIG_CHANGE   5007  /* Konfigurationsaenderung (u. a. Ausnahmen) */

const char *rg_version(void) { return RG_VER; }

/* Letzten Pfadteil zurueckgeben (Dateiname). */
static const char *file_name(const char *path)
{
    const char *s = strrchr(path, '\\');
    const char *f = strrchr(path, '/');
    if (f > s) s = f;
    return s ? s + 1 : path;
}

/* Gehoeren zwei Pfade zusammen? (gleicher Dateiname oder gleicher Threat-Name) */
static int same_target(const char *a, const char *b, const char *threat)
{
    const char *fa = file_name(a);
    const char *fb = file_name(b);
    if (fa[0] && strstr(a, fb)) return 1;
    if (fb[0] && strstr(b, fa)) return 1;
    if (threat && threat[0]) {
        if (strstr(a, threat)) return 1;
        if (strstr(b, threat)) return 1;
    }
    return 0;
}

static int is_threat_event(int id)
{
    return id == EV_THREAT_DETECTED || id == EV_THREAT_REMOVED;
}

static int is_exclusion_change(const rg_event_t *e)
{
    if (e->event_id != EV_CONFIG_CHANGE) return 0;
    /* Der Ausnahme-Pfad steht im Ereignis in HKLM\...\Exclusions\... */
    return strstr(e->path, "Exclusions") != NULL;
}

int rg_analyze(const rg_event_t *ev, size_t n, long long window_sec, rg_report_t *out)
{
    size_t i, j;
    int alarm = 0;

    if (!ev || !out) return 0;

    memset(out, 0, sizeof(*out));
    strcpy(out->detail, "keine Auffaelligkeit");

    if (n == 0) return 0;

    /* 1) Bedrohung ausgeführt? */
    for (i = 0; i < n; i++) {
        if (is_threat_event(ev[i].event_id) && ev[i].did_execute) {
            out->threat_executed = 1;
            snprintf(out->threat, sizeof(out->threat), "%s", ev[i].threat);
            break;
        }
    }

    /* 2) Kette: Erkennung -> Restore aus Quarantaeune */
    for (i = 0; i < n; i++) {
        if (!is_threat_event(ev[i].event_id)) continue;
        for (j = 0; j < n; j++) {
            if (ev[j].event_id != EV_QUARANTINE_RESTORE) continue;
            if (ev[j].ts < ev[i].ts) continue;
            if ((ev[j].ts - ev[i].ts) > window_sec) continue;
            /* gleiche Datei? (Restore nennt den Schadsoftware-Namen) */
            if (same_target(ev[j].path, ev[i].path, ev[i].threat)) {
                out->repack_reactivated = 1;
                snprintf(out->detail, sizeof(out->detail),
                         "Erkennung (%d) um %lld, Restore aus Quarantaeune (%d) um %lld",
                         ev[i].event_id, ev[i].ts, ev[j].event_id, ev[j].ts);
                alarm = 1;
            }
        }
    }

    /* 3) Kette: Erkennung -> Ausnahme gesetzt */
    for (i = 0; i < n; i++) {
        if (!is_threat_event(ev[i].event_id)) continue;
        for (j = 0; j < n; j++) {
            if (!is_exclusion_change(&ev[j])) continue;
            if (ev[j].ts < ev[i].ts) continue;
            if ((ev[j].ts - ev[i].ts) > window_sec) continue;
            if (same_target(ev[j].path, ev[i].path, ev[i].threat)) {
                out->exclusion_set = 1;
                if (!alarm) {
                    snprintf(out->detail, sizeof(out->detail),
                             "Erkennung (%d) um %lld, Ausnahme gesetzt um %lld",
                             ev[i].event_id, ev[i].ts, ev[j].ts);
                }
                alarm = 1;
            }
        }
    }

    if (alarm && out->threat[0] == '\0') {
        /* Name ggf. aus einem anderen Threat-Event holen */
        for (i = 0; i < n; i++) {
            if (is_threat_event(ev[i].event_id) && ev[i].threat[0]) {
                snprintf(out->threat, sizeof(out->threat), "%s", ev[i].threat);
                break;
            }
        }
    }

    return alarm;
}
