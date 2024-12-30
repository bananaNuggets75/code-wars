def decode_morse(morse_code):
    words = morse_code.strip().split('   ') 
    decoded_words = []
    for word in words:
        # Split each word into individual Morse code characters and decode
        decoded_word = ''.join(MORSE_CODE[char] for char in word.split())
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)