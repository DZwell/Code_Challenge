$(function() {

    $('#submit').click(function() {
        var value = $('#input').val();
        if(value == '') {
           var text = $('#alert').text('List cannot be left blank!');
           text.fadeIn();
           text.fadeOut(2500);
        }
        else {
            $('#list').prepend('<li>' + value + '</li>');
            $('#input').val('');
            $removeItem();
        }
    });

    $('#input').keypress(function(e) {
        var key = e.which;
        if(key == 13) {
            $('#submit').click();
            return false;
        }
    });

    function $removeItem() {
        $('li').click(function(e) {
            $(this).remove();
        });
    }
});
