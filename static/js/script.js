$('#id_date_field').change(function() {
    var parking = window.location.pathname;
    console.log(parking);
    var date = $(this).val();
    $.ajax({
        type: 'GET',
        url: '/ajax/load_time/',
        data: {'date': date, 'parking': parking},
        success: function(response) {
            $('#id_time').html(response);
        }
    });
});
