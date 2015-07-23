$(function() {

    $('#submit').click(function() {
        var value = $('#input').val();
        if(value == '') {
           var text = $('#alert').text('List cannot be left blank!');
           text.fadeIn();
           text.fadeOut(2000);
        }
        else {
            $('#list').prepend('<li>' + value + '</li>');
            $('#input').val('');
        }
    });

    $('#input').keypress(function(e) {
        var key = e.which;
        if(key == 13) {
            $('#submit').click();
            return false;
        }
    });

    $('li').on('click', function() {
        $('li').remove();
    });
});
