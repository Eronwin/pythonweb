$(function(){
    keydown_keyup();
});

/*
按住飘号键说出命令
松开飘号键发送命令
*/
var keydown_keyup = function(){
    $(document).keydown(function(event){
        if(event.keyCode == 192){
            console.log("请说出命令")
            start_reco();
        }
    });

    $(document).keyup(function(event){
        if(event.keyCode == 192){
            console.log("发送录音")
            ai_reco();
        }
    });
}

var reco = null;
var audio_context = new AudioContext();//音频内容对象
navigator.getUserMedia = (navigator.getUserMedia ||
    navigator.webkitGetUserMedia ||
    navigator.mozGetUserMedia ||
    navigator.msGetUserMedia); // 兼容其他浏览器

navigator.getUserMedia({audio: true}, create_stream, function (err) {
    console.log(err)
});

function create_stream(user_media) {
    var stream_input = audio_context.createMediaStreamSource(user_media);
    reco = new Recorder(stream_input);
}


function start_reco(){
    reco.record();
}

function ai_reco(){
    reco.stop();

    reco.exportWAV(function (wav_file) {
        console.log(wav_file);
        var formdata = new FormData(); // form 表单 {key:value}
        formdata.append("audio", wav_file); // form input type="file"
        $.ajax({
            url: "/video/receive_audio",
            type: 'post',
            processData: false,
            contentType: false,
            data: formdata,
            dataType: 'json',
            success: function (data) {
                console.log(data);
                document.getElementById("player").src = "/video/get_audio/" + data.filename;
            }
        })
    });
    reco.clear();
}