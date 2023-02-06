from wordle import Wordle


class Main:
  myWordle = Wordle()
  myWordle.promptUser()
  myWordle.cycleTests()
  myWordle.beginGameLogic()