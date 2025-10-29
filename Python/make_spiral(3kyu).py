""" Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
 """

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
