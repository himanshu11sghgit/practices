jQuery.noConflict();

jQuery(document).ready(function ($)
{
    console.log("jquery is running!!");


    function isPasswordValid()
    {
        return $("#password").val().length >= 8;
    }

    function errorMessageEvent()
    {
        if (isPasswordValid())
        {
            $(this).next().hide();
        }
        else
        {
            $(this).next().show();
        }
    }

    function isPasswordMatched()
    {
        return ($("#password").val() === $("#password2").val());
    }

    function errorMatchingEvent()
    {
        if (isPasswordMatched())
        {
            $(this).next().hide();
        }
        else 
        {
            $(this).next().show();
        }
    }

    function submitButtonValid() {
        return isPasswordValid() && isPasswordMatched()
    }

    function enableSubmitButton()
    {
        $("input[type=submit]").prop("disabled", !submitButtonValid())
        if (!submitButtonValid())
        {
            $("input[type=submit]").css(
                {
                    backgroundColor: "#d3d3d3",
                    color: "#000"
                }
            )
        }
        else 
        {
            $("input[type=submit]").css(
                {
                    backgroundColor: "#2f558e",
                    color: "#fff"
                }
            )
        }
    }


    $("form span").hide();

    $("input[name=password]").keyup(errorMessageEvent).keyup(enableSubmitButton);
    $("input[name=password2").keyup(errorMatchingEvent).keyup(enableSubmitButton);

})
