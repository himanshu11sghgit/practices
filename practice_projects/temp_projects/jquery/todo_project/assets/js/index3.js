$(document).ready(function()
{
    console.log($);

    // add task in tasks list start
    $("#task").on("keyup", function(e)
    {
        if (e.which === 13)
        {
            let task, content;
            task = $(this).val();
            content = `<li> <span class="delete"><i class="fa-solid fa-trash-can"></i></span> ${task}</li>`;

            $("ul").append(content);
            $(this).val("");
        }

    })
    // add task in tasks list end



    // fade toggle on plus button start

    $("#plus").on("click", function()
    {
        $("#task").fadeToggle("fast");
    });

    // fade toggle on plus button end



    // line through in tasks list start


    $("ul").on("click", "li", function()
    {
        $(this).toggleClass("done");
    })


    // line through in tasks list end



    // delete task from tasks list start 

    $("ul").on("click", ".delete", function(e)
    {
        $(this).parent().fadeOut("fast", function()
        {
            $(this).remove()
        });
        e.stopPropagation();
    })
    
    // delete task from tasks list end

})