$(document).ready(function(){

    $(".cl_arrow_right").click(function(){
        var lst = $(".cl_content");
        lst.animate({
            left: "-=404"
        },500);
    });

    $(".cl_arrow_left").click(function(){
        var lst = $(".cl_content");
        lst.animate({
            left: "+=404"
        },500);
    });

});