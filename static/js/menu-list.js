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
                    url: "/menu/list/page",
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
            { title: "菜单编码", name: "menu_code", type: "text", width: 50 },
            { title: "菜单名称", name: "menu_name", type: "text", width: 20 },
            { title: "菜单级别", name: "menu_level", type: "text", width: 20 },
            { title: "父级菜单", name: "parent_menu_name", type: "text", width: 20 },
            { title: "菜单链接", name: "menu_url", type: "text", width: 100 },
            { title: "菜单排序", name: "sort", type: "text", width: 20 },
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
        "url": "menu-add.html",
        "dom_id": "content",
        "func": function () {
            // alert(id);
            $("#id").val(id);
            $.ajax({

                type: "post",
                url: "/menu/get/id",
                data: { "id": id },
                dataType: "json",
                success: function (data) {
                    // console.log(data);
                    $("#menu_code").val(data.menu_code)
                    $("#menu_code").attr("readonly", "readonly")

                    $("#menu_name").val(data.menu_name)
                    $("#menu_url").val(data.menu_url)
                    $("#menu_level").val(data.menu_level)

                    $("#menu_sort").val(data.sort)

                    load_parent_menus($("#menu_level"))
                    $("#parent_id").val(data.parent_id)

                }
            })
        }
    })
}
var del = function (id) {

    del_by_json({
        "prefix": "/menu/",
        "model_name": "菜单",
        "id": id
    })
}