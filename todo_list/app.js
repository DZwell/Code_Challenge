$(function() {

    $('#submit').click(function() {
        var value = $('#input').val();
        if(value == '') {

        }
        $('#list').prepend('<li>' + value + '</li>');
        $('#input').val('');
    });

     $('#input').keypress(function(e) {
        var key = e.which;
        if(key == 13) {
            $('#submit').click();
            return false;
        }
    });
});
