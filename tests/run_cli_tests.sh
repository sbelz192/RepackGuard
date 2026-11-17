#!/usr/bin/env bash
# CLI-Tests: prueft Exit-Codes und Ausgaben gegen die echten Testdaten.
# Aufruf: run_cli_tests.sh <pfad-zur-exe> <pfad-zu-testdata>
set -u
CLI="$1"
DATA="$2"
fail=0

echo "== Test: Vorfall (erwartet ALARM, Exit 1) =="
"$CLI" "$DATA/ds2_incident.tsv" > "$DATA/.incident.out" 2>&1
rc=$?
grep -q "ALARM" "$DATA/.incident.out" || { echo "  FEHL: Ausgabe enthaelt kein ALARM"; fail=1; }
if [ "$rc" -ne 1 ]; then echo "  FEHL: Exit $rc statt 1"; fail=1; else echo "  ok   Exit 1"; fi
grep -q "Repack reaktiviert:    ja" "$DATA/.incident.out" || { echo "  FEHL: nicht als reaktiviert erkannt"; fail=1; }

echo "== Test: Kontrolle (erwartet ok, Exit 0) =="
"$CLI" "$DATA/control_clean.tsv" > "$DATA/.control.out" 2>&1
rc=$?
grep -q "ERGEBNIS: ok" "$DATA/.control.out" || { echo "  FEHL: Ausgabe enthaelt kein 'ok'"; fail=1; }
if [ "$rc" -ne 0 ]; then echo "  FEHL: Exit $rc statt 0"; fail=1; else echo "  ok   Exit 0"; fi

echo "== Ergebnis: $([ $fail -eq 0 ] && echo ALLE OK || echo FEHLER) =="
exit $fail
