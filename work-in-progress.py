import time
import math

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



checked_numbers = [1, 2, 4]
checked_numbers_times = [0, 1, 2]

i2 = 1
i = 1
times = 0
#print(color.BOLD + color.dark.BLUE + f'Get ({i})' + color.END)

while i2 <= 100000:
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

