$(".nav-button").on("click", function () {
    $(".nav-button").removeClass("active");
    $(this).addClass("active");

    $(".page-section").addClass("hidden");

    const sectionId = $(this).data("section");
    $("#" + sectionId).removeClass("hidden");
});

function fetchRanking() {
    $.getJSON("test_data/ranking.json").done(function (players) {
        renderRanking(players);
        fillPlayersInDropdown(players);
    });
}


function renderRanking(players) {
    const tbody = $("#ranking-table-body");
    tbody.empty();
    players.forEach((player, index) => {
        const place = index + 1;
        const row = $("<tr></tr>");
        row.append(`<td>${place}</td>`);
        row.append(`<td>${player.first_name}</td>`);
        row.append(`<td>${player.last_name}</td>`);
        row.append(`<td><span class="department">${player.department}</span></td>`);
        row.append(`<td class="number number-elo">${player.elo}</td>`);
        row.append(`<td class="number">${player.games_played}</td>`);
        tbody.append(row);
    });
}

function fillPlayersInDropdown(players) {
    $("#player-a, #player-b").each(function () {
        const select = $(this);
        select.find("option:not(:first)").remove();
        players.forEach((player) => {
            select.append(`<option value="${player.id}">${player.first_name} ${player.last_name} (${player.department})</option>`);
        });
    });
}

function showErrors(errors) {
    const list = $("#game-errors");
    list.empty();
    errors.forEach((error) => list.append(`<li>${error}</li>`));
}

$("#game-form").on("submit", function (event) {
    event.preventDefault();
    showErrors([]);
    $("#game-success").text("");

    const gameData = {
        player_a_id: Number($("#player-a").val()),
        player_b_id: Number($("#player-b").val()),
        goals_a: Number($("#goals-a").val()),
        goals_b: Number($("#goals-b").val()),
    };
    console.log(gameData);
    $("#game-success").text("Saving follows in T17.");
});

function fetchDepartments() {
    $.getJSON("test_data/departments.json").done(function (departments) {
        const select = $("#department");
        departments.forEach((department) => {
            select.append(`<option value="${department}">${department}</option>`);
        });
    });
}

function fetchLastGame() {
    $.getJSON("test_data/last_game.json").done(renderLastGame);
}

function renderLastGame(game) {
    const playerA = `${game.player_a.first_name} ${game.player_a.last_name}`;
    const playerB = `${game.player_b.first_name} ${game.player_b.last_name}`;
    const winnerIsA = game.winner_id === game.player_a.id;

    $("#last-game .last-game-result").html(
        `<span class="${winnerIsA ? "winner" : ""}">${playerA}</span>
         ${game.goals_a} : ${game.goals_b}
         <span class="${winnerIsA ? "" : "winner"}">${playerB}</span>`
    );

    const date = new Date(game.played_at).toLocaleString("de-CH", {
        day: "2-digit", month: "2-digit", year: "numeric", hour: "2-digit", minute: "2-digit",
    });
    $("#last-game .last-game-info").text(`${date} · Elo ±${game.elo_change}`);
}

$("#player-form").on("submit", function (event) {
    event.preventDefault();
});

$(document).ready(function () {
    fetchRanking();
    fetchDepartments();
    fetchLastGame();
});