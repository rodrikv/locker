def response_data(data=None, code=None, msg=None):
    d = {}
    if data:
        d["data"] = data
    if code:
        d["code"] = code
    if msg:
        d["msg"] = msg
    return d
