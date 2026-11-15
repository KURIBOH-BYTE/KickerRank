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

function validateGameInput(game) {
    const errors = [];

    if (game.player_a_id === "" || game.player_b_id === "") {
        errors.push("Please choose two players.");
    } else if (game.player_a_id === game.player_b_id) {
        errors.push("A player cannot play against themselves.");
    }

    if (game.goals_a === "" || game.goals_b === "") {
        errors.push("Please enter the goals for both players.");
    } else {
        const goalsA = Number(game.goals_a);
        const goalsB = Number(game.goals_b);
        const validA = Number.isInteger(goalsA) && goalsA >= 0 && goalsA <= 10;
        const validB = Number.isInteger(goalsB) && goalsB >= 0 && goalsB <= 10;
        if (!validA || !validB) {
            errors.push("Goals must be whole numbers from 0 to 10.");
        }
    }

    return errors;
}

function showErrors(errors) {
    const list = $("#game-errors");
    list.empty();
    errors.forEach((error) => list.append(`<li>${error}</li>`));
}

$("#game-form").on("submit", function (event) {
    event.preventDefault();
    $("#game-success").text("");

    const game = {
        player_a_id: $("#player-a").val(),
        player_b_id: $("#player-b").val(),
        goals_a: $("#goals-a").val(),
        goals_b: $("#goals-b").val(),
    };
    const errors = validateGameInput(game);
    showErrors(errors);

    if (errors.length === 0) {
        const gameData = {
            player_a_id: Number(game.player_a_id),
            player_b_id: Number(game.player_b_id),
            goals_a: Number(game.goals_a),
            goals_b: Number(game.goals_b),
        };
        console.log(gameData);
        $("#game-success").text("Input is valid. Saving follows in T17.");
    }
});

$(document).ready(function () {
    fetchRanking();
});