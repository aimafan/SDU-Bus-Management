$(document).ready(function() {
    $('.bus-btn').click(function() {
        // var busName = $(this).closest('input').find('#bus-name').val();
        var busName = $(this).closest(".single_bus").find('.bus-name').val();
        $.ajax({
            type: 'GET',
            url: '/bus_detail',
            data: { 'bus-name': busName },
            success: function(response) {
                $('#popupContent').html(response.message);
                $('#popup').fadeIn();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('#popupClose').click(function() {
        $('#popup').fadeOut();
    });
});
