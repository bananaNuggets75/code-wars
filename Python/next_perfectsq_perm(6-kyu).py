def next_perfectsq_perm(lower_limit, k):
    def is_perfect_square(num):
        root = int(num ** 0.5)
        return root * root == num

    def generate_permutations(num):
        str_num = str(num)
        length = len(str_num)
        used = [False] * length
        current = []
        permutations = set()

        def backtrack():
            if len(current) == length:
                perm = int("".join(current))
                permutations.add(perm)
                return
            for i in range(length):
                if used[i]:
                    continue
                if current == [] and str_num[i] == '0':
                    continue
                used[i] = True
                current.append(str_num[i])
                backtrack()
                current.pop()
                used[i] = False

        backtrack()
        return permutations

    num = int(lower_limit ** 0.5) + 1 
    while True:
        square = num * num
        if '0' not in str(square): 
            perms = generate_permutations(square)
            valid_squares = [p for p in perms if is_perfect_square(p)]
            if len(valid_squares) == k:
                return max(valid_squares)
        num += 1
