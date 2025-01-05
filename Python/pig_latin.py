def pig_it(text):
    words = text.split()
    result = []
    for word in words:
        if word.isalpha(): 
            result.append(word[1:] + word[0] + 'ay')
        else:
            result.append(word) 
    return ' '.join(result)