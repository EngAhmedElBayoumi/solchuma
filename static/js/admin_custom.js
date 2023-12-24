$(document).ready(function () {
    // Hide all .nav-item until the next .nav-header
    $(".nav-header").nextUntil(".nav-header").filter(".nav-item").hide();

    $(".nav-header").click(function () {
        // Hide all .nav-item until the next .nav-header
        $(this).nextUntil(".nav-header").filter(".nav-item").toggle();
    });
});