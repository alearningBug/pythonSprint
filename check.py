class Checker:
    
    
    
  def checkQuestion1(func):
    testCase = [[1],[2]]
    answers = [2,4]
    for i in range(len(testCase)):
      x = func(testCase[i][0])
      if answers[i] != x:
        print(f"Test Case Failed : \nYour output: {x}\nExcepted output : {answers[i]}")
        return False
    return True


  def checkQuestion2(func):
    testCase = [[1],[2]]
    answers = [2,4]
    for i in range(len(testCase)):
      x = func(testCase[i][0])
      if answers[i] != x:
        print(f"Test Case Failed : \nYour output: {x}\nExcepted output : {answers[i]}")
        return False
    return True



  def checkQuestion3(func):
    testCase = [[1],[2]]
    answers = [2,4]
    for i in range(len(testCase)):
      x = func(testCase[i][0])
      if answers[i] != x:
        print(f"Test Case Failed : \nYour output: {x}\nExcepted output : {answers[i]}")
        return False
    return True