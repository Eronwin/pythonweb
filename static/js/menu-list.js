$(function () {
    load_page_list()
});


var load_page_list = function () {
    $("#jsGrid1").jsGrid({
        height: "100%",
        width: "100%",

        sorting: true,
        paging: true,
        pageLoding: true, // 分页加载
        autoload: true, // 自动加载
        controller: {//请求后台url和参数配置
            loadData: function (filter) {
                return $.ajax({
                    type: "post",
                    url: "/menu/list/page",
                    data: filter,
                    dataType: "json",
                    success: function (data) {
                        return data;
                    }
                })
            }
        },
        pageIndex: 1,    // 初始化页码
        pageSize: 10,    // 初始化每页显示数量
        pageButtonCount: 5,    // 分页按钮数量
        pagePrevText: "上一页",    // 上一页按钮文本
        pageNextText: "下一页",    // 下一页按钮文本
        pageFirstText: "首页",    // 首页按钮文本
        pageLastText: "末页",    // 末页按钮文本
        noDataContent: "暂无数据",    // 无数据时显示内容
        fields: [
            { title: "id", name: "id", type: "text", width: 20 },
            { title: "菜单编码", name: "menu_code", type: "text", width: 50 },
            { title: "菜单名称", name: "menu_name", type: "text", width: 20 },
            { title: "菜单级别", name: "menu_level", type: "text", width: 20 },
            { title: "父级菜单", name: "parent_id", type: "text", width: 20 },
            { title: "菜单链接", name: "menu_url", type: "text", width: 150 },
            { title: "菜单排序", name: "menu_sort", type: "text", width: 20 },
        ],

        // data: db.clients,

    });
}