

var load_parent_menus = function (select_obj) {
    var menu_level = $(select_obj).val();
    if (menu_level == 2) {
        $.ajax({
            type: "post",
            url: "/menu/first/all",
            data: {
            },
            async: false,
            dataType: "json",
            success: function (data) {
                var option = ' <option selected disabled>请选择一个级别</option>';
                $.each(data, function (index, value) {
                    option += '<option value="' + value.id + '">' + value.menu_name + '</option>';
                });
                // console.log(option);
                // console.log(data)
                $("#parent_id").html(option);
            }
        })
    }
    else {
        $("#parent_id").html("<option value='0'>默认父级菜单</option>");
    }
}

var submit_new_menu = function () {
    var params = {
        menu_code: $("#menu_code").val(),
        menu_name: $("#menu_name").val(),
        menu_level: $("#menu_level").val(),
        parent_id: $("#parent_id").val(),
        menu_url: $("#menu_url").val(),
        sort: $("#menu_sort").val(),
    }
    var isUpdate = $("#id").val() == "" ? false : true

    var url = "/menu/"
    var str = ""
    if (isUpdate) {
        params["id"] = $("#id").val()
        url += "update"
        str = "修改"
    } else {
        url += "add"
        str = "新增"
    }
    $.ajax({
        type: "post",
        url: url,
        data: params,
        dataType: "json",
        success: function (data) {
            var msg = str + "菜单" + (data.code == 200 ? "成功" : "失败");
            alert(msg);
        }
    })
}