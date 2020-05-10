
def displayData(data = {},msg = '',status = 200):
    responseData = {}
    responseData['data'] = data
    responseData['msg'] = msg
    responseData['status'] = status
    return responseData
    