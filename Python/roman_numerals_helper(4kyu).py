Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

""" In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1
Help
+--------+-------+
| Symbol | Value |
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
+--------+-------+ """

class RomanNumerals:
    roman_map = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    ]

    @staticmethod
    def to_roman(val: int) -> str:
        result = []
        for symbol, number in RomanNumerals.roman_map:
            while val >= number:
                result.append(symbol)
                val -= number
        return "".join(result)

    @staticmethod
    def from_roman(roman_num: str) -> int:
        i = 0
        result = 0
        roman_dict = dict(RomanNumerals.roman_map)

        while i < len(roman_num):
            # check if two-character symbol is valid
            if i + 1 < len(roman_num) and roman_num[i:i+2] in roman_dict:
                result += roman_dict[roman_num[i:i+2]]
                i += 2
            else:
                result += roman_dict[roman_num[i]]
                i += 1
        return result


""" class RomanNumerals:

    def to_roman(val):
        onesRoman = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tensRoman = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hundsRoman = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thousRoman = ["","M","MM","MMM","MMMM"]
            
        ones =  onesRoman[val % 10]
        tens = tensRoman[val // 10 % 10]
        hunds = hundsRoman[val // 100 % 10]
        thous = thousRoman[val // 1000]
        
            
        return thous + hunds + tens + ones

    def from_roman(roman_num):
        out = 0 
        mx = 0
        for cur in map(lambda c: { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 } [c], roman_num[::-1]):
            if cur >= mx: 
                out += cur
                mx = cur
            else:
                out -= cur
        
        return out
        

from itertools import groupby

"""A RomanNumerals helper object"""
class RomanNumerals(object):
    letters = [('M',1000), ('CM',900), ('D',500), ('CD',400), ('C',100), ('XC',90),
               ('L',50), ('XL',40), ('X',10), ('IX',9), ('V',5), ('IV',4), ('I',1)]
    
    @classmethod
    def to_roman(cls, val):
        rom = []
        for l, v in cls.letters:
            m = val // v
            rom += m*[l]
            val -= m*v
        return ''.join(rom)
        
    @classmethod
    def from_roman(cls, rom):
        cumu = 0
        for l, v in cls.letters:
            while rom[:len(l)] == l:
                rom = rom[len(l):]
                cumu += v
            if not rom: break
        return cumu
        
class RomanNumerals:
    @staticmethod
    def from_roman(s):
        X=[dict(zip('MDCLXVI',(1e3,500,100,50,10,5,1)))[x]for x in s]
        return int(sum((x,-x)[x<y]for x,y in zip(X,X[1:]))+X[-1])
    @staticmethod
    def to_roman(i,o=' I II III IV V VI VII VIII IX'.split(' ')):
        r=lambda n:o[n]if n<10 else''.join(dict(zip('IVXLC','XLCDM'))[c]for c in r(n//10))+o[n%10]
        return r(i)
         """