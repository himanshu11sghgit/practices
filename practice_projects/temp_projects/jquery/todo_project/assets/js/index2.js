$(document).ready(function () 
{
    console.log("jquery is running!!");

    // add a new task
    $("input[name=task]").on("keypress", function (event)
    {
        console.log("key is pressed!!");
        console.log(event.which);

        if (event.which === 13)
        {
            let task = $("input[name=task]").val();
            content = `<li> <span class="delete"><i class="fa-solid fa-trash-can"></i></span> ${task}</li>`;
            $("ul").append(content);
            $("input[name=task]").val("");
        }

    })


    // delete a task
    $("ul").on("click", "span", function (event)
    {
        event.stopPropagation();
        $(this).parent().fadeOut("slow", function () 
        {
            $(this).remove();
        })
    })


    // line through 
    $("ul").on("click", "li", function ()
    {
        $(this).toggleClass("done");
    })


    // hide and show add task input
    $("#plus").on("click", function ()
    {
        console.log("Plus button is clicked!!");
        $("input[name=task]").fadeToggle();
    })
})