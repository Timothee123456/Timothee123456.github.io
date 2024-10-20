import time
import sys
import time
class color:
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    STRIKETHROUGH = '\033[9m'
    class light:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        GREY = '\033[97m'
    class dark:
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        GREY = '\033[37m'

def write(text, delay=0.05):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after scrolling
        
print('To which number would you like to go to?')
nb1 = input(">")
nb = nb1.replace(" ", "")
while not nb.isdigit():
    print("Please enter a valid number")
    nb = input(">")
    nb = nb.replace(" ", "")

Max = int(nb)
print(color.dark.GREEN + 'Working...' + color.END)



start_time = time.time()

prime_numbers = []
odd = []

for number in range(3, Max, 2):
    if number not in odd:
        odd.append(number)
        prime_numbers.append(number)
    odd.sort()
    for item in odd:
        if item <= number:
            result = item * number
            if result > Max:
                break
            odd.append(result)

prime_numbers.insert(0, 2)

end_time = time.time()
execution_time = end_time - start_time

write('It took the computer ' + str(execution_time) + ' seconds to count ' + str(len(prime_numbers)) + ' prime numbers, between 1 and ' + str(nb1))
print(prime_numbers)



#time.sleep(1)
#print('There are ' + b10 + ' prime numbers between 1 and 10')
#print('There are ' + b100 + ' prime numbers between 1 and 100')
#print('There are ' + b1000 + ' prime numbers between 1 and 1000')
#print('There are ' + b10000 + ' prime numbers between 1 and 10 000')
#print('There are ' + b100000 + ' prime numbers between 1 and 100 000')
#print('There are ' + b1000000 + ' prime numbers between 1 and 1 000 000')
#print('There are ' + b10000000 + ' prime numbers between 1 and 10 000 000')
#print('There are ' + b100000000 + ' prime numbers between 1 and 100 000 000')
#print('There are ' + b1000000000 + ' prime numbers between 1 and 1 000 000 000')
