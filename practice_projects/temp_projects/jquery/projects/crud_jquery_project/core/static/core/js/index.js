$(document).ready(function() 
{
    // save student data
    $("#btn-save").on("click", function() 
    {   
        let id, name, email, password, csrf;
        id = $("#id-id").val();
        name = $("#name-id").val();
        email = $("#email-id").val();
        password = $("#password-id").val();
        csrf = $("input[name=csrfmiddlewaretoken]").val();

        if (name === "") 
        {
            console.log("Student must have name!!");
        }
        else if (email === "") 
        {
            console.log("Student must have email!!");
        }
        else if (password === "") 
        {
            console.log("Student must have password!!");
        }
        else 
        {
            data = {
                id: id,
                name: name,
                email: email,
                password: password,
                csrfmiddlewaretoken: csrf
            }
            $.ajax({
                url: "/save/",
                method: "POST",
                data: data,
                success: function(data)
                {
                    if (data.status === 200)
                    {
                        $("form")[0].reset();
                        let students, content;
                        students = data.students;
                        content = '';
                        for (let i=0; i<students.length; i++)
                        {
                            content += `
                                <tr>
                                    <td>${students[i].id}</td>
                                    <td>${students[i].name}</td>
                                    <td>${students[i].email}</td>
                                    <td>${students[i].password}</td>
                                    <td id="col-action">
                                        <button class="btn btn-sm btn-warning" id="btn-update" data-sid=${students[i].id}>Update</button>
                                        <button class="btn btn-sm btn-danger" id="btn-delete" data-sid=${students[i].id}>Delete</button>
                                    </td>
                                </tr>
                            `
                        }
                        $("tbody").html(content);
                        $("#id-id").val("");
                        $("form")[0].reset();
                    }
                    else if (data.status === 400)
                    {
                        console.log("data is failed to save!!");
                        $("tbody").html(content);
                        $("#id-id").val("");
                        $("form")[0].reset();
                    }
                },
                error: function()
                {
                    console.log("error!!");
                }
            })
        }
    });


    // delete student data
    $("tbody").on("click", ".btn-delete", function()
    {   
        let id, csrf, thisElement;
        id = $(this).attr("data-sid");
        csrf = $("input[name=csrfmiddlewaretoken]").val();
        thisElement = this;

        data = {
            id: id,
            csrfmiddlewaretoken: csrf
        }

        $.ajax({
            url: "/delete/",
            method: "POST",
            data: data,
            success: function(data) 
            {
                if (data.status === 200)
                {
                    console.log("data is deleted!!");
                    $(thisElement).closest("tr").fadeOut();
                }
                else if (data.status === 400)
                {
                    console.log("data is failed to delete!!");
                }
            },
            error: function()
            {
                console.log("error!!");
            }
        })
    });


    // update student data
    $("tbody").on("click", ".btn-update", function() 
    {
        let id, csrf, thisElement;
        id = $(this).attr("data-sid");
        csrf = $("input[name=csrfmiddlewaretoken]").val();
        thisElement = this;

        data = {
            id: id,
            csrfmiddlewaretoken: csrf
        }

        $.ajax({
            url: "/update/",
            method: "POST",
            data: data,
            success: function(data) 
            {
                if (data.status === 200)
                {
                    console.log("Update button is clicked");
                    // $("#id-id").val(data.student.id);
                    // $("#name-id").val(data.student.name);
                    // $("#email-id").val(data.student.email);
                    // $("#password-id").val(data.student.password);
                    $("input[name=id]").val(data.student.id);
                    $("input[name=name]").val(data.student.name);
                    $("input[name=email]").val(data.student.email);
                    $("input[name=password]").val(data.student.password);

                }
                else if (data.status === 400)
                {
                    console.log("failed!!");
                }
            },
            error: function() 
            {
                console.log("error!!");
            }
        })
            
        
    }) 
})