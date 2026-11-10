"""Legt alle Tickets aus tickets.json als GitHub-Issues an (mit Labels und Meilensteinen).

Aufruf im Ordner planung/:
    python3 github_issues_erstellen.py --dry-run   # nur anzeigen, nichts anlegen
    python3 github_issues_erstellen.py             # wirklich anlegen

Voraussetzung: GitHub CLI (`gh`) installiert und angemeldet (`gh auth login`).
Das Skript kann gefahrlos erneut gestartet werden: bestehende Issues mit gleichem Titel werden übersprungen.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = "KURIBOH-BYTE/KickerRank"
FARBEN = {"Setup": "6e7781", "Test": "0e8a16", "Doku": "c5def5", "Presentation": "a371f7",
          "Service": "1f6feb", "Business": "d4a72c", "Persistence": "bf5b04",
          "Erweiterung": "e99695", "Verteidigung": "5319e7"}
DRY = "--dry-run" in sys.argv
HIER = Path(__file__).parent


def gh(*args, capture=True):
    if DRY:
        print("  gh", " ".join(a if " " not in a else f'"{a}"' for a in args)[:160])
        return ""
    r = subprocess.run(["gh", *args], capture_output=capture, text=True)
    if r.returncode != 0:
        raise SystemExit(f"Fehler bei gh {' '.join(args[:3])}: {r.stderr.strip()}")
    return r.stdout.strip()


def main():
    daten = json.loads((HIER / "tickets.json").read_text(encoding="utf-8"))

    print("Labels anlegen ...")
    for name, farbe in FARBEN.items():
        gh("label", "create", name, "--color", farbe, "--force", "--repo", REPO)

    print("Meilensteine anlegen ...")
    vorhanden = set() if DRY else set(json.loads(gh("api", f"repos/{REPO}/milestones?state=all&per_page=100", "--jq", "[.[].title]") or "[]"))
    for m in daten["meilensteine"]:
        if m not in vorhanden:
            gh("api", f"repos/{REPO}/milestones", "-f", f"title={m}")

    print("Issues anlegen ...")
    bestehend = {} if DRY else {i["title"]: i["number"] for i in json.loads(
        gh("issue", "list", "--repo", REPO, "--state", "all", "--limit", "500", "--json", "title,number"))}
    nummer = {}
    for t in daten["tickets"]:
        if t["titel"] in bestehend:
            nummer[t["id"]] = bestehend[t["titel"]]
            print(f"  übersprungen (existiert): {t['titel']}")
            continue
        text = (HIER / t["datei"]).read_text(encoding="utf-8").split("\n", 2)[2]  # Titelzeile weglassen
        if t["abh"]:
            verweise = ", ".join(f"#{nummer[a]} ({a})" if a in nummer else a for a in t["abh"])
            text = text.replace(f"**Abhängig von:** {', '.join(t['abh'])}", f"**Abhängig von:** {verweise}")
        args = ["issue", "create", "--repo", REPO, "--title", t["titel"], "--body", text, "--milestone", t["meilenstein"]]
        for l in t["labels"]:
            args += ["--label", l]
        url = gh(*args)
        if not DRY:
            nummer[t["id"]] = int(url.rstrip("/").split("/")[-1])
            print(f"  {t['titel']} → {url}")
    print("Fertig." if not DRY else "Dry-Run beendet, nichts angelegt.")


if __name__ == "__main__":
    main()
