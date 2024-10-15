import time
import math
import re

start_time = time.time()

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
    class bg:
        INVERTED = '\033[7m'     # this is white text on any color backround
        DARKGREY = '\033[40m'
        RED = '\033[41m'
        GREEN = '\033[42m'
        YELLOW = '\033[43m'
        BLUE = '\033[44m'
        PURPLE = '\033[45m'
        DARKCYAN = '\033[46m'
        LIGHTGREY = '\033[47m'
        


def is_even(number):
    return number % 2 == 0
    
def check_number(answer):
    if isinstance(answer, (int, float)):  # Convert numbers to strings
        answer = str(answer)

    pattern = r"^10*$"  # Regular expression pattern
    match = re.match(pattern, answer)
    return bool(match)


checked_numbers = [1]
checked_numbers_times = [0]

i2 = 1
i = 1
times = 0

print('To which number would you like to go to?')
number = input(">")
while not check_number(number):
    print(color.BOLD + "Wrong person!!!")
    time.sleep(0.5) 
number = int(number)


def full_text():
    global checked_numbers
    global checked_numbers_times
    global i2
    global i
    global times
    
    #print(color.BOLD + color.dark.BLUE + f'Get ({i})' + color.END)
    
    while i2 <= number:
        if i == 1:
            checked_numbers.append(i2)
            checked_numbers_times.append(times)
            print(color.BOLD + color.light.GREEN + f'✓ ({times})' + color.END)
            print('')
            i2 += 1
            i = i2
            times = 0
            print(color.BOLD + color.dark.BLUE + f'Get ({i})' + color.END)
        else:
            times = times + 1
            if is_even(i): 
                i = i / 2
            else:
                i = i * 3 + 1
            print(math.floor(i))


def light_text():
    global checked_numbers
    global checked_numbers_times
    global i2
    global i
    global times
    
    print(color.BOLD + color.dark.BLUE + f'Get ({i})' + color.END)
    
    while i2 <= number:
        if i in checked_numbers:
            index = checked_numbers.index(i)
            times += checked_numbers_times[index]
            checked_numbers.append(i2)
            checked_numbers_times.append(times)
            print(color.BOLD + color.light.GREEN + f'✓ ({times})' + color.END)
            print('')
            i2 += 1
            i = i2
            times = 0
            print(color.BOLD + color.dark.BLUE + f'Get ({i})' + color.END)
        else:
            times = times + 1
            if is_even(i): 
                i = i / 2
            else:
                i = i * 3 + 1
            print(math.floor(i))

   
def no_text():
    global checked_numbers
    global checked_numbers_times
    global i2
    global i
    global times
    
    #print(color.BOLD + color.dark.BLUE + f'Get ({i})' + color.END)
    
    while i2 <= number:
        if i in checked_numbers:
            index = checked_numbers.index(i)
            times += checked_numbers_times[index]
            checked_numbers.append(i2)
            checked_numbers_times.append(times)
            #print(color.BOLD + color.light.GREEN + f'✓ ({times})' + color.END)
            #print('')
            i2 += 1
            i = i2
            times = 0
            #print(color.BOLD + color.dark.BLUE + f'Get ({i})' + color.END)
        else:
            times = times + 1
            if is_even(i): 
                i = i / 2
            else:
                i = i * 3 + 1
            #print(math.floor(i))
    
full_text()
end_time = time.time()
execution_time = end_time - start_time

data = checked_numbers_times
bindex = data.index(max(data))
bi = checked_numbers[bindex]
bt = checked_numbers_times[bindex]
print(color.light.RED + f'The number with the largest steps is number {bi} who had {bt} steps.')
print(f'It took the computer {execution_time} seconds to find it.')
print(checked_numbers)
print(checked_numbers_times)
