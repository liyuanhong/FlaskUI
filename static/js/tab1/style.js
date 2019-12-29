/**
*tab1基本控件顶部tab且换
*/
function styleManTab(e){
    var url = window.location.href;
    var id = $(e).attr("id");
    if(id == "style_buttons"){
        $(location).attr('href', "http://" + window.location.host + "/tab1/style");
    }else if(id == "style_labels"){
        $(location).attr('href', "http://" + window.location.host + "/tab1/style/labels");
    }else if(id == "style_tables"){
        $(location).attr('href', "http://" + window.location.host + "/tab1/style/tables");
    }else{
        alert(id)
    }
}
