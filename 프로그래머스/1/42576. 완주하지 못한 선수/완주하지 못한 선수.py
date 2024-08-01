def solution(participant, completion):
    # hashed algorithm
    
    dic = {}
    for p in participant:
        #참가자들의 이름 추가
        if p in dic:
            dic[p] += 1
        else:
            dic[p] =1
            
    
    for c in completion:
        dic[c] -= 1
    
    for k in dic.keys():
        if dic[k] > 0:
            return k
