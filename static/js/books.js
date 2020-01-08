$(function () {
    $("body").on("click", ".js-create", function() {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $(".modal .modal-content").html('');
                $(".modal").modal("show");
            },
            success: function (data) {
                $(".modal .modal-content").html(data.html_form);
            }
        });
    });

    $(".modal").on("submit", ".js-modal-form", function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if(data.form_is_valid) {
                    $(".objects_list").html(data.html_list);
                    $(".modal").modal("hide");
                } else {
                    $(".modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });
});