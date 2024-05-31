print("Enter your sentence:")
sentence = input()
print(findLetters(Hello))


def findLetters(sentence):
	characters = []
    numbers = []
    number = 0
	for letter in sentence:
    	number = number + 1
		characters.append(letter)
        characters.append(number)
    return[characters, numbers]
