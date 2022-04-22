$(function () {
    load_page_list()
});


var load_page_list = function () {
    $("#jsGrid1").jsGrid({
        height: 'auto',
        width: "100%",

        sorting: true,
        paging: true,
        pageLoading: true, // 分页加载
        autoload: true, // 自动加载
        pageIndex: 1,    // 初始化页码
        pageSize: 5,    // 初始化每页显示数量
        pageButtonCount: 5,    // 分页按钮数量
        pagePrevText: "上一页",    // 上一页按钮文本
        pageNextText: "下一页",    // 下一页按钮文本
        pageFirstText: "首页",    // 首页按钮文本
        pageLastText: "末页",    // 末页按钮文本
        noDataContent: "暂无数据",    // 无数据时显示内容

        controller: {//请求后台url和参数配置
            loadData: function (filter) {
                filter["search"] = $("#search").val();
                return $.ajax({
                    type: "post",
                    url: "/role/list/page",
                    data: filter,
                    dataType: "json",
                    success: function (data) {
                        // console.log(data);
                        return data;
                    }
                })
            }
        },


        fields: [
            { title: "id", name: "id", type: "text", width: 20 },
            { title: "角色编码", name: "role_code", type: "text", width: 50 },
            { title: "角色名称", name: "role_name", type: "text", width: 50 },
            {
                title: "操作", name: "id", type: "text", width: 30,
                itemTemplate: function (value, item) {
                    return "<a href='#' onclick='update(" + value + ")'>修改</a>"
                        + "&nbsp;&nbsp;&nbsp;&nbsp;<a href='#' onclick='del(" + value + ")'>删除</a>"
                }
            }
        ],

        // data: db.clients,

    });
}
var update = function (id) {

    loadHtml({
        "url": "role-add.html",
        "dom_id": "content",
        "func": function () {
            // alert(id);
            $("#id").val(id);
            $.ajax({
                type: "post",
                url: "/role/get/id",
                data: { "id": id },
                dataType: "json",
                success: function (data) {
                    $("#role_code").val(data.role.role_code)
                    $("#role_code").attr("readonly", "readonly")

                    $("#role_name").val(data.role.role_name)

                    load_menu_tree({
                        "func": function () {

                            var zTreeObj = $.fn.zTree.getZTreeObj("treeDemo")

                            var role_menus = data.role_menus
                            console.log(role_menus)
                            $.each(role_menus, function (index, role_menu) {

                                var node = zTreeObj.getNodeByParam("menu_code", role_menu.menu_code)
                                console.log(node)

                                if (node.parent_id > 0) {
                                    zTreeObj.checkNode(node, true, true)
                                }
                            })
                        }
                    })
                }
            })
        }
    })
}
var del = function (id) {

    var params = {
        "prefix": "/role/",
        "model_name": "角色",
        "id": id
    }
    del_by_json(params)
}
