def alphabet_position(text):
    result = []
    for char in text:
        if char.isalpha():  
            result.append(str(ord(char.lower()) - 96)) 
    return ' '.join(result)

#or 
""" def alphabet_position(text):
    return ' '.join(str(ord(char) - 96) for char in text.lower() if char.isalpha())
 """