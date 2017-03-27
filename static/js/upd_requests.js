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
