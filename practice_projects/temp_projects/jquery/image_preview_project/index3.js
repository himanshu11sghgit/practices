$(document).ready(function()
{
    console.log($);

    // make frame for image preview start

    $overlay = $("<div id='overlay'> </div>");
    $image = $("<img id='image'> </img>");
    $close = $("<img id='close'> </img>");

    $overlay.append($image);
    $overlay.append($close);

    $("#image-gallery").append($overlay);

    $("#image-gallery a").on("click", function(e)
    {
        e.preventDefault();
        $image.attr("src", $(this).attr("href"));
        $close.attr("src", "images/9.jpg")
        $overlay.show();
    })

    // make frame for image preview end



    // add functionality to close button start

    $close.on("click", function()
    {
        $overlay.hide();
    })


    // add functionality to close button end


})