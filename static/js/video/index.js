$(function () {
    index_init()
})

var index_init = function () {
    // 加载电视剧
    create_lis(2, "vt_2")

    // 加载综艺
    // create_lis(4, "vt_4")
}

var create_lis = function (video_type_id, dom_id) {
    load_video_type_id({
        "video_type_id": video_type_id,
        "func": function (data) {
            console.log(data)
            var li_temp = '<li class="first_content bg">'
                + ' <a class="pic" target="_blank" href="$href$">'
                + '  <img src="$v_pic$"  width="100%"/>'
                + '  <span class="first_bg"><i class="icon_bf"></i></span>'
                + ' </a>'
                + ' <a target="_blank" href="$href$" class="bq" >$episodes$集</a>'
                + ' <div class="tc">'
                + '  <p class="tit">'
                + '  <a target="_blank" href="$href$">$v_name$</a></p>'
                + '  <p class="des">$synopsis$</p>'
                + ' </div>'
                + '</li>'
            $.each(data, function (index, v) {
                // 对图片路径做Unicode编码，可以正常把请求传递到后台
                // $.ajax({
                //     url: "/video/pic/" + encodeURI(v.v_pic),
                //     type: "post",
                // })
                // console.log(data)
                tmp = li_temp.replace("$v_pic$", "/video/pic/" + v.v_pic)
                // tmp = li_temp.replace("$v_pic$", "{{ url_for('static', filename='images/banaer.png') }}")
                tmp = tmp.replace("$episodes$", v.episodes)
                tmp = tmp.replace("$v_name$", v.v_name)
                tmp = tmp.replace("$synopsis$", v.synopsis)
                tmp = tmp.replaceAll("$href$", "/static/select.html?" + v.id)

                $("#" + dom_id).append($(tmp))
            })
        }
    })
}

var load_video_type_id = function (params) {
    $.ajax({

        type: "post",
        url: "/video/type/id",
        data: { "video_type_id": params.video_type_id },
        dataType: "json",
        success: function (data) {
            // console.log(data)
            params.func(data)
        }
    })
}