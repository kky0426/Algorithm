import re

def solution(new_id):
    answer = ''
    answer = new_id.lower()
    answer = re.sub('[^a-z0-9._-]','',answer)
    answer = re.sub('[.]+','.',answer)
    if len(answer)>0 and answer[0] == '.':
        answer=answer[1:]
    if len(answer)>0 and answer[-1] == '.':
        answer=answer[:-1]
    if len(answer) == 0:
        answer+='a'
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer=answer[:-1]
    while(len(answer)<3):
        answer +=answer[-1]
    return answer
