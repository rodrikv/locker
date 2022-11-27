def response_data(data=None, msg=None, code=None):
    d = {}
    if data:
        d["data"] = data
    if code:
        d["code"] = code
    if msg:
        d["msg"] = msg
    return d
