// 执行加载脚本
$(function () {
    // 加载页面
    loadHtml({
        url: "header.html",
        dom_id: "header",
    });
    loadHtml({
        url: "footer.html",
        dom_id: "footer",
    });
    loadHtml({
        url: "left-menu.html",
        dom_id: "left-menu",
    });
    loadHtml({
        url: "wolcome.html",
        dom_id: "content",
    });

});