$(".nav-button").on("click", function () {
    $(".nav-button").removeClass("active");
    $(this).addClass("active");

    $(".page-section").addClass("hidden");

    const sectionId = $(this).data("section");
    $("#" + sectionId).removeClass("hidden");
});


// ---------- Helpers for talking to the server ----------

function sendJson(method, url, data) {
    return $.ajax({
        url: url,
        method: method,
        contentType: "application/json",
        data: data === undefined ? undefined : JSON.stringify(data),
    });
}

function errorMessage(xhr) {
    if (xhr.responseJSON && xhr.responseJSON.error) {
        return xhr.responseJSON.error;
    }
    return "Please fill in all fields.";
}

function numberOrNull(value) {
    return value === "" ? null : Number(value);
}

function showErrors(listSelector, errors) {
    const list = $(listSelector);
    list.empty();
    errors.forEach((error) => list.append(`<li>${error}</li>`));
}


// ---------- Ranking and player dropdowns ----------

function fetchRanking() {
    $.getJSON("/api/ranking").done(function (players) {
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
        const selected = select.val();
        select.find("option:not(:first)").remove();
        players.forEach((player) => {
            select.append(`<option value="${player.id}">${player.first_name} ${player.last_name} (${player.department})</option>`);
        });
        select.val(selected);
    });
}


// ---------- Add player ----------

function fetchDepartments() {
    $.getJSON("/api/departments").done(function (departments) {
        $("#department, #edit-department").each(function () {
            const select = $(this);
            departments.forEach((department) => {
                select.append(`<option value="${department}">${department}</option>`);
            });
        });
    });
}

$("#player-form").on("submit", function (event) {
    event.preventDefault();
    showErrors("#player-errors", []);
    $("#player-success").text("");

    const playerData = {
        first_name: $("#first-name").val(),
        last_name: $("#last-name").val(),
        department: $("#department").val(),
    };

    sendJson("POST", "/api/players", playerData)
        .done(function (player) {
            $("#player-form")[0].reset();
            $("#player-success").text(`${player.first_name} ${player.last_name} was added.`);
            fetchRanking();
            fetchAllPlayers();
        })
        .fail(function (xhr) {
            showErrors("#player-errors", [errorMessage(xhr)]);
        });
});


// ---------- Edit player ----------

let allPlayers = [];

function fetchAllPlayers() {
    $.getJSON("/api/players").done(function (players) {
        allPlayers = players;
        const select = $("#edit-player");
        select.find("option:not(:first)").remove();
        players.forEach((player) => {
            const status = player.active ? "" : " – inactive";
            select.append(`<option value="${player.id}">${player.first_name} ${player.last_name} (${player.department})${status}</option>`);
        });
    });
}

$("#edit-player").on("change", function () {
    showErrors("#edit-player-errors", []);
    $("#edit-player-success").text("");

    let player = null;
    for (const entry of allPlayers) {
        if (entry.id === Number($(this).val())) {
            player = entry;
        }
    }

    $("#edit-first-name").val(player ? player.first_name : "");
    $("#edit-last-name").val(player ? player.last_name : "");
    $("#edit-department").val(player ? player.department : "");
    $("#edit-active").val(player && !player.active ? "false" : "true");
    $("#update-player").prop("disabled", player === null);
});

$("#edit-player-form").on("submit", function (event) {
    event.preventDefault();
    showErrors("#edit-player-errors", []);
    $("#edit-player-success").text("");

    const playerData = {
        first_name: $("#edit-first-name").val(),
        last_name: $("#edit-last-name").val(),
        department: $("#edit-department").val(),
        active: $("#edit-active").val() === "true",
    };

    sendJson("PUT", `/api/players/${$("#edit-player").val()}`, playerData)
        .done(function (player) {
            $("#edit-player-form")[0].reset();
            $("#update-player").prop("disabled", true);
            $("#edit-player-success").text(`${player.first_name} ${player.last_name} was updated.`);
            fetchRanking();
            fetchAllPlayers();
            fetchLastGame();
        })
        .fail(function (xhr) {
            showErrors("#edit-player-errors", [errorMessage(xhr)]);
        });
});


// ---------- New game ----------

$("#game-form").on("submit", function (event) {
    event.preventDefault();
    showErrors("#game-errors", []);
    $("#game-success").text("");

    const gameData = {
        player_a_id: Number($("#player-a").val()),
        player_b_id: Number($("#player-b").val()),
        goals_a: numberOrNull($("#goals-a").val()),
        goals_b: numberOrNull($("#goals-b").val()),
    };

    sendJson("POST", "/api/games", gameData)
        .done(function (game) {
            $("#goals-a, #goals-b").val("");
            $("#game-success").text(`Game saved. Elo ±${game.elo_change}`);
            renderLastGame(game);
            fetchRanking();
        })
        .fail(function (xhr) {
            showErrors("#game-errors", [errorMessage(xhr)]);
        });
});


// ---------- Last game: show, edit, delete ----------

let lastGame = null;

function fetchLastGame() {
    $.getJSON("/api/games/last").done(renderLastGame);
}

function playerName(player) {
    return `${player.first_name} ${player.last_name}`;
}

function renderLastGame(game) {
    lastGame = game;
    showErrors("#last-game-errors", []);

    if (game === null) {
        $("#last-game .last-game-result").text("No games yet.");
        $("#last-game .last-game-info").text("");
        $("#last-game .last-game-actions").empty();
        return;
    }

    const winnerIsA = game.winner_id === game.player_a.id;
    $("#last-game .last-game-result").html(
        `<span class="${winnerIsA ? "winner" : ""}">${playerName(game.player_a)}</span>
         ${game.goals_a} : ${game.goals_b}
         <span class="${winnerIsA ? "" : "winner"}">${playerName(game.player_b)}</span>`
    );

    const date = new Date(game.played_at).toLocaleString("de-CH", {
        day: "2-digit", month: "2-digit", year: "numeric", hour: "2-digit", minute: "2-digit",
    });
    $("#last-game .last-game-info").text(`${date} · Elo ±${game.elo_change}`);

    $("#last-game .last-game-actions").html(
        `<button type="button" class="edit-button" id="edit-game">Edit</button>
         <button type="button" class="danger-button" id="delete-game">Delete</button>`
    );
}

$("#last-game").on("click", "#edit-game", function () {
    $("#last-game .last-game-result").html(
        `${playerName(lastGame.player_a)}
         <input type="number" id="edit-goals-a" min="0" max="10" value="${lastGame.goals_a}">
         :
         <input type="number" id="edit-goals-b" min="0" max="10" value="${lastGame.goals_b}">
         ${playerName(lastGame.player_b)}`
    );
    $("#last-game .last-game-actions").html(
        `<button type="button" class="submit-button" id="save-game">Save</button>
         <button type="button" class="edit-button" id="cancel-edit">Cancel</button>`
    );
});

$("#last-game").on("click", "#save-game", function () {
    const result = {
        goals_a: numberOrNull($("#edit-goals-a").val()),
        goals_b: numberOrNull($("#edit-goals-b").val()),
    };

    sendJson("PUT", `/api/games/${lastGame.id}`, result)
        .done(function (game) {
            renderLastGame(game);
            fetchRanking();
        })
        .fail(function (xhr) {
            showErrors("#last-game-errors", [errorMessage(xhr)]);
        });
});

$("#last-game").on("click", "#cancel-edit", function () {
    renderLastGame(lastGame);
});

$("#last-game").on("click", "#delete-game", function () {
    $("#last-game .last-game-actions").html(
        `<span class="confirm-text">Delete this game?</span>
         <button type="button" class="danger-button" id="confirm-delete">Yes, delete</button>
         <button type="button" class="edit-button" id="cancel-delete">Cancel</button>`
    );
});

$("#last-game").on("click", "#confirm-delete", function () {
    sendJson("DELETE", `/api/games/${lastGame.id}`)
        .done(function () {
            fetchLastGame();
            fetchRanking();
        })
        .fail(function (xhr) {
            showErrors("#last-game-errors", [errorMessage(xhr)]);
        });
});

$("#last-game").on("click", "#cancel-delete", function () {
    renderLastGame(lastGame);
});


$(document).ready(function () {
    fetchRanking();
    fetchAllPlayers();
    fetchDepartments();
    fetchLastGame();
});
