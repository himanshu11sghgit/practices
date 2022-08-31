jQuery.noConflict();
jQuery(document).ready(function ($) 
{
    console.log("jquery is running!!");


    var $overlay = $("<div id='overlay'> </div>");
    var $close = $("<img id='close'>");
    var $image = $("<img id='image' >");


    $('#image-gallery').append($overlay);
    $overlay.append($image);
    $overlay.append($close);


    $("#image-gallery a").on("click", function (event) 
    {
        event.preventDefault();

        let imageSource = $(this).attr("href")
        $image.attr("src", imageSource);
        $close.attr("src", "images/9.jpg");

        $overlay.show();
    })

    $close.on("click", function () 
    {
        $overlay.hide();
    })
})