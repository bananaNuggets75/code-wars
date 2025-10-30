""" To give credit where credit is due: This problem was taken from the ACMICPC-Northwest Regional Programming Contest. Thank you problem writers.

You are helping an archaeologist decipher some runes. He knows that this ancient society used a Base 10 system, and that they never start a number with a leading zero. He's figured out most of the digits as well as a few operators, but he needs your help to figure out the rest.

The professor will give you a simple math expression, of the form

[number][op][number]=[number]
He has converted all of the runes he knows into digits. The only operators he knows are addition (+),subtraction(-), and multiplication (*), so those are the only ones that will appear. Each number will be in the range from -1000000 to 1000000, and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s. If there are ?s in an expression, they represent a digit rune that the professor doesn't know (never an operator, and never a leading -). All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the other given digits in the expression. No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.

Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works, give the lowest one. If no digit works, well, that's bad news for the professor - it means that he's got some of his runes wrong. output -1 in that case.

Complete the method to solve the expression to find the value of the unknown rune. The method takes a string as a paramater repressenting the expression and will return an int value representing the unknown rune or -1 if no such rune exists.

 """
 
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
