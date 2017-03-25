//main js file
function initAddNoteForm(form, modal, link){
    form.find('input[name="cancel_button"]').click(function(event) {
        event.preventDefault();
        modal.modal('hide');
        $('.messages').html('<div class="alert alert-warning">Note is not create</div>');
    });

    form.find('input[name="add_button"]').click(function(event) {
        event.preventDefault();
        $.ajax({
            'type': 'POST',
            'url': link.attr('href'),
            'dataType': 'html',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'text': form.find("#id_text").val()
            },
            'beforeSend': function(xhr,setting){},
            'error': function(xhr, status, error){
                alert("error");
                return false;
            },
            'success': function(data, status, xhr) {
                var html = $(data),
                    new_form = html.find('form');

                if (new_form.length > 0) {
                    modal.find('.modal-body').html(new_form);

                    //initialize form fields and buttons
                    initAddNoteForm(new_form, modal, link);
                } else {
                    var msg = html.find('.messages').html(),
                        note_list = html.find('#note-list').html(),
                        note_count = html.find('#note_count').html();

                    $(".messages").html(msg);
                    $('#note-list').html(note_list);
                    $('#note_count').html(note_count);
                    modal.modal('hide');
                }
            }
        });
    });

}

function initAddNotePage() {
	$('a.add_note').click(function(event){
	    var link = $(this);
	    event.preventDefault();
	    $.ajax({
	        'url': link.attr('href'),
	        'dataType': 'html',
			'type': 'get',
			'beforeSend': function(xhr,setting){
//			    alert("before sent");
			},
			'success': function(data, status, xhr){
			    var modal = $('#myModal'),
					html = $(data),
					form = html.find('form');

                modal.find('.modal-title').html(html.find('#title h2'));
				modal.find('.modal-body').html(form);
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});

				initAddNoteForm(form, modal, link);
			},
			'error': function(){
			    alert('error');
			    return false;
			}
	    });
        return false;
	});
}

$(document).ready(function(){
    initAddNotePage();
});
