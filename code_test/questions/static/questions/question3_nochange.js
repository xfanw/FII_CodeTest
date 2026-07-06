"use strict;";
// You can copy any useful code from this file, but do not modify this file.
function reset_employee_data() {
    $.ajax({
        url: "/reset_employee",
        type: "GET",
        dataType: "json",
        data: {
            field1: "val1",
            field2: "val2",
        },

        success: function (response) {
            if (response.status === "success") {
                location.reload();
            } else {
                show_json_message(response.status, response.msg);
            }
        },
        error: function () {
            show_json_message("error", "Connection Error.");
        },
    }); // end ajax
}
