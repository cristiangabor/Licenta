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

function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

$(document).ready(function() {
    $("#ChapterOneid").click(function() {
        $("#ChapterOneContent").toggle("slide", { direction: "right" }, 1000);
    });
});