"use strict;";

function delete_curr_row(emp_id, first_name, last_name) {
    Swal.fire({
        text: `You will delete ID ${emp_id}, ${first_name} ${last_name}.`,
    });
}
