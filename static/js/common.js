/**
 * 读取分页面的HTML，加载到index.html的.content-wrapper中
 * ajax异步刷新
 * {
 * url: 'xxx.html',
 * "dom_id":'*****,
 * "func":function(){}
 * }
 */
var loadHtml = function (obj) {
	$.ajax({
		type: "get",
		url: "/static/pages/" + obj.url,
		async: true,
		success: function (data) {
			// console.log(id);
			$("#" + obj.dom_id).html(data);
			obj.func
		}
	});
}

