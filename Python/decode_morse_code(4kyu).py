""" Part of Series 2/3
This kata is part of a series on the Morse code. Make sure you solve the previous part before you try this one. After you solve this kata, you may move to the next one.


In this kata you have to write a Morse code decoder for wired electrical telegraph.
Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects the wires together, which can be detected on a remote station. The Morse code encodes every character being transmitted as a sequence of "dots" (short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is. And in fact different operators would transmit at different speed. An amateur person may need a few seconds to transmit a single character, a skilled professional can transmit 60 words per minute, and robotic transmitters may go way faster.

For this kata we assume the message receiving is performed automatically by the hardware that checks the line periodically, and if the line is connected (the key at the remote station is down), 1 is recorded, and if the line is not connected (remote key is up), 0 is recorded. After the message is fully received, it gets to you for decoding as a string containing only symbols 0 and 1.

For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:

1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line exactly two times per "dot".

That said, your task is to implement two functions:

Function decodeBits(bits), that should find out the transmission rate of the message, correctly decode the message to dots ., dashes - and spaces (one between characters, three between words) and return those as a string. Note that some extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them. Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.
2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string.

NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you (see the solution setup, to get its identifier in your language).


Eg:
  morseCodes(".--") //to access the morse translation of ".--"
All the test strings would be valid to the point that they could be reliably decoded as described above, so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!

Good luck! """

import re

def decode_bits(bits):
    # Trim leading and trailing zeros
    bits = bits.strip('0')
    if not bits:
        return ''
    
    # Find minimal time unit (shortest streak of 1s or 0s)
    chunks = re.findall(r'(0+|1+)', bits)
    unit = min(len(chunk) for chunk in chunks)

    # Translate according to Morse timing rules
    bits = bits.replace('111' * unit, '-')
    bits = bits.replace('1' * unit, '.')
    bits = bits.replace('0000000' * unit, '   ')
    bits = bits.replace('000' * unit, ' ')
    bits = bits.replace('0' * unit, '')
    
    return bits


def decode_morse(morseCode):
    # Trim whitespace
    morseCode = morseCode.strip()
    
    # Split into words
    words = morseCode.split('   ')
    decoded_words = []
    
    for word in words:
        # Split into characters
        chars = word.split()
        decoded_chars = [MORSE_CODE[char] for char in chars]
        decoded_words.append(''.join(decoded_chars))
    
    return ' '.join(decoded_words)


""" def decodeBits(bits):
    import re
    
    # remove trailing and leading 0's
    bits = bits.strip('0')
    
    # find the least amount of occurrences of either a 0 or 1, and that is the time hop
    time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))
    
    # hop through the bits and translate to morse
    return bits[::time_unit].replace('111', '-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','')

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[l] for l in w.split()) for w in morseCode.split('   '))

# add dictionary entry for space
MORSE_CODE['_'] = ' '

def decodeBits(bits):
    # strip extra zeros
    bits = bits.strip('0')
    
    # if no zeros in bits
    if '0' not in bits:
        return '.'
    
    # check for multiple bits per dot
    minOnes = min(len(s) for s in bits.split('0') if s)
    minZeros = min(len(s) for s in bits.split('1') if s)
    m = min(minOnes, minZeros)
    
    # decode bits to morse code
    return bits.replace('111'*m, '-').replace('0000000'*m, ' _ ').replace('000'*m, ' ').replace('1'*m, '.').replace('0'*m, '')

def decodeMorse(morseCode):
    # decode morse code to letters
    return ''.join(MORSE_CODE[c] for c in morseCode.split()) """

from re import findall

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}
MORSE_CODE["_"] = " "

""" def decodeBits(bitString):
    bitString = bitString.strip("0")
    m = len(sorted(findall( "(1+|0+)", bitString ), key=len)[0])
    return bitString.replace('111'*m, '-').replace('000'*m, ' ').replace('1'*m, '.').replace('0'*m, '')

def decodeMorse(morseCode):
    print(morseCode)
    return "".join(map(lambda m: MORSE_CODE.get(m," "), morseCode.replace("   "," _ " ).split(" "))).strip()

def decodeBits(bits):
    bits = bits.strip('0')
    time_unit = min(map(len, bits.replace('1', ' ').split() + bits.replace('0', ' ').split()))
    word_sep = '0' * 7 * time_unit
    char_sep = '0' * 3 * time_unit
    ones_sep = '0' * 1 * time_unit
    dash = '1' * 3 * time_unit
    dot = '1' * 1 * time_unit
    return bits.replace(dash, '-').replace(dot, '.') \
               .replace(word_sep, '   ').replace(char_sep, ' ').replace(ones_sep, '')

def decodeMorse(morse_code):
    return ' '.join(''.join(map(MORSE_CODE.get, word.split()))
                    for word in morse_code.split('   ')).strip() """