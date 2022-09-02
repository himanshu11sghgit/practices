$(document).ready(function ()
{
    let $select = $("<select> </select>");
    $("#mainmenu").append($select);

    $("#mainmenu a").each(function () 
    {
        let $option = $("<option> </option>");
        $option.text($(this).text());
        $option.val($(this).attr("href"));

        if ($(this).parent().hasClass("selected"))
        {
            $option.prop("selected", true)
        }

        $select.append($option);

    })


    $("select").change(function ()
    {
        window.location = $(this).val();
    })
})

