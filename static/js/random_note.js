function get_note(){

    $.get("note/random/", function(data, status){
        var html = $(data);
        var note = html.find('#note_random').parent().html();

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
    var action = true;

    if ( action == true ) {
        get_note();
        action = false;
    }
//    document.write("My custom");
});
//document.write("My custom");