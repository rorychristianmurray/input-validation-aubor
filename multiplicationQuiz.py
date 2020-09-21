import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
  # pick two rand nums
  num1 = random.randint(0,9)
  num2 = random.randint(0,9)

  prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

  # right answers are handled by allowRegexes
  # wrong answers are handled by blockRegexes

  try:
    pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
      blockRegexes=[('.*', 'incorrect')],
      timeout=10, limit=3
    )

  except pyip.TimeoutException:
    print('out of time')

  except pyip.RetryLimitException:
    print('out of tries')

  else:
    # runs if correct
    print('correct')
    correctAnswers += 1
  
  time.sleep(1)

print(f'score : {correctAnswers} / {numberOfQuestions}')
