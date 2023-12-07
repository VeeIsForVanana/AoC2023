import re

def getFirstAndLastCharacterAsInt(line: str) -> int:
    return int(''.join([re.sub(r'[A-z\s]', '', line)[i] for i in [0, -1]]))

def main():
    with open("test.txt") as file:
        total: int = 0
        
        while((line := file.readline()) != ''):
            total += getFirstAndLastCharacterAsInt(line)
        
        return total

if __name__ == '__main__':
    main()