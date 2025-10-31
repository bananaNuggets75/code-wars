""" Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas """

def strip_comments(text, markers):
    lines = text.split('\n')
    result = []

    for line in lines:
        # For each marker, cut the line at the first occurrence
        for m in markers:
            if m in line:
                line = line.split(m)[0]
        result.append(line.rstrip())  # remove trailing spaces

    return '\n'.join(result)
