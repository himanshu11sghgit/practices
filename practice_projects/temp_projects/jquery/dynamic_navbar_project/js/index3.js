$(document).ready(function()
{
    console.log($);

    $select = $("<select></select>");
    $("#mainmenu").append($select);

    $("#mainmenu a").each(function()
    {
        $option = $("<option></option>")
        $option.val($(this).attr("href"));
        $option.text($(this).text());

        if ($(this).parent().hasClass("selected"))
        {
            $option.prop("selected", true);
        }
        $select.append($option);
    })

    $("#mainmenu select").change(function()
    {
        window.location = $(this).val();
    })
})