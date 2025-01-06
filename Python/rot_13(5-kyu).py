def rot13(message):
    def shift_char(c):
        if 'a' <= c <= 'z': 
            return chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= c <= 'Z': 
            return chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        return c 

    return ''.join(shift_char(c) for c in message)


