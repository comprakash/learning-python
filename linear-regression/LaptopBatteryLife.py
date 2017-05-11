import numpy as np
from sklearn import linear_model
import csv
import sys
import datetime

laptop_charge_time = []
laptop_battery_lasted_time = []
file = "laptop-battery-life-trainingdata.txt"
try:
    for key, value in csv.reader(open(file)):
        # Analyzing the data reveals that charging the laptop more than 4 hours has no effect on the battery last time.
        # The maximum battery last time is 8 hours. Hence they are excluded from the training set
        if float(key) <= 4:
            laptop_charge_time.append([float(key)])
            laptop_battery_lasted_time.append(float(value))
except:
    # If file is not present exit program
    print(datetime.datetime.now().isoformat(), "-",
          "Error - Unexpected error while reading the training date file - ", file, ", Exception Details :", sys.exc_info())
    sys.exit(1)

X = np.array(laptop_charge_time)
Y = np.array(laptop_battery_lasted_time)

model = linear_model.LinearRegression()

model.fit(X, Y)

current_laptop_charge_time = 3.42

if current_laptop_charge_time <= 4:
    print("For laptop_charge_time =", current_laptop_charge_time, ", the Predicted Battery Lasting Time =",
          round(model.predict(np.array([current_laptop_charge_time]).reshape(1, -1))[0], 2))
else:
    print("For laptop_charge_time =", current_laptop_charge_time, ", the Predicted Battery Lasting Time =", round(8.0, 2))
