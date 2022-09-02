$(document).ready(function ()
{
    console.log("jquery is running!!");
    $("span").hide();

    // password  must be more than or equal to 8 chars


    function isPasswordValid()
    {
        console.log($("input[name=password]").val());
        return $("input[name=password]").val().length >= 7;
    }

    $("input[name=password]").on("keyup", function ()
    {
        console.log(isPasswordValid());
        if (isPasswordValid())
        {
            $(this).next().hide();
        }
        else
        {
            $(this).next().show();
        }
    })

    // both passwords must match
    function isPasswordMatched()
    {
        console.log("password", $("#password").val());
        console.log("password2", $("#password2").val());
        return $("#password").val() === $("#password2").val();
    }

    $("input[type=password]").on("keyup", function ()
    {
        console.log(isPasswordMatched());
        if (isPasswordMatched())
        {
            $("#password2").next().hide();
        }
        else
        {
            $("#password2").next().show();
        }
    })


    // disable submit button if any of the condition is failed
    $("input").on("keyup", function ()
    {
        let submitButtonStatus = isPasswordValid() && isPasswordMatched();
        console.log("submit button", submitButtonStatus);
        $("#submit").prop("disabled", !submitButtonStatus);
    })

    $("form").on("submit", function (event)
    {
        event.preventDefault();
    })


})