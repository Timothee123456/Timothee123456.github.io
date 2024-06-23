# colours
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



# setting up the BME680

import bme680
import time

sensor = bme680.BME680()

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

# seting up the graph

import matplotlib.pyplot as plt
import numpy as np

# asking the times
MS = input('Do you want the time to be in seconds, minutes or hours (s, m, h)? ')
while (MS != 'm' and MS != 's' and MS != 'h'):
    MS = input('Do you want the time to be in seconds, minutes or hourss (s, m, h)? ')
if MS == 's':
    MS = 'seconds'
elif MS == 'm':
    MS = 'minutes'
else:
    MS = 'hours'
    
Range = int(input('Number of times the value is checked = '))
Time = int(input('Time between each check = '))
print('The total time will be of ' + str(Range * Time) + ' seconds or ' + str((Range * Time) / 60) + ' minutes')
answer = input('Are you okay with this (y, N)? ')
while (answer != 'y'):
    print('The total time will be of ' + str(Range * Time) + ' seconds or ' + str((Range * Time) / 60) + ' minutes')
    answer = input('Are you okay with this (y, N)? ')
    if answer == 'N':
        Range = int(input('Number of times the value is checked = '))
        Time = int(input('Time between each check = '))




xList = []
ytemperatureList = []
yhumidityList = []


# import the progress bar
from progress.bar import ChargingBar
bar = ChargingBar('Collecting data', max=Range)

for i in range(Range):
    bar.next()
    time.sleep(Time)
    I = int(i * Time)
    if sensor.get_sensor_data():
        temperature = "{0:.2f}".format(sensor.data.temperature)
        humidity = "{0:.2f}".format(sensor.data.humidity)
        # print(color.BOLD + str(I) + ": " + color.END + temperature + '°C, ' + humidity + '%RH')
        if MS == 'seconds':
            xList.append(I)
        elif MS == 'minutes':
            xList.append(I / 60)
        else:
            xList.append(I / 60 / 60)
        ytemperatureList.append(float(temperature))
        yhumidityList.append(float(humidity))
    # else:
        # print(color.BOLD + color.dark.RED + "Error: " + color.END + str(I))
        
bar.finish()
    

x = np.array(xList)
ytemperature = np.array(ytemperatureList)
yhumidity = np.array(yhumidityList)
# fonts
font = {'family':'serif','color':'green'}
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#plot 2:
plt.subplot(2, 1, 1)
plt.plot(x, ytemperature)
plt.title("Computer temperature", fontdict = font1)
plt.xlabel("Time (in " + MS + ")", fontdict = font2)
plt.ylabel("Degrees (in °C)", fontdict = font2)

#plot 2:
plt.subplot(2, 1, 2)
plt.plot(x, yhumidity)
plt.title("Computer humidity", fontdict = font1)
plt.xlabel("Time (in " + MS + ")", fontdict = font2)
plt.ylabel("Humidity (in %RH)", fontdict = font2)

plt.suptitle("Temperature & humidity", fontsize=30, fontdict = font)
plt.show()

