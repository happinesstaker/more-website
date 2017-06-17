jQuery(function() {

    //Submit the form on pressing enter (key 13), but not while holding shift
    $("body").on('keypress', 'textarea[id=id_comment]', function() {
        if ((event.which == 13) && !event.shiftKey) {
            var form = $(this).parents('form:first');
            form.submit();

            // increment counter
            var id = $(this).parents('.comments-container').attr('id').split('-')[2];
            var prevCtr = $("#comments-ctr-"+id).text().trim().split(" ")[0];
            var newCtr = '' + (parseInt(prevCtr) + 1) + ' comments';
            $("#comments-ctr-"+id).text(newCtr);

            return false;
        }
    });

    // Delete comment using Ajax call
    $("body").on('click', 'a.delete-comment', function(){
        // Prevent the default django action on button click. Otherwise it'll reload the whole page
        event.preventDefault();

        var comment_id = $(this).data('value');
        var url = $(this).data('ajax-url');

        // decrement counter
        var id = $(this).parents('.comments-container').attr('id').split('-')[2];
        var ctrDiv = $("#comments-ctr-"+id)
        var prevCtr = ctrDiv.text().trim().split(" ")[0];
        var newCtr = '' + (parseInt(prevCtr) - 1) + ' comments';

        $.ajax({
            url: url,
            type: 'POST',
            data: {comment_id: comment_id}, // Send the selected use case id

            success: function(result) {
                if (result.is_removed) {
                    var comment = $("#c" + result.comment_id);
                    comment.hide("normal",function(){
                        comment.remove();
                    })
                    ctrDiv.text(newCtr);
                } else {
                    alert("Oops! Could not delete the comment!")
                }
            },

            error: function(xhr,errmsg,err) {
                // Show error message in the alert
                alert("Oops! We have encountered and error \n" + errmsg);
            }
        });

    });
});
