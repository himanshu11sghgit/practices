// slectors in jquery
// $.noConflict();
// jQuery(document).ready(function ($)
// {
//     console.log($);
//     console.log(jQuery);
    
    
//     // $("button").click(function ()
//     // {
//     //     alert("button is clicked!!");
//     // })

//     $("h2").click(function() 
//     {
//         alert("heading is clicked!!");
//     });

//     $("#btn-id").click(function() 
//     {
//         alert("button with id is clicked!!");
//     });

//     $(".btn-class").click(function() 
//     {
//         alert("button with class is clicked!!");
//     });


// });


$(document).ready(function() 
{

    // mouse events selector
    // $("#p-id").click(function() 
    // {
    //     console.log("p-id is clicked!!");
    // });

    // $("#p-id2").dblclick(function() 
    // {
    //     console.log("p-id2 is double clicked!!");
    // });

    // $("#p-id3").hover(function() 
    // {
    //     console.log("p-id3 is hovered!!");
    // });



    // keyboard events
    // $("#name-id").keypress(function() 
    // {
    //     console.log("key is pressed!!");
    // })


    // form events
    // $("#name-id").focus(function() 
    // {
    //     console.log("name-id is focussed!!");
    // });

    // $("#name-id").blur(function() 
    // {
    //     console.log("name-id is blurred!!");
    // });

    // $("#form-id").submit(function(e) 
    // {
    //     e.preventDefault();
    //     console.log("form-id is submitted!!");
    // });


    // window events
    // $(window).resize(function() 
    // {
    //     console.log("Window resized!!");
    // })


    // hide/show/toggle 
    // $("#btn-hide").click(function() 
    // {
    //     $("#image-id").hide(1000, function() {
    //         console.log("India gate image is hidden!!");
    //     })
    // });

    // $("#btn-show").click(function() 
    // {
    //     $("#image-id").show(1000, function() {
    //         console.log("India gate image is shown!!");
    //     })
    // });

    // $("#btn-toggle").click(function() 
    // {
    //     $("#image-id").toggle(1000, function() {
    //         console.log("India gate image is toggled!!");
    //     })
    // });


    // animation
    // $("#btn-animate").click(function() 
    // {
    //     $("#taj-mahal").animate({left: "+=100px"}, 1000, function() 
    //     {
    //         console.log("Taj Mahal is animated!!");
    //     });
    // });


    // // Get text
    // $("#btn-get").click(function() 
    // {
    //     let text = $("h2").text();
    //     console.log(text);
    // });


    // // Set text
    // $("#btn-set").click(function() 
    // {
    //     $("h2").text("This is <b> your </b> text");
    //     console.log("text is changed!!");
    // });

    // // Get html
    // $("#btn-get").click(function() 
    // {
    //     let text = $("h2").html();
    //     console.log(text);
    // });


    // // Set htl
    // $("#btn-set").click(function() 
    // {
    //     $("h2").html("This is your text");
    //     console.log("text is changed!!");
    // });


    // // Get value in form field
    // $("#btn-get").click(function() 
    // {
    //     let value = $("#name-id").val();
    //     console.log(value);
    // });

    // // Set value in form field
    // $("#btn-set").click(function() 
    // {
    //     let value = "new name"
    //     $("#name-id").val(value);
    //     console.log(value);
    // });


    // // get attribute of css link
    // $("#btn-get").click(function() 
    // {
    //     let value = $("link").attr("href");
    //     console.log(value);
    // })


    // // get data-value attribute of input
    // $("#btn-get").click(function() 
    // {
    //     let value = $("#name-id").attr("data-value");
    //     console.log(value);
    // })


    // // set data-value attribute of input
    // $("#btn-set").click(function() 
    // {
    //     let value = "20 out of 10";
    //     $("#name-id").attr("data-value", value);
    //     console.log(value);
    // });


    // // change image on button click
    // $("#btn-change").click(function() 
    // {
    //     let newImagePath = "images/india_gate.jpg";
    //     $("#img-frame").attr("src", newImagePath);
    //     console.log("image path is changed!!");
    // })


    // // add/remove/toggle css class in element
    // $("#btn-add-class").click(function() 
    // {
    //     $("#p-id").addClass("color-blue");
    // });

    // $("#btn-remove-class").click(function() 
    // {
    //     $("#p-id").removeClass("color-blue");
    // });

    // $("#btn-toggle-class").click(function() 
    // {
    //     $("#p-id").toggleClass("color-blue");
    // });

    
    // get/set css properties value
    $("#btn-get-css").click(function() 
    {
        let value = $("#p-id").css("color");
        console.log(value);
    });

    $("#btn-set-css").click(function() 
    {
        // let value = "2px solid black";
        // $("#p-id").css("border", value)
        // console.log("css color is changed to 'green'");


        $("#p-id").css({"background-color": "red", "font-size": "100px", "font-style": "bold italic"})
    })

});


