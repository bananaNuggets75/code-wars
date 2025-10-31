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
