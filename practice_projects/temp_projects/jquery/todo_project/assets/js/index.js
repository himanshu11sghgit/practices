$(document).ready(function()
{
    console.log("jquery is running!!");

    // line through functionality
    $("ul").on("click", "li", function ()
    {
        console.log("task is clicked!!");
        $(this).toggleClass("done");
    })

    // delete functionality
    $("ul").on("click", "span", function (event)
    {
        console.log("delete button is clicked!!");
        $(this).parent().fadeOut("slow", function() 
        {
            $(this).remove();
            
        });
        event.stopPropagation();
    })


    // add task functionality
    $("input[name=task]").on("keypress", function (event) 
    {
        console.log("key is pressed!!");
        if (event.which === 13) 
        {
            var task = $("input[name=task]").val();
            var content = `<li> <span class="delete"><i class="fa-solid fa-trash-can"></i></span> ${task}</li>`
            $("ul").append(content);
            $("input[name=task]").val("");
        }
    })


    // scroll toggle on add task view
    $("#plus").on("click", function () 
    {
        $("input[name=task]").fadeToggle("fast");
    })
})