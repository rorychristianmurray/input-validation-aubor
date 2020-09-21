import pyinputplus as pyip

response = pyip.inputNum(prompt="enter num : ",allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

print(response)
