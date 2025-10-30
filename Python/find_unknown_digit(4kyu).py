def solve_runes(expression):
    left_side, right_side = expression.split('=')
    used_digits = {ch for ch in expression if ch.isdigit()}

    def invalid(num):
        # Reject numbers with invalid leading zeros like "012" or "-01"
        return (len(num) > 1 and num[0] == '0') or (len(num) > 2 and num[0] == '-' and num[1] == '0')

    # Find operator that isn't a leading minus
    def find_operator(expr):
        for i, ch in enumerate(expr):
            if ch in '+-*' and i != 0:
                return ch, i
        return None, -1

    for d in map(str, range(10)):
        if d in used_digits:
            continue

        trial_expr = expression.replace('?', d)
        left_side_replaced, right_side_replaced = trial_expr.split('=')

        op, pos = find_operator(left_side_replaced)
        if op is None:
            continue

        a = left_side_replaced[:pos]
        b = left_side_replaced[pos + 1:]
        c = right_side_replaced

        # Skip invalid numbers
        if any(invalid(x) for x in [a, b, c]):
            continue

        try:
            a, b, c = int(a), int(b), int(c)
        except ValueError:
            continue

        if op == '+' and a + b == c:
            return int(d)
        elif op == '-' and a - b == c:
            return int(d)
        elif op == '*' and a * b == c:
            return int(d)

    return -1
