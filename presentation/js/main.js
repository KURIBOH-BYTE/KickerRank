


$(".nav-button").on("click", function () {
    $(".nav-button").removeClass("active");
    $(this).addClass("active");

    $(".page-section").addClass("hidden");

    const sectionId = $(this).data("section");
    $("#" + sectionId).removeClass("hidden");
});

function fetchRanking(){
    $.getJSON("test_data/ranking.json").done(renderRanking);
}


function renderRanking(players) {
    const tbody = $("#ranking-table-body");
    tbody.empty();
    players.forEach((player, index) => {
        const place = index + 1;
        const row = $("<tr></tr>");
        row.append(`<td>${place}</td>`);
        row.append(`<td>${player.first_name}</td>`);
        row.append(`<td cal>${player.last_name}</td>`);
        row.append(`<td><span class="department">${player.department}</span></td>`);
        row.append(`<td class="number number-elo">${player.elo}</td>`);
        row.append(`<td class="number">${player.games_played}</td>`);
        tbody.append(row);
    });
}

$(document).ready(function() {
    fetchRanking();
});