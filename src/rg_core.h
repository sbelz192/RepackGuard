#ifndef RG_CORE_H
#define RG_CORE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Ein Defender-Ereignis, so weit der Kern es braucht. */
typedef struct {
    long long ts;             /* Unixzeit (Sekunden) */
    int       event_id;       /* 1116/1117 Erkennung, 1009 Restore, 5007 Config */
    char      user[128];      /* Benutzer, der die Aktion ausgeloest hat */
    char      path[512];      /* betroffene Datei / Registry-Pfad */
    char      threat[128];    /* Schadsoftware-Name */
    int       did_execute;    /* DidThreatExecute */
} rg_event_t;

/* Ergebnis der Analyse. */
typedef struct {
    int  repack_reactivated;  /* 1116/1117 gefolgt von 1009 (Restore) */
    int  exclusion_set;       /* 5007 mit Exclusions-Pfad */
    int  threat_executed;     /* mind. ein Ereignis mit did_execute=1 */
    char threat[128];         /* Name der Schadsoftware */
    char detail[512];         /* lesbare Begruendung */
} rg_report_t;

/*
 * Analysiert eine Liste von Ereignissen (chronologisch aufsteigend).
 * window_sec: Maximale Zeit zwischen Erkennung und Restore/Ausnahme.
 * out: Report (nicht NULL).
 * Rueckgabe: 1 = Alarm (Repack-Reaktion erkannt), 0 = unauffaellig.
 */
int rg_analyze(const rg_event_t *ev, size_t n, long long window_sec, rg_report_t *out);

/* Version des Kerns. */
const char *rg_version(void);

#ifdef __cplusplus
}
#endif

#endif /* RG_CORE_H */
