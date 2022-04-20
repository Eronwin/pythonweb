

var load_parent_menus = function (select_obj) {
    var menu_level = $(select_obj).val();
    if (menu_level == 2) {
        $.ajax({
            type: "post",
            url: "/menu/first/all",
            data: {
            },
            dataType: "json",
            success: function (data) {
                var option = ' <option selected disabled>请选择一个级别</option>';
                $.each(data, function (index, value) {
                    option += '<option value="' + value.id + '">' + value.menu_name + '</option>';
                });
                console.log(option);
                console.log(data)
                $("#parent_id").html(option);
            }
        })
    }
    else {
        $("#parent_id").html("<option value='0'>默认父级菜单</option>");
    }
}

var submit_new_menu = function () {
    params = {
        menu_code: $("#menu_code").val(),
        menu_name: $("#menu_name").val(),
        menu_level: $("#menu_level").val(),
        parent_id: $("#parent_id").val(),
        menu_url: $("#menu_url").val(),
        sort: $("#menu_sort").val(),
    }
    $.ajax({
        type: "post",
        url: "/menu/add",
        data: params,
        dataType: "json",
        success: function (data) {
            var msg = "menuadd" + (data.code == 200 ? "success" : "fail");
            alert(msg);
        }
    })
}