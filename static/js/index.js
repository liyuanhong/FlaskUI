/**
*页面顶部的tab切换
*/
function  swichTap(e){
    var id = $(e).attr("id")
    if(id == "tab1"){
        $(location).attr('href', "http://" + window.location.host + "/tab1/style");
    }else if(id == "tab2"){
        $(location).attr('href', "http://" + window.location.host + "/tab2/login");
    }else if(id == "otherTab"){
        $(location).attr('href', "http://" + window.location.host + "/other");
    }
}
