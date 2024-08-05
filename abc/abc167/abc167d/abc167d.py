N,K = map(int, input().split())

teleporter = [0] + list(map(int, input().split()))

pos = 1
visited = {1:0}

jumps = 0

while jumps < K:
    pos = teleporter[pos]
    jumps += 1

    # posがvisited内にあるか判定。なければ現在位置に移動を記載
    if pos in visited:
        #周期の長さ
        loop_length = jumps -visited[pos]

        #周期前の余分な長さ
        K -= visited[pos]
        #残りのK回分
        to_jump = K % loop_length

        #残りのK回分位置の値をセット
        for _ in range(to_jump):
            pos =teleporter[pos]
        
        print(pos)
        exit()

    visited[pos] = jumps

print(pos)