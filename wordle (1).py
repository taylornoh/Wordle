from test import Test

class Wordle:

  def __init__(self):
    self.solution = ""
    self.guess = ""
    self.testCount = 0

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
    self.myCycle = Test(self.solution, self.guess)
    print("----Testing Cycle Begins----")
    self.myCycle.checkLength()
    self.myCycle.checkSolutionType()
    self.myCycle.checkGuessType()
    self.myCycle.checkSolWhiteSpace()
    self.myCycle.checkGuessWhiteSpace()
    print("\n-----Testing Cycle Ends----\n")

  def beginGameLogic(self):
    errorCount = 0
    self.statusList = [""]
    if self.solution == self.guess:
      print("\nResult: Congrats! You guessed the correct word.")
    if self.myCycle.getTestCount() != 5:
      print("\nERROR: Invalid Input")
    else:
      for i in range(len(self.guess)):
        if self.guess[i] != self.solution[i]:
          self.statusList.append("_")
          errorCount += 1
        else:
          self.statusList.append(str(self.guess[i]))
    if errorCount > 0:
      print("\nYou need " + str(errorCount) + " more letter(s) to win:")
      for element in self.statusList:
        print(element)
      self.guess = input("\nEnter a new guess: ")
      return(self.beginGameLogic())
