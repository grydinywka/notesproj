//// using jQuery
//function getCookie(name) {
//    var cookieValue = null;
//    if (document.cookie && document.cookie !== '') {
//        var cookies = document.cookie.split(';');
//        for (var i = 0; i < cookies.length; i++) {
//            var cookie = jQuery.trim(cookies[i]);
//            // Does this cookie string begin with the name we want?
//            if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                break;
//            }
//        }
//    }
//    return cookieValue;
//}

function updateRequestsList() {
    var viewed = false;
    url = location.protocol + "//" + location.host + "/requests-ajax/";

    if (!document.hidden) {
        viewed = true;
    }

    $.ajax({
        url: url,
        method: 'get',
        dataType: 'html',
        data: {
            'viewed': viewed
        },
         success: function(data, status){
            var html = $(data);
            var title = html.find("head").text();
            $('title').html(html.find('#request-count').text() + ' - Notes - Requests');
            $('#request-list').html(html.find('#request-list').html());
            $('#request-count').html(html.find('#request-count').text());
        }
    });
    viewed = false;
}


$(document).ready(function(){
    setInterval(updateRequestsList, 1000);
});
