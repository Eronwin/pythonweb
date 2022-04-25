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
                    url: "/admin/list/user",
                    data: filter,
                    dataType: "json",
                    success: function (data) {
                        //    console.log(data);
                        return data;
                    }
                })
            }
        },


        fields: [
            { title: "id", name: "id", type: "text", width: 20 },
            { title: "用户名", name: "username", type: "text", width: 50 },
            { title: "密码", name: "password", type: "text", width: 50 },
            { title: "真实姓名", name: "real_name", type: "text", width: 20 },
            { title: "工号", name: "job_no", type: "text", width: 20 },
            { title: "角色", name: "role_name", type: "text", width: 20 },
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
        "url": "user-add.html",
        "dom_id": "content",
        "func": function () {
            // alert(id);
            $("#id").val(id);
            $.ajax({

                type: "post",
                url: "/admin/get/id",
                data: { "id": id },
                dataType: "json",
                success: function (data) {
                    // console.log(data);
                    $("#username").val(data.username);

                    $("#password").val(data.password);
                    $("#real_name").val(data.real_name);
                    $("#job_no").val(data.job_no);
                    load_roles()
                    $("#role_code").val(data.role_code);

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