def spiralize(size):
    # n x n zero matrix
    m = [[0] * size for _ in range(size)]

    # directions: right, down, left, up
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    x, y = 0, 0
    m[x][y] = 1

    def is_free(a, b):
        return 0 <= a < size and 0 <= b < size and m[a][b] == 0

    def would_touch_other_ones(nx, ny, prev_x, prev_y):
        # check orthogonal neighbors of (nx,ny)
        for ax, ay in ((nx + 1, ny), (nx - 1, ny), (nx, ny + 1), (nx, ny - 1)):
            if (ax, ay) == (prev_x, prev_y):
                continue
            if 0 <= ax < size and 0 <= ay < size and m[ax][ay] == 1:
                return True
        return False

    while True:
        dx, dy = dirs[d]
        nx, ny = x + dx, y + dy

        # try to move forward if safe
        if is_free(nx, ny) and not would_touch_other_ones(nx, ny, x, y):
            m[nx][ny] = 1
            x, y = nx, ny
            continue

        # otherwise turn right
        d = (d + 1) % 4
        dx, dy = dirs[d]
        nx, ny = x + dx, y + dy

        # if turning doesn't allow a safe move, we're done
        if not (is_free(nx, ny) and not would_touch_other_ones(nx, ny, x, y)):
            break

        m[nx][ny] = 1
        x, y = nx, ny

    return m
