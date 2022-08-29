def make_response(status, message, body_key=False, body=False):
    response = {}
    response['status'] = status
    response['message'] = message

    if (body_key and body):
        response[body_key] = body

    return response
