var video = [
            ['/video/get_audio/隐式转换之隐式函数.mp4'],
            ['/video/get_audio/隐式转换之隐式类_1.mp4']
        ];

$(function(){
    $("#videoArea").fix({
        float : 'right',   //default.left or right
        //minStatue : true,
        skin : 'green',    //default.gray or blue
        durationTime :300
    });
    jQuery("#playerlist").slide({delayTime:0});
    playvideo(0);
})

$(".bd").niceScroll({
   cursorcolor:"#888888",
   cursoropacitymax:1,
   touchbehavior:false,
   cursorwidth:"5px",
   cursorborder:"0",
   cursorborderradius:"5px"
});

function playerstop() {
    setTimeend();
}

function setTimeend() {//获取下一部视频的播放ID
    nowD++;
    if (nowD >= video.length ) {
        nowD = 0;
    }
    playvideo(nowD);
}

var nowD = 0;//目前播放的视频的编号(在数组里的编号)
var frontTime = false;//前置广告倒计时是否在运行中
var frontHtime = false;//后置广告是否在进行中



// 按集数播放视频，从0开始
function playvideo(n) {
    nowD = n;
    var flashvars = {
        f: video[n],
        c: 0,
        p: 1,
        e: 0,
        my_url: encodeURIComponent(window.location.href)
    };

    CKobject.embed('js/ckplayer/ckplayer.swf', 'a1', 'ckplayer_a1', '100%', '100%', false, flashvars, video[n]);
}