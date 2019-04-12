import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high, and low temperatures from file.
filename1 = '北京2018年天气数据.csv'
filename2 = '大连2018年天气数据.csv'
with open(filename1) as f1, open(filename2) as f2:
    reader = csv.reader(f1)
    header_row = next(reader)

    dates1, highs1, lows1 = [], [], []
    for row in reader:
        try:
            current_date1 = datetime.strptime(row[2], "%Y/%m/%d")
            high1 = int(row[5])
            low1 = int(row[8])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates1.append(current_date1)
            highs1.append(high1)
            lows1.append(low1)
            
    reader = csv.reader(f2)
    header_row = next(reader)

    dates2, highs2, lows2 = [], [], []
    for row in reader:
        try:
            current_date2 = datetime.strptime(row[2], "%Y/%m/%d")
            high2 = int(row[5])
            low2 = int(row[8])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates2.append(current_date2)
            highs2.append(high2)
            lows2.append(low2)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates1, highs1, c='red', alpha=0.5)
plt.plot(dates1, lows1, c='red', alpha=0.5)
plt.fill_between(dates1, highs1, lows1, facecolor='magenta', alpha=0.1)

# Plot data.
plt.plot(dates2, highs2, c='blue', alpha=0.5)
plt.plot(dates2, lows2, c='blue', alpha=0.5)
plt.fill_between(dates2, highs2, lows2, facecolor='cyan', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nBeijing and Shanghai"
plt.title(title, fontsize=20)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('weather.png')

'''
#Another simple method
def get_weather_data(filename, dates, highs, lows):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y/%m/%d")
                high = int(row[5])
                low = int(row[8])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

dates, highs, lows = [], [], []
get_weather_data('北京2018年天气数据.csv', dates, highs, lows)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='red', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='magenta', alpha=0.15)

dates, highs, lows = [], [], []
get_weather_data('大连2018年天气数据.csv', dates, highs, lows)

plt.plot(dates, highs, c='blue', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='cyan', alpha=0.05)

title = "Daily high and low temperatures - 2018\nBeijing and Shanghai"
plt.title(title, fontsize=20)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('weather.png')
'''