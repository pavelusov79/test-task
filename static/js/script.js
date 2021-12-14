$('#id_date_field').change(function() {
    var parking = $('h1').text();
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
