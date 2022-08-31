jQuery.noConflict();
jQuery(document).ready(function($)
{
    console.log('jquery is working!!')
    
    
    $select = $("<select> </select>");
    $("#mainmenu").append($select);


    $("#mainmenu a").each(function () 
    {
        $option = $("<option> </option>");
        $option.text($(this).text());
        $option.val($(this).attr("href"));

        if ($(this).parent().hasClass("selected"))
        {
            $option.attr("selected", "selected");
        }

        $select.append($option)
    });


    $("#mainmenu select").change(function()
    {
        window.location = $(this).val();
    })
})