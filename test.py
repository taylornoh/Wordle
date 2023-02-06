import re


class Test:

  def __init__(self, solution, guess):
    self.solution = solution
    self.solutionLength = 0
    self.guess = guess
    self.guessLength = 0
    self.testCount = 0

  def getTestCount(self):
    return (self.testCount)

  def checkLength(self):
    self.solutionLength = len(self.solution)
    self.guessLength = len(self.guess)
    
    if self.solutionLength != self.guessLength:
      self.testCount -= 1
      print("\nLength Test: FAILED\n")
    else:
      print("\nLength Test: PASSED\n")
      self.testCount += 1

  def checkSolutionType(self):
    if self.solution.isdigit():
      self.testCount -= 1
      print("\nSolution Type Test: FAILED")
    try:
      float(self.solution)
      self.testCount -= 1
      print("Solution Type Test: FAILED")
    except ValueError:
      self.testCount += 1
      print("Solution Type Test: PASSED")

  def checkGuessType(self):
    if self.guess.isdigit():
      self.testCount -= 1
      print("\nGuess Type Test: FAILED")
    try:
      float(self.guess)
      self.testCount -= 1
      print("\nGuess Type Test: FAILED")
    except ValueError:
      self.testCount += 1
      print("\nGuess Type Test: PASSED")

  def checkSolWhiteSpace(self):
    res = bool(re.search(r"\s", self.solution))
    if res:
      self.testCount -= 1
      print("\nSolution White Space Test: FAILED")
    else:
      self.testCount += 1
      print("\nSolution White Space Test: PASSED")

  def checkGuessWhiteSpace(self):
    res = bool(re.search(r"\s", self.guess))
    if res:
      print("\nGuess White Space Test: FAILED")
    else:
      self.testCount += 1
      print("\nGuess White Space Test: PASSED")
