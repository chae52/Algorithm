# import sys
# sys.stdin = open("input.txt", "r")
INT_MAX= 1e9

def cal_distance(r1,c1, r2, c2):
    return (r1-r2)**2 + (c1-c2)**2
def find_santa(n, m, p, c, d, rr,rc,info_santa):
    # r이 큰 것부터, c 가 큰 것부터 순으로
    # 루돌프는 기절한 산타를 돌진 대상으로 선택할 수 있습니다.
    distances=[]
    sorted_santa=list()
    for i in range(p):
        x=info_santa['location'][i][:]
        x.append(i)
        sorted_santa.append(x)
    sorted_santa=sorted(sorted_santa, reverse=True)
    for idx, santa in enumerate(sorted_santa):
        # sorted santa의 index와 원래 santa의 인덱스가 같지 않아서 state가 맞지 않음
        if info_santa['state'][sorted_santa[idx][2]] >=0: # 죽지 않은 산타 #sorted_santa[idx][2]=원래 santas에서의 인덱스
            distances.append(cal_distance(santa[0], santa[1],rr,rc))
        else: # 죽은 산타
            distances.append(INT_MAX)
    min_dis = distances.index(min(distances))
    target_santa_location = sorted_santa[min_dis]
    target = info_santa['location'].index(target_santa_location[:2])
    return target +1

def move_rudolph(n, m, p, c, d, rr, rc, info_santa, target_santa):
    r_di=[[1,0,-1,0,1,1,-1,-1],
          [0,1,0,-1,1,-1,1,-1]]
    sr, sc = info_santa['location'][target_santa-1]
    distances=[]
    for i in range(len(r_di[0])):
        new_rr = rr + r_di[0][i]
        new_rc = rc + r_di[1][i]
        if 0<new_rr and new_rr<=n and 0<new_rc and new_rc<=n:
            distances.append(cal_distance(sr, sc, new_rr, new_rc))
        else:
            distances.append(INT_MAX)
    dr,dc = r_di[0][distances.index(min(distances))], r_di[1][distances.index(min(distances))]

    # 루돌프 위치 옮기기
    rr += dr
    rc += dc

    bumped=False
    if sr == rr and sc == rc: # 타겟 산타와 부딪힘
        bumped=True

    return rr,rc, bumped, dr, dc
def pull_santa(n, jumsu, rr,rc,info_santa, target, dr, dc,graph):
    # 기절한 산타는 움직일 수 없게 됩니다. 단, 기절한 도중 충돌이나 상호작용으로 인해 밀려날 수는 있습니다.
    # 1번 산타는 루돌프와 충돌하게 되어 2(=C)의 점수를 얻으면서 격자 밖으로 거리 2(=C)만큼 튕겨나가게 됩니다. 1번 산타는 4번 턴까지 기절하게 됩니다.
    info_santa['location'][target-1][0] += dr*jumsu
    info_santa['location'][target-1][1] += dc*jumsu
    info_santa['score'][target-1] += jumsu
    if (0<info_santa['location'][target-1][0]  and info_santa['location'][target-1][0]<=n
            and 0<info_santa['location'][target-1][1]  and info_santa['location'][target-1][1]<=n):
        info_santa['state'][target-1] = 2
        info_santa, graph=interaction(n, dr,dc, info_santa, graph, target)
    else:
        info_santa['state'][target - 1] = -1
    graph = [[0] * (n+1) for _ in range(n+1)]
    graph[rr][rc] = 99

    for idx, santa in enumerate(info_santa['location']):
        if info_santa['state'][idx]==-1:
            continue
        else:
            graph[santa[0]][santa[1]] = idx + 1
    return info_santa,graph
def interaction(n, dr, dc, info_santa, graph, target):
    # 이미 d나 c만큼 움직인 상태로 온다
    # 이동 할 방향 = dr, dc
    now_r, now_c = info_santa['location'][target-1]
    while True:
        if 0<now_r<=n and 0<now_c<=n and graph[now_r][now_c]>0 and target !=graph[now_r][now_c]: # 또 부딪힘 # 나 자신과 부딪히면 안 됌
            bumped_santa = graph[now_r][now_c] # index임
            info_santa['location'][bumped_santa - 1][0] += dr # 산타 밀기
            info_santa['location'][bumped_santa - 1][1] += dc
            if (info_santa['location'][bumped_santa - 1][0]>n or
                    info_santa['location'][bumped_santa - 1][0] <=0 or
                    info_santa['location'][bumped_santa - 1][1] > n or
                    info_santa['location'][bumped_santa - 1][1] <= 0 ): # 밀려서 죽은 산타 처리
                info_santa['state'][bumped_santa - 1]=-1 # 죽음처리
        else:
            break
        now_r += dr
        now_c += dc
    return info_santa, graph
def find_rudolph(n,p, rr,rc,info_santa, santa,graph):
    sr, sc = info_santa['location'][santa-1]
    s_di = [[-1, 0, 1, 0],
            [0, 1, 0, -1]] # 상우하좌
    found=False
    distances=[]
    for i in range(4):
        new_sr= sr+s_di[0][i]
        new_sc= sc+s_di[1][i]

        if 0<new_sr<=n and 0<new_sc<=n and (graph[new_sr][new_sc]==0 or graph[new_sr][new_sc]==99):
            distances.append(cal_distance(rr, rc, new_sr, new_sc))
        else:
            distances.append(INT_MAX)

    ori_dist = cal_distance(rr, rc, sr, sc)
    min_dist = min(distances)
    for i in range(len(distances)):
        if ori_dist>distances[i] and distances[i] == min_dist:
            found=True
            break
    return found, s_di[0][i], s_di[1][i]

def move_santa(n,p, jumsu, rr,rc,info_santa, santa,graph,dr,dc):
    sr, sc = info_santa['location'][santa - 1]
    new_sr = sr + dr
    new_sc = sc + dc
    info_santa['location'][santa-1] = [new_sr, new_sc]

    if rr == new_sr and rc == new_sc: # 루돌프와 부딪힘
        info_santa, graph = pull_santa(n, jumsu, rr, rc, info_santa, santa, dr*(-1), dc*(-1), graph)
    else:
        graph[sr][sc]=0
        graph[new_sr][new_sc]=santa
    return info_santa, graph

# T = int(input())
T=1
for test_case in range(1, T + 1):
    n, m, p, c, d = map(int, input().split(' '))
    rr,rc = map(int, input().split(' '))
    santas=[[] for i in range(p)]
    for i in range(p):
        idx, dr,dc = list(map(int, input().split(' ')))
        santas[idx-1]=[dr,dc]

    santa_state = [0] * len(santas)  # 0: 살아있음, 2: 기절, -1: 죽음
    santa_score = [0] * len(santas)
    info_santa = {'state': santa_state,
                  'score': santa_score,
                  'location': santas
                  }
    # 그래프 ::::: 0: 빈 칸, 1 : 산타, 99: 루돌프
    graph = [[0] * (n+1) for _ in range(n+1)]
    graph[rr][rc] = 99

    for idx, santa in enumerate(santas):
        graph[santa[0]][santa[1]] = idx + 1

    for iiii in range(m):
        for ii in range(p): # 기절 상태 살리기
            if info_santa['state'][ii] > 0 :
                info_santa['state'][ii]-=1

        target_santa = find_santa(n, m, p, c, d, rr,rc,info_santa)
        new_rr, new_rc, bumped, dr, dc = move_rudolph(n, m, p, c, d, rr, rc, info_santa, target_santa)
        graph[rr][rc]=0
        graph[new_rr][new_rc]=99
        rr=new_rr
        rc= new_rc
        if bumped:
            info_santa,graph=pull_santa(n, c, rr,rc,info_santa, target_santa, dr, dc,graph)
        for idx,santa in enumerate(info_santa['location']):
            # 산타가 살아 있을 때만
            if info_santa['state'][idx]==0:
                found,dr,dc=find_rudolph(n,p, rr,rc,info_santa, idx+1,graph)
                if found:
                        info_santa,graph = move_santa(n,p, d,rr,rc,info_santa, idx+1,graph,dr,dc)

        # 살아있는 산타 1점 씩 추가
        for i in range(p):
            if info_santa['state'][i]>=0:
                info_santa['score'][i]+=1
    # 답 출력
    print(*info_santa['score'])
