

def getApiMsg(code) :
    msg = {
        200 : 'Success',
        201 : 'Fail',
        202 : 'not found'
    }
    return msg[code]