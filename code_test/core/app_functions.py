from django.http import JsonResponse


def json_msg(status, msg, **kwargs):
    """Json Message

    Args:
        status: 'error' or 'success
        msg: message

    Returns:
        JsonResponse:  'status': status + msg
    """
    return JsonResponse({"status": status, "msg": msg})


def json_error(msg, **kwargs):
    """Json Error

    Args:
        msg: error message

    Returns:
        JsonResponse: 'status':'error' + msg
    """
    return JsonResponse({"status": "error", "msg": msg, **kwargs})


def json_success(msg="", **kwargs):
    """Json Success

    Args:
        msg (optional): success message. Defaults to ''.

    Returns:
        JsonResponse:  'status': 'success' + msg
    """
    return JsonResponse({"status": "success", "msg": msg, **kwargs})


def json_warning(msg, **kwargs):
    """Json Success

    Args:
        msg (optional): warning message. Defaults to ''.

    Returns:
        JsonResponse:  'status': 'warning' + msg
    """
    return JsonResponse({"status": "warning", "msg": msg, **kwargs})
