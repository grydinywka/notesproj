function get_note(){
    $.get("https://notes-proj.herokuapp.com/note/random/", function(data, status){
//    $.get("note/random/", function(data, status){
        var note = "<div id=\"note_random\">"
            + "<span>Random note object is:</span>"
            + "<p>" + data['note'] + "</p>"
            + "</div>"

        $('#rand-script').after( note ).css( "color", "green" );
        $('#note_random').css({
            "text-align": "center",
            "margin": "40px",
            "font-size": "30px"
        });
         $('#note_random p').css({
            "background-color": "#ffe"
         });
    });
}


$(document).ready(function(){
    get_note();
});