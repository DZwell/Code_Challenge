$(function(){
    $('#submit').bind('click', function() {
        var value = $('#input').val();
        $('#list').append('<ul>' + value + '</ul>')
    })




})
