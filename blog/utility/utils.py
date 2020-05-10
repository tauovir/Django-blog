from django.conf import settings

def setCommentFormat(commetQuerySet):
    commentList = []
    repliedDict = {}
    if not commetQuerySet: # Check Query set is Empty or not
        return commentList
    else:
        for cmt in commetQuerySet:
            if cmt.replied_on == 0:
                commentData = {
                    'comment_id':cmt.id,'comment':cmt.comment,
                'user_name':getCommenterName(cmt.user),
                'comment_date' : cmt.created_at
                }
                commentList.append(commentData)
            elif cmt.replied_on != 0: # Check it reply of a comment or Comment only
                if cmt.replied_on in repliedDict.keys(): 
                    temList = []
                    temp = {'comment':cmt.comment,'user_name':getCommenterName(cmt.user),'comment_date' : cmt.created_at}
                    temList = repliedDict[cmt.replied_on]
                    temList.append(temp)
                    repliedDict[cmt.replied_on] = temList
                else:
                    temp = [{'comment':cmt.comment,'user_name':getCommenterName(cmt.user),'comment_date' : cmt.created_at}]
                    repliedDict[cmt.replied_on] = temp

        
               
        # Loof for injecting reply to particular comment
        commentList = setReplyToComment(commentList, repliedDict)
        #print(commentList)

        return commentList

def getCommenterName(userObj):
    name = ''
    if userObj.first_name:
        name = userObj.first_name + " " + userObj.last_name
    else:
        name = userObj.username
        
    return name



def setReplyToComment(commentList,relpyDict):
    for cmt1 in commentList:
            if cmt1['comment_id'] in relpyDict.keys():
                cmt1['reply'] = relpyDict[cmt1['comment_id']]
            else:
                cmt1['reply'] = []
    return commentList

# Write Temporary file
def writeTempFile(text = ''):
    filePath = settings.MEDIA_ROOT+"/textFile/slug.txt"
    if not text:
        f = open(filePath, "r")
        slug = f.read()
        return slug
    else:
        f = open(filePath, "a") # Open Blank file
        f.seek(0)  # sets the reference point at the beginning of the file(setting position of the offset)
        f.truncate()  # Clear previous content
        f.write(text) # Write file
        f.close() # Close file
        return text