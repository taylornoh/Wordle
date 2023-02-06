from test import Test

class Wordle:

  def init(self):
    self.solution = ""
    self.guess = ""

  def promptUser(self):
    print("\nWelcome to Wordle!")
    print("\nRules:\n")
    print("1. Must only enter words (no numerics)\n")
    print("2. No white spaces in entries\n")
    print("\nGame Begins:")
    self.solution = input("\nEnter a solution: ")
    self.guess = input("\nEnter a guess: ")
    print("\n")

  def cycleTests(self):
    print("----Testing Cycle Begins----")
    myCycle = Test(self.solution, self.guess)
    myCycle.checkLength()
    myCycle.checkSolutionType()
    myCycle.checkGuessType()
    myCycle.checkSolWhiteSpace()
    myCycle.checkGuessWhiteSpace()
    print("\n-----Testing Cycle Ends----\n")

  def beginGameLogic(self):
    if self.solution == self.guess:
      print("\nResult: Congrats! You guessed the correct word.")
    
