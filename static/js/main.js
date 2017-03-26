//main js file

function initAddNoteForm2(form, modal, link){
    form.find('input[name="cancel_button"]').click(function(event) {
        event.preventDefault();
        modal.modal('hide');
        $('.messages').html('<div class="alert alert-warning">Note is not create</div>');
    });

    form.find('input[name="add_button"]').click(function(event) {
        var text = form.find("#id_text").val();
        event.preventDefault();
        $.ajax({
            'type': 'POST',
            'url': link.attr('href'),
//            'url': "https://notes-proj.herokuapp.com/note/add-upper/",
            'dataType': 'json',
            'data': {
//                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'text': form.find("#id_text").val()
            },
            'beforeSend': function(xhr,setting){},
            'error': function(xhr, status, error){
                alert("error");
                return false;
            },
            'success': function(data, status, xhr) {
                if ( data['status'] == 'created' ) {
                    modal.modal('hide');
                    $('.messages').html('<div class="alert alert-warning">Note is create</div>');
                    $('#note-list').append('<li>' + text.toUpperCase() + '</li>');
                    $('#note_count').text('Amount of notes is ' + data['new_count']);
                } else {
//                    alert(data['status']);
                    $('tr.required').addClass("text-danger has-error");
                    $('#id_text').parent().find('ul').hide();
                    $('#id_text').parent().prepend('<ul><li>' + data['errors']['text'] + '</li></ul>');
                }
            }
        });
    });

}

function initAddNotePage2() {
	$('a.add_note2').click(function(event){
	    var link = $(this);
//	    var link = 'https://notes-proj.herokuapp.com/note/add-upper/';

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

				initAddNoteForm2(form, modal, link);
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
    initAddNotePage2();
});
