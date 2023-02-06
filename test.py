import re


class Test:

  def __init__(self, solution, guess):
    self.solution = solution
    self.solutionLength = 0
    self.guess = guess
    self.guessLength = 0

  def checkLength(self):
    self.solutionLength = len(self.solution)
    self.guessLength = len(self.guess)
    if self.solutionLength != self.guessLength:
      print("\nLength Test: FAILED\n")
    else:
      print("\nLength Test: PASSED\n")

  def checkSolutionType(self):
    if self.solution.isdigit():
      print("\nSolution Type Test: FAILED")
    try:
      float(self.solution)
      print("Solution Type Test: FAILED")
    except ValueError:
      print("Solution Type Test: PASSED")

  def checkGuessType(self):
    if self.guess.isdigit():
      print("\nGuess Type Test: FAILED")
    try:
      float(self.guess)
      print("\nGuess Type Test: FAILED")
    except ValueError:
      print("\nGuess Type Test: PASSED")

  def checkSolWhiteSpace(self):
    res = bool(re.search(r"\s", self.solution))
    if res:
      print("\nSolution White Space Test: FAILED")
    else:
      print("\nSolution White Space Test: PASSED")

  def checkGuessWhiteSpace(self):
    res = bool(re.search(r"\s", self.guess))
    if res:
      print("\nGuess White Space Test: FAILED")
    else:
      print("\nGuess White Space Test: PASSED")
