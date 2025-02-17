def to_camel_case(text):
    words = text.replace('-', ' ').replace('_', ' ').split()
    for i in range(1, len(words)):
        words[i] = words[i].capitalize()
    return ''.join(words)

# or 
""" def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '') """

# or 
""" import re
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text) """
