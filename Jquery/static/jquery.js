$(document).ready(function(){
    $('#jquery').click(function(){
        var data = {
            'first_name':$('#name').val(),
            'second_name':$('#last_name').val(),
            };
            $.ajax({
                type: 'POST',
                url: '/api/retorno',
                dataType: 'json',
                contentType: 'application/json; charset=utf-8',
                data: JSON.stringify(data),
                success: function(callback) {
                    console.log(callback);
                    alert(callback.Completo)
                },
                error: function() {
                    $(this).html("error!");
                }
            });
        });
});