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
			if (obj.func) {
				obj.func();
			}
		}
	});
}


var create_params = function (params_ids) {
	var params = {};
	$.each(params_ids, function (index, param_id) {
		params[param_id] = $("#" + param_id).val();
	})
	return params
}


var del_by_json = function (params) {
	$.ajax({
		type: "post",
		url: params.prefix + "del/id",
		data: { "id": params.id },
		dataType: "json",
		success: function (data) {
			var msg = "删除" + params.model_name + (data.code == "200" ? "成功" : "失败");
			alert(msg);
		}
	})
}