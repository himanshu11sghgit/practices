// jquery starts

$(document).ready(function()
{
    console.log("jquery is running");

    $("#submit").on("click", function()
    {
        let tick, countries, desc, gender;
        tick = $("#tick").prop("checked");
        countries = $("#countries").val();
        desc = $("#desc").val();
        gender = $('input:radio[name=gender]:checked').val();
    
        console.log("*******")
        console.log(tick);
        console.log(countries);
        console.log(desc);
        console.log(gender);
    })

})

// jquery ends



// angular starts





// angular ends
