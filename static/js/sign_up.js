"use strict";

//function example1() {
//    let name = prompt("Как Вас зовут?");
//    alert("Будем знакомы, " + name);
//}

$(document).ready(() => {
    example1();

    let correct1 = false;
    let correct2 = false;
    let correct3 = false;
    let correct4 = false;

    let regExp1 = /^[a-zA-Z][a-zA-Z0-9_\-]{5,15}$/;
    let regExp2 = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[_\-\$#&])[A-Za-z0-9_\-\$#&]{8,}$/;
    let regExp3 = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;

    $("#login").blur(() => {
        let loginX = $("#login").val();
        if (regExp1.test(loginX)) {
            // Checking is login available:
            $.ajax({
                url: "/accounts/ajax_reg",
                data: "login=" + loginX,
                success: function (result) {
                    if (result.message == "occupied") {
                        $("#login_mess").html("Login is not available!");
                        correct1 = false;
                    } else {
                        $("#login_mess").html("");
                        correct1 = true;
                    }
                }
            });
        } else {
            correct1 = false;
            $("#login_mess").html("Login does not match security pattern");
        }
    });

    $("#submit").click(() => {
        if (correct1 == true && correct2 == true && correct3 == true && correct4 == true) {
            $("#form1").attr("onsubmit", "return true");
        } else {
            $("#form1").attr("onsubmit", "return false");
            alert("The form contains incorrect data! \nData sending blocked!");
        }
    });
});
