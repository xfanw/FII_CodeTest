"use strict;";

function add_employee() {
    $("#emp_list").append(`
        <tr>
            <td><input type='text' class='form-control' name='first_name' placeholder='First Name' autocomplete='off'></td>
            <td><input type='text' class='form-control' name='last_name' placeholder='Last Name' autocomplete='off'></td>
        </tr>
    `);
}
