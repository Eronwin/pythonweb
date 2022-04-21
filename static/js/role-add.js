$(function () {
    if ($('#id').val() == "") {
        load_menu_tree()
    }
})

var load_menu_tree = function (obj) {
    var setting = {
        check: {
            enable: true
        },
        data: {
            key: {
                name: "menu_name"
            },
            simpleData: {
                enable: true,
                idKey: "id",
                pIdKey: "parent_id",
                rootPId: "0",

            }
        }
    };
    $.ajax({
        // async: true,
        type: "post",
        url: "/menu/all",
        data: {},
        dataType: "json",
        success: function (data) {
            console.log(1)

            $.fn.zTree.init($("#treeDemo"), setting, data);
            console.log(2)
            if (obj && obj.func) {
                if ($.isFunction(obj.func)) {
                    obj.func()
                }
            }
            console.log(3)
        }
    })
}

var submit_new_role = function () {
    var params_ids = ["role_code", "role_name"];
    var params = create_params(params_ids);

    var isUpdate = $("#id").val() == "" ? false : true

    params["codes"] = get_znodes_checked();


    var url = "/role/"
    var str = ""
    if (isUpdate) {
        params["id"] = $("#id").val()
        url += "update"
        str = "修改"
    } else {
        url += "add"
        str = "新增"
    }
    str += "角色"
    $.ajax({
        type: "post",
        url: url,
        data: params,
        dataType: "json",
        success: function (data) {
            var msg = str + (data.code == 200 ? "成功" : "失败");
            alert(msg);
        }
    })
}

var get_znodes_checked = function () {

    var zTreeObj = $.fn.zTree.getZTreeObj("treeDemo");

    var nodes = zTreeObj.getCheckedNodes(true);

    var codes = "";

    $.each(nodes, function (index, node) {
        codes += "," + node.menu_code;
    })

    codes = codes.substring(1, codes.length);

    return codes;

}