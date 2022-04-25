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
			console.log(obj);
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


var submit_add_update = function (submit_form_params) {
	// isUpdate，如果是新增页面false，修改页true
	var isUpdate = $("#id").val() == "" ? false : true

	var url = submit_form_params.prefix
	var str = ""
	if (isUpdate) {
		submit_form_params.params["id"] = $("#id").val()
		url += "update"
		str = "修改"
	} else {
		url += "add"
		str = "新增"
	}

	str += submit_form_params.model_name
	// 如果新增页，url="/menu/add"，str = "新增"
	// 如果修改页，url="/menu/update"，str = "修改"，params多一个参数
	console.log(submit_form_params.params);
	console.log(url);
	$.ajax({
		type: "post",
		url: url,
		data: submit_form_params.params,
		dataType: "json",
		success: function (data) {
			var msg = str + (data.code == "200" ? "成功" : "失败") + "!"
			alert(msg)
		}
	})
}



/*
公共加载下拉列表组件
{
	"tab_name": "language", // 查询的表名
	"value": "id", // 想要填到option的value的数据的对应的字段名
	"text": "language", // 想要填到option的text的数据的对应的字段名
	"dom_id": "language_id" // 组装下拉列表的下拉列表id
}
*/
var create_select = function (params) {
	$.ajax({
		type: "post",
		url: "/admin/load/select",
		data: { "tab_name": params.tab_name },
		dataType: "json",
		success: function (data) {
			var option = "<option value=''>--请选择--</option>"
			$.each(data, function (index, obj) {
				option += "<option value='" + obj[params.value] + "'>" + obj[params.text] + "</option>"
			})
			$("#" + params.dom_id).html(option)
		}
	})
}