$(document).ready(function()
{
    $("span").hide();



    // Password is equal or greater than 8 chars start 
    function isPasswordValid()
    {
        return $("#password").val().length >= 8;
    }


    $("#password").on("keyup", function()
    {
        if (isPasswordValid())
        {
            $(this).next().hide();
        }
        else
        {
            $(this).next().show();
        }
    });

    // Password is equal or greater than 8 chars end



    // Both Passwords must match start

    function isPasswordMatch()
    {
        return $("#password").val() === $("#password2").val();
    }

    $("#password2").on("keyup", function()
    {
        if (isPasswordMatch())
        {
            $(this).next().hide();
        }
        else
        {
            $(this).next().show();
        }
    })


    // Both Passwords must match start


    // Allow submit button when data is valid and match start

    function isSubmitButtonValid()
    {
        return ($("#username").val() !== "") && isPasswordMatch() && isPasswordValid();
    }

    $("input").keyup(function()
    {
        console.log(isSubmitButtonValid());
        $("#submit").prop("disabled", !isSubmitButtonValid())
        if (!isSubmitButtonValid())
        {
            $("input[type=button]").css(
                {
                    backgroundColor: "#d3d3d3",
                    color: "#000"
                }
            )
        }
        else
        {
            $("input[type=button]").css(
                {
                    backgroundColor: "#2f558e",
                    color: "#fff"
                }
            )
        }
    })


    // Allow submit button when data is valid and match end


})