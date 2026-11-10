$(".nav-button").on("click", function () {
    $(".nav-button").removeClass("active");
    $(this).addClass("active");

    $(".page-section").addClass("hidden");

    const sectionId = $(this).data("section");
    $("#" + sectionId).removeClass("hidden");
});
