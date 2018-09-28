import matplotlib.pyplot as plt
import math
import numpy as np

xB_value = 0.000
xC_value = 0.000
yB_value = .9600
yC_value = 0.000
yC_over_xC = .3576
yA = .04
xB = np.empty(0)
xC = np.empty(0)
yB = np.empty(0)
yC = np.empty(0)
slope = 0.000
slope_values = np.empty([])

for j in range(0, 6, 1):
    xB = np.append(xB, xB_value)
    xC_value = j * .02
    xC = np.append(xC, xC_value)
    yC_value = round(.295 * xC_value, 4)
    yB_value = round(1 - yC_value - yA, 4)
    yB = np.append(yB, yB_value)
    yC = np.append(yC, yC_value)

print xB, xC, yB, yC

left_tie_bounds = [0, .12]
y_axis_values = np.empty(0)
y_tie_line_values = np.empty(0)
x_tie_line_values = np.empty(0)
y_tie_line = 0
x_tie_line = .96

print xB, xC, yB, yC

for i in range(int(left_tie_bounds[0]), int(left_tie_bounds[1]*1000), 1):
    y_axis_values = np.append(y_axis_values, float(i)/1000)
    y_tie_line = round(yC[1] + (y_axis_values[i] - xC[1]) * (yC[1] / xC[1]), 6)
    y_tie_line_values = np.append(y_tie_line_values, y_tie_line)
    x_tie_line = round(yB[1] + (y_axis_values[i] - xC[1]) * (-yC[1] / xC[1]), 6)
    x_tie_line_values = np.append(x_tie_line_values, x_tie_line)
    slope = round((-(y_axis_values[i]-y_tie_line_values[i]))/x_tie_line_values[i], 6)
    slope_values = np.append(slope_values, slope)
    print y_tie_line, x_tie_line, float(i)/1000, slope

print y_axis_values
print x_tie_line_values
print y_tie_line_values
print slope_values


def find_nearest(array, value):
    element = (np.abs(array-value)).argmin()
    return element
