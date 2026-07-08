"use strict;";

function delete_curr_row(emp_id, first_name, last_name) {
    Swal.fire({
        title: `You will delete <br>ID ${emp_id}, ${first_name} ${last_name}.`,
        html: "Hint: Find this function and remove the current prompt.<br>Use AJAX to call the backend /question3/delete_emp using the GET method, passing emp_id as the request parameter.",
    });
}
