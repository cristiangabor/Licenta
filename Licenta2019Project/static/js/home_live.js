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
    $("#ChapterOne").click(function() {
        if ($(".ChapterTwo").is(":visible")) {
            $(".ChapterTwo").toggle("slow")
        }
        if ($(".ChapterThree").is(":visible")) {
            $(".ChapterThree").toggle("slow")
        }
        $(".ChapterOne").toggle("slow");
    });
});

$(document).ready(function() {
    $("#ChapterTwo").click(function() {
        if ($(".ChapterOne").is(":visible")) {
            $(".ChapterOne").toggle("slow")
        }
        if ($(".ChapterThree").is(":visible")) {
            $(".ChapterThree").toggle("slow")
        }
        $(".ChapterTwo").toggle("slow");

    });
});

$(document).ready(function() {
    $("#ChapterThree").click(function() {
        if ($(".ChapterOne").is(":visible")) {
            $(".ChapterOne").toggle("slow")
        }
        if ($(".ChapterTwo").is(":visible")) {
            $(".ChapterTwo").toggle("slow")
        }
        $(".ChapterThree").toggle("slow");

    });
});