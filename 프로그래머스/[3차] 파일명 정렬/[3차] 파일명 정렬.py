def solution(files):
    answer = []
    head = {}
    nothead = {}
    number = {}
    for file in files:
        for id in range(len(file)):
            if not file[id].isdigit():
                #문자열은 소문자로 통일
                try:
                    head[file] += file[id].lower()
                except:
                    head[file] = file[id].lower()
            else:
                nothead[file] = file[id:]
                break
        count=0 # 숫자는 최대 5자리
        for id in range(len(nothead[file])):
            if count >=5:
                break
            if nothead[file][id].isdigit():
                count +=1
                try:
                    number[file] += nothead[file][id]
                except:
                    number[file] = nothead[file][id]
            else:
                break
                    
        # 숫자에서 처음 0 제거
        number[file] = int(number[file])
   
    # head의 key, value 자리 바꾸기
    new_head = {}
    for key in head.keys():
        if new_head.get(head.get(key)):
            new_head[head.get(key)].append(key)
        else:
            new_head[head.get(key)] = [key]
    new_head = dict(sorted(new_head.items(), key=lambda x:x[0]))


    for array in new_head.values():
        if len(array) ==1:
            answer.append(array[0])
        else:
            array = sorted(array, key= lambda x: number[x])
            answer += array
                
    return answer