function updateRequestsList() {
    var viewed = false;
    url = location.protocol + "//" + location.host + "/requests-ajax/";

    if (!document.hidden) {
        viewed = true;
    }

    $.ajax({
        url: url,
        method: 'get',
        dataType: 'json',
        data: {
            'viewed': viewed
        },
         success: function(data, status){
            $('title').html(data["unviewed"] + ' - Notes - Requests');
            $('#request-list li').each(function(i, obj){
                $(this).html(data["requests"][i]);
            });
//            var html = $(data);
//            var title = html.find("head").text();
//            $('title').html(html.find('#request-count').text() + ' - Notes - Requests');
//            $('#request-list').html(html.find('#request-list').html());
            $('#request-count').html(data["unviewed"]);
        }
    });
    viewed = false;
}


$(document).ready(function(){
    setInterval(updateRequestsList, 2000);
});
