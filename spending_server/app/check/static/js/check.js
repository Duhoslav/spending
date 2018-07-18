const csrftoken = $("[name=csrfmiddlewaretoken]").val();

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function () {
    $(".btn__check_left").click(function () {
        const postData = {
            "id": this.id
        };
        $.post("/api/get_check/", postData)
            .done(function (data) {
                if (data.length > 0) {
                    $('.cards__check_container').html(data);
                }
                console.log(data);
            })
            .fail(function (err) {
                console.log(err);
            });
    });

    $(".btn__check_add").click(function () {
        const postData = {
            "fn": $('.input__fn').val(),
            "fd": $('.input__fd').val(),
            "fpd": $('.input__fpd').val()
        };
        $.post("/api/add_check/", postData)
            .done(function (data) {
                if (data.length > 0) {
                    $('.cards__check_container').html(data);
                }
                console.log(data);
            })
            .fail(function (err) {
                console.log(err);
            });
    })
});