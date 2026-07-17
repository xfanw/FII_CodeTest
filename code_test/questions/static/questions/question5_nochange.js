"use strict;";

function add_employee() {
    Swal.fire({
        title: `Add Employee`,
        html: `
            <div class='input-group'>
                <div class='input-group-text'>First Name: </div>
                <input type="text" id="first_name" class="form-control" placeholder="First Name">
            </div>

            <div class='input-group mt-3'>
                <div class='input-group-text'>Last Name: </div>
                <input type="text" id="last_name" class="form-control" placeholder="Last Name">
            </div>
        `,
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: `Add Employee`,
    }).then(function (result) {
        if (result.isConfirmed) {
            $.ajax({
                url: "/question5/add_employee",
                type: "GET",
                data: {
                    first_name: $("#first_name").val(),
                    last_name: $("#last_name").val(),
                },
                success: function (response) {
                    show_json_message(response.status, response.msg);
                    if (response.status === "success") {
                        setTimeout(function () {
                            location.reload();
                        }, 2000);
                    }
                },
                error: function () {
                    show_json_message("error", "Connection Error.");
                },
            }); // end ajax
        }
    }); // end Swal
}
