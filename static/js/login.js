var login = function () {
    var username = $('#username').val();
    var password = $('#password').val();

    if (username == "") { alert("请输入用户名"); return false; }
    if (password == "") { alert("请输入密码"); return false; }


    $.ajax({
        type: "post",
        url: "/admin/login",
        data: {
            "username": username,
            "password": password
        },
        dataType: "json",
        success: function (data) {
            console.log("[success]")
            if (data.code == "200") {
                window.location.href = "/admin/index.html";
            }
            else {
                alert("用户或密码错误");
            }
        }
    })
}