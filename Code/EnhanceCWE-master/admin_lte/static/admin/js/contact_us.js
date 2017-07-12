function get_ContactUs_info(){
	var user_name = $("#contact-us-username").val();
	var user_email = $("#contact-us-email").val();
	var subject = $('#contact-us-subject').val();
	var content = $('#contact-us-text').val();

	var url = $("#send-email-btn").data('ajax-url');

	$.ajax({
        url: url,
        type: 'POST',
        data: {user_name: user_name, user_email: user_email, subject: subject,
        content: content}, // Send the selected use case id

        success: function(result) {
           $('#contact-us-Modal').modal('hide');
        },

        error: function(xhr,errmsg,err) {
            // Show error message in the alert
            alert("Oops! We have encountered and error \n" + errmsg);
        }
    });

}