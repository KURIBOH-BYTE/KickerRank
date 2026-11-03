// Präsentationsschicht: holt Daten per AJAX vom Service Layer und zeigt sie an.
// Hier wird nichts berechnet – alle Regeln liegen im Business Layer.

// ---------- Hilfsfunktionen ----------

// Sendet JSON an das API und gibt ein jQuery-Promise zurück.
function api(methode, url, daten) {
  return $.ajax({
    url: url,
    method: methode,
    contentType: "application/json",
    data: daten ? JSON.stringify(daten) : undefined,
  });
}

// Liest die Fehlermeldung aus der Antwort des Servers.
function fehlertext(xhr) {
  if (xhr.responseJSON && xhr.responseJSON.fehler) return xhr.responseJSON.fehler;
  return "Unerwarteter Fehler (" + xhr.status + ").";
}

function zeigeMeldung(id, text, istFehler) {
  $(id).text(text).toggleClass("fehler", istFehler).toggleClass("ok", !istFehler);
}

// Verhindert, dass Namen als HTML interpretiert werden.
function esc(text) {
  return $("<div>").text(text).html();
}

function vorzeichen(zahl) {
  return zahl > 0 ? "+" + zahl : String(zahl);
}

// ---------- Rangliste ----------

function ladeRangliste() {
  api("GET", "/api/rangliste").done(function (spieler) {
    const zeilen = spieler.map(function (s, i) {
      return "<tr><td>" + (i + 1) + "</td><td>" + esc(s.name) + "</td><td>" +
        esc(s.abteilung) + "</td><td class='zahl'>" + s.elo + "</td><td class='zahl'>" +
        s.anzahl_spiele + "</td></tr>";
    });
    $("#rangliste-zeilen").html(zeilen.join(""));

    // Dieselben Daten füllen die Dropdowns beim Spiel erfassen.
    const optionen = spieler
      .slice()
      .sort(function (a, b) { return a.name.localeCompare(b.name); })
      .map(function (s) { return "<option value='" + s.id + "'>" + esc(s.name) + " (" + s.elo + ")</option>"; });
    $(".spieler-auswahl").each(function () {
      const gewaehlt = $(this).val();
      $(this).html(optionen.join(""));
      if (gewaehlt) $(this).val(gewaehlt);
    });
    if (!$("#spieler-b").data("gesetzt") && spieler.length > 1) {
      $("#spieler-b").prop("selectedIndex", 1).data("gesetzt", true);
    }
  });
}

function ladeAbteilungen() {
  api("GET", "/api/abteilungen").done(function (liste) {
    $("#spieler-abteilung").html(liste.map(function (a) {
      return "<option>" + esc(a) + "</option>";
    }).join(""));
  });
}

$("#spieler-form").on("submit", function (e) {
  e.preventDefault();
  api("POST", "/api/spieler", {
    name: $("#spieler-name").val(),
    abteilung: $("#spieler-abteilung").val(),
  })
    .done(function (s) {
      zeigeMeldung("#spieler-meldung", s.name + " wurde mit " + s.elo + " Elo hinzugefügt.", false);
      $("#spieler-name").val("");
      ladeRangliste();
    })
    .fail(function (xhr) { zeigeMeldung("#spieler-meldung", fehlertext(xhr), true); });
});

// ---------- Spiel erfassen ----------

function ergebnisText(spiel) {
  const a = spiel.spieler_a, b = spiel.spieler_b;
  const aGewinnt = spiel.tore_a > spiel.tore_b;
  const d = spiel.elo_aenderung;
  return a.name + " " + vorzeichen(aGewinnt ? d : -d) + " (" + a.elo + "), " +
         b.name + " " + vorzeichen(aGewinnt ? -d : d) + " (" + b.elo + ")";
}

$("#spiel-form").on("submit", function (e) {
  e.preventDefault();
  api("POST", "/api/spiele", {
    spieler_a_id: Number($("#spieler-a").val()),
    spieler_b_id: Number($("#spieler-b").val()),
    tore_a: Number($("#tore-a").val()),
    tore_b: Number($("#tore-b").val()),
  })
    .done(function (spiel) {
      zeigeMeldung("#spiel-meldung", "Gespeichert: " + ergebnisText(spiel), false);
      aktualisiereAlles();
    })
    .fail(function (xhr) { zeigeMeldung("#spiel-meldung", fehlertext(xhr), true); });
});

// ---------- Letztes Spiel: anzeigen, korrigieren, löschen ----------

function ladeLetztesSpiel() {
  api("GET", "/api/spiele/letztes").done(function (spiel) {
    const box = $("#letztes-spiel");
    if (!spiel) {
      box.html("<p class='info'>Noch keine Spiele erfasst.</p>");
      return;
    }
    const zeit = new Date(spiel.gespielt_am).toLocaleString("de-CH",
      { dateStyle: "short", timeStyle: "short" });
    box.html(
      "<div class='resultat'>" + esc(spiel.spieler_a.name) + " " + spiel.tore_a + " : " +
        spiel.tore_b + " " + esc(spiel.spieler_b.name) + "</div>" +
      "<div class='info'>" + zeit + " · Sieger: " + esc(spiel.gewinner) +
        " · <span class='plus'>±" + spiel.elo_aenderung + " Elo</span></div>" +
      "<div class='aktionen'>" +
        "<input id='korr-a' type='number' min='0' max='10' value='" + spiel.tore_a + "' aria-label='Tore A'>" +
        "<span>:</span>" +
        "<input id='korr-b' type='number' min='0' max='10' value='" + spiel.tore_b + "' aria-label='Tore B'>" +
        "<button class='sekundaer' id='korrigieren'>Resultat korrigieren</button>" +
        "<button class='gefahr' id='loeschen'>Löschen</button>" +
      "</div>"
    ).data("spiel-id", spiel.id);
  });
}

$("#letztes-spiel").on("click", "#korrigieren", function () {
  const id = $("#letztes-spiel").data("spiel-id");
  api("PUT", "/api/spiele/" + id, {
    tore_a: Number($("#korr-a").val()),
    tore_b: Number($("#korr-b").val()),
  })
    .done(function (spiel) {
      zeigeMeldung("#spiel-meldung", "Korrigiert: " + ergebnisText(spiel), false);
      aktualisiereAlles();
    })
    .fail(function (xhr) { zeigeMeldung("#spiel-meldung", fehlertext(xhr), true); });
});

$("#letztes-spiel").on("click", "#loeschen", function () {
  const id = $("#letztes-spiel").data("spiel-id");
  api("DELETE", "/api/spiele/" + id)
    .done(function () {
      zeigeMeldung("#spiel-meldung", "Spiel gelöscht, Elo wurde zurückgesetzt.", false);
      aktualisiereAlles();
    })
    .fail(function (xhr) { zeigeMeldung("#spiel-meldung", fehlertext(xhr), true); });
});

// ---------- Navigation und Start ----------

$(".tab").on("click", function () {
  $(".tab").removeClass("aktiv");
  $(this).addClass("aktiv");
  $(".bereich").addClass("versteckt");
  $("#" + $(this).data("bereich")).removeClass("versteckt");
});

function aktualisiereAlles() {
  ladeRangliste();
  ladeLetztesSpiel();
}

$(function () {
  ladeAbteilungen();
  aktualisiereAlles();
});
