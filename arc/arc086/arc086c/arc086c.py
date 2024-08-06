def is_reachable(time_positions):
    prev_t, prev_x, prev_y = 0, 0, 0

    for t, x, y in time_positions:
        dt = t - prev_t
        dx = abs(x - prev_x)
        dy = abs(y - prev_y)

        # 移動可能か判定（dx+dyがdt未満ならそももそ移動不可、奇数と奇数、偶数と偶数のペアでないならdt時にその場に入れない）
        if dt < dx + dy or (dt - dx - dy) % 2 != 0:
            return "No"

        prev_t, prev_x, prev_y = t, x, y

    return "Yes"

# 入力の処理
N = int(input())
time_positions = [tuple(map(int, input().split())) for _ in range(N)]

# 判定結果を出力
print(is_reachable(time_positions))