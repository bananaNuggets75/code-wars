def alphabet_position(text):
    result = []
    for char in text:
        if char.isalpha():  
            result.append(str(ord(char.lower()) - 96)) 
    return ' '.join(result)
