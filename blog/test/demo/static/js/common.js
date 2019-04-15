function createXhr(){
    var xhr = null;
    // 判断是否支持 XMLHttpRequest
    if(window.XMLHttpRequest){
        var xhr = new XMLHttpRequest();
    } else {
        var xhr = new ActiveXObject("Microsoft.XMLHttp");
    }
    return xhr;
}