def to_camel_case(text):
    words = text.replace('-', ' ').replace('_', ' ').split()
    for i in range(1, len(words)):
        words[i] = words[i].capitalize()
    return ''.join(words)
