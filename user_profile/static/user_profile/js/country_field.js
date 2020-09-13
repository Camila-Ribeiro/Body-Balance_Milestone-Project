let selected_country = $('#id_default_country').val();
if(!selected_country) {
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function() {
    selected_country = $(this).val();
    if(!selected_country) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});