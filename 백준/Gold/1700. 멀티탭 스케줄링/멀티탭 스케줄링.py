import sys
input = sys.stdin.readline

n, k = map(int, input().split())

plugs = list(map(int, input().split()))

curr_plugs = []
cnt = 0
for i in range(k):
    flag = False
    if len(curr_plugs) < n and plugs[i] not in curr_plugs: # 플러그 공간 있는 경우
        curr_plugs.append(plugs[i])
    elif plugs[i] in curr_plugs: # 이미 플러그 꽂혀있는 경우
        continue
    else: 
        for now in curr_plugs:
            if now not in plugs[i+1:]: # 나중에 안쓰이는 플러그 제거 
                curr_plugs.remove(now)
                curr_plugs.append(plugs[i])
                cnt += 1
                flag = True
                break
        if flag == False: # 만약 둘다 뒤에서 쓸 경우 아무거나가 아니고 가장 나중에 쓰일 애를 빼야 함
            latest_pos = -1 # 가장 나중에 등장하는 인덱스 저장
            target = None # 
            for now in curr_plugs:
                pos = plugs[i+1:].index(now) # plugs 해당 범위 중 now의 인덱스 반환
                if pos > latest_pos:
                    latest_pos = pos
                    target = now
            curr_plugs.remove(target)
            curr_plugs.append(plugs[i])
            cnt += 1
print(cnt)
