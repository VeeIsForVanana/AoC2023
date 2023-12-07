import regex

WORD_TO_NUMERAL_DICT = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
WORD_TO_NUMERAL_PATTERN = r''
NON_NUMERICALS_PATTERN = r'[A-z\s]'
ALL_NUMERICALS_PATTERN = r'1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'

def listAllNumericals(line: str) -> list[str]:
    def mapMatchToNumerical(match: str) -> str:
        return WORD_TO_NUMERAL_DICT.get(match, match)
    return list(map(mapMatchToNumerical, regex.findall(ALL_NUMERICALS_PATTERN, line, overlapped=True)))

def getFirstAndLastCharacterAsInt(line: str) -> int:
    return int(''.join(listAllNumericals(line)[i] for i in [0, -1]))

def main():
    with open("input.txt") as file:
        total: int = 0
        
        while((line := file.readline()) != ''):
            total += getFirstAndLastCharacterAsInt(line)
        
        print(total)

        return total

if __name__ == '__main__':
    main()