$(document).ready(function ()
{
    console.log("jquery is running!!");

    let $overlay = $("<div id='overlay'></div>");
    let $close = $("<img id='close'>");
    let $image = $("<img id='image'>");

    $("#image-gallery").append($overlay);
    $overlay.append($image);
    $overlay.append($close);

    $("#image-gallery a").on("click", function (event) 
    {
        event.preventDefault();
        console.log("image is clicked!!");

        let imageSource = $(this).attr("href");
        console.log(imageSource);
        $image.attr("src", imageSource);
        $close.attr("src", "images/9.jpg");

        $overlay.show();
    });


    $($close).on("click", function ()
    {
        $overlay.hide();
    })
});
