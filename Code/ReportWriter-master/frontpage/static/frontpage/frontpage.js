var offset = window.pageYOffset;
setTimeout(function(){
   offset = window.pageYOffset;
}, 3000);

jQuery(function() {

    if ($('#search-reports-input').val()) {
        $('#marquee').slideUp();
        search_reports();
    }

    $('#search-reports-form').on('submit', function(event){
        // Prevent the default django action on button click. Otherwise it'll reload the whole page
        event.preventDefault();
        search_reports();
    });


    $("#muo-modal").on("show.bs.modal", function (e) {
        var usecase_id = $(e.relatedTarget).data('usecase-id');
        var url = $(e.relatedTarget).data('ajax-url');

        // Load the report issue dialog
        $.ajax({
            url: url,
            type: 'POST',
            data: {usecase_id: usecase_id}, // Send the selected use case id

            success: function(result) {
                $(e.currentTarget).html(result);
            },

            error: function(xhr,errmsg,err) {
                // Show error message in the alert
                alert("Oops! We have encountered and error \n" + errmsg);
            }
        });
    });

});

var page;
function search_reports(){
    $('#marquee').slideUp();
    $('.search-reports-container').show();
    page = 1;

    $.ajax({
        url: $('#search-reports-form').data('ajax-url'),
        type: 'POST',
        dataType: 'json',
        data: {term: $('#search-reports-input').val(), page: 1}, // Send the search term

        success: function(result) {
            $('.search-reports-result').html(result.html);
        },

        error: function(xhr,errmsg,err) {
            // Show error message in the alert
            alert("Oops! We have encountered and error \n" + errmsg);
        }
    });
    // $(".search-reports-result").bind('scroll', function() {
    //    console.log('Event worked');
    // });

    var win_lastScrollTop = 0;
    $('.search-reports-result').bind('scroll', function() {
        var st = $(this).scrollTop();
        if( st>$('.search-reports-result').height()-150)
        {
            page += 1;
            $.ajax({
                url: $('#search-reports-form').data('ajax-url'),
                type: 'POST',
                dataType: 'json',
                data: {term: $('#search-reports-input').val(), page: page}, // Send the search term

                success: function(result) {
                    if (!result.hasnext) {
                        $('.search-reports-result').unbind();
                    }
                    $('.search-reports-result').append(result.html);
                },

                error: function(xhr,errmsg,err) {
                    // Show error message in the alert
                    alert("Oops! We have encountered and error \n" + errmsg);
                }
            });
        }
    //     else if(st<20){
    //         page -= 1;
    //         if(page<1)
    //         {
    //             page = 1;
    //         }
    //         $.ajax({
    //             url: $('#search-reports-form').data('ajax-url'),
    //             type: 'POST',
    //             data: {term: $('#search-reports-input').val(), page: page}, // Send the search term

    //             success: function(result) {

    //                 $('.search-reports-result').html(result);
    //             },

    //             error: function(xhr,errmsg,err) {
    //                 // Show error message in the alert
    //                 alert("Oops! We have encountered and error \n" + errmsg);
    //             }
    //         });
    //     }

    // });

    // $(window).bind('scroll', function() {
    //     var win_st = $(this).scrollTop();
    //     if(win_st < win_lastScrollTop)
    //     {
    //         page -= 1;
    //         if(page<1)
    //         {
    //             page = 1;
    //         }
    //         $.ajax({
    //             url: $('#search-reports-form').data('ajax-url'),
    //             type: 'POST',
    //             data: {term: $('#search-reports-input').val(), page: page}, // Send the search term

    //             success: function(result) {
    //                 $('.search-reports-result').html(result);
    //             },

    //             error: function(xhr,errmsg,err) {
    //                 // Show error message in the alert
    //                 alert("Oops! We have encountered and error \n" + errmsg);
    //             }
    //         });
    //     }
    //     win_lastScrollTop = win_st;

    });

}
