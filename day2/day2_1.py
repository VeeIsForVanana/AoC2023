from sys import argv
from enum import StrEnum, auto

class Color(StrEnum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

CONST_MAX_RED = 12
CONST_MAX_GREEN = 13
CONST_MAX_BLUE = 14

class Line:
    
    string: str
    index: int
    rounds: list[dict[Color: int]]

    def __init__(self, inString) -> None:
        self.string = inString
        self.index = 0
        self.rounds = []

    def __str__(self) -> str:
        return f"Round {self.index} with {self.rounds}"

    def parseLine(self):
        gameString, allRoundsString = self.string.split(":")
        self.index = int(gameString[5:])
        
        def fromRoundToDictRound(round: str) -> dict[Color: int]:

            def fromColorCountToTuple(colorCount: str) -> (Color, int):
                colorCount = colorCount.strip()
                match colorCount.split()[1]:
                    case Color.RED:
                        return (Color.RED, int(colorCount.split(" ")[0]))
                    case Color.BLUE:
                        return (Color.BLUE, int(colorCount.split(" ")[0]))
                    case Color.GREEN:
                        return (Color.GREEN, int(colorCount.split(" ")[0]))

            return dict(map(fromColorCountToTuple, round.split(',')))

        rounds = allRoundsString.split(";")
        self.rounds = list(map(fromRoundToDictRound, rounds))
        return self

    def returnValidSum(self) -> int:
        
        def validityCheck(inDict: dict) -> bool:
            print(f'inDict: {inDict}')
            print(f'sum: {sum(inDict.values()) <= CONST_MAX_BLUE + CONST_MAX_GREEN + CONST_MAX_RED}')
            print(f'red: {inDict.get(Color.RED, 0) <= CONST_MAX_RED}')
            print(f'green: {inDict.get(Color.GREEN, 0) <= CONST_MAX_GREEN}')
            print(f'blue: {inDict.get(Color.BLUE, 0) <= CONST_MAX_BLUE}')
            return (sum(inDict.values()) <= CONST_MAX_BLUE + CONST_MAX_GREEN + CONST_MAX_RED) & (inDict.get(Color.RED, 0) <= CONST_MAX_RED) & (inDict.get(Color.GREEN, 0) <= CONST_MAX_GREEN) & (inDict.get(Color.BLUE, 0) <= CONST_MAX_BLUE)
        
        print(self.rounds)
        return self.index if all(list(map(validityCheck, self.rounds))) else 0

def main(filename: str) -> int:
    with open(filename) as file:
        total = 0
        while((line := file.readline()) != ""):
            print(line)
            total += (Line(line).parseLine().returnValidSum())
        print(total)
        return total

if __name__ == "__main__":
    main(argv[1])