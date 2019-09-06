$(document).ready(function() {
    $("#flip").click(function() {
        $("#panel").slideDown("slow");
    });
});

$(document).ready(function() {
    $("#panel").click(function() {
        $("#panel").slideUp("slow");
    });
});