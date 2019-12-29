/**
*tab1基本控件顶部tab且换
*/
function iconManTab(e){
    var url = window.location.href;
    var id = $(e).attr("id");
    if(id == "style_index"){
        $(location).attr('href', "http://" + window.location.host + "/tab1/icon");
    }else{
        alert(id)
    }
}
