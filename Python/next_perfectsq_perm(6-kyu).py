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


# or 
""" from itertools import count, permutations

def next_perfectsq_perm(limit_below, k):
    for n in count(int(limit_below**.5)+1):
        s = str(n**2)
        if '0' not in s:
            sq_set = {x for x in (int(''.join(p)) for p in permutations(s)) if (x**.5).is_integer()}
            if len(sq_set) == k:
                return max(sq_set) """


# or 
""" from itertools import permutations

def is_perfect(square):
    return round(square**0.5)**2 == square

def permuted(n):
    return (int("".join(p)) for p in set(permutations(str(n))))

def perfect_permutations(n):
    return tuple(p for p in permuted(n) if is_perfect(p))
    
def next_perfectsq_perm(lower_limit, k): 
    root = int(lower_limit**0.5) + 1
    while True:
        square = root**2
        if not "0" in str(square):
            p = perfect_permutations(square)
            if len(p) == k:
                return max(p)
        root += 1 """


