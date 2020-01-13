function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function cloneMore(prefix) {
    var selector = '.' + prefix + '-empty';
    var selector_name = prefix + '-empty';
    var newElement = $(selector).clone(true);
    newElement.removeClass('d-none');
    newElement.removeClass(selector_name);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
        var name = $(this).attr('name').replace('-' + '__prefix__' + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var forValue = $(this).attr('for');
        if (forValue) {
          forValue = forValue.replace('-' + '__prefix__' + '-', '-' + total + '-');
          $(this).attr({'for': forValue});
        }
    });
    newElement.find('.form-group:last').remove();
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    var putIn = '.' + prefix + '-row:last';
    $(putIn).after(newElement);
    return false;
}

function deleteForm(prefix, btn) {
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        var elemName = '.' + prefix + '-row';
        btn.closest(elemName).remove();
        var forms = $(elemName);
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}

$(document).on('click', '.add-row', function(e){
    e.preventDefault();
    var prefix = $(this).data('prefix');
    cloneMore(prefix);
    return false;
});

$(document).on('click', '.delete-row', function(e){
    e.preventDefault();
    var prefix = $(this).data('prefix');
    deleteForm(prefix, $(this));
    return false;
});