import re

WORD_TO_NUMERAL_DICT = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
WORD_TO_NUMERAL_PATTERN = r'one|two|three|four|five|six|seven|eight|nine'
NON_NUMERICALS_PATTERN = r'[A-z\s]'

def replaceWordNumericals(line: str) -> str:
    def wordToNumerical(matchobj: re.Match) -> str:
        return str(WORD_TO_NUMERAL_DICT[matchobj.group(0)])
    return re.sub(WORD_TO_NUMERAL_PATTERN, wordToNumerical, line)

def stripNonNumericals(line: str) -> str:
    return re.sub(NON_NUMERICALS_PATTERN, '', line)

def getFirstAndLastCharacterAsInt(line: str) -> int:
    return int(''.join([stripNonNumericals(replaceWordNumericals(line))[i] for i in [0, -1]]))

def main():
    with open(".txt") as file:
        total: int = 0
        
        while((line := file.readline()) != ''):
            total += getFirstAndLastCharacterAsInt(line)
        
        print(total)

        return total

if __name__ == '__main__':
    main()