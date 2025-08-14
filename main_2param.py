"""
Instead of following the line of best fit, this code explores all possible options of m and b

M and B are a list of numbers defined by a start stop and step variable
"""
import matplotlib.pyplot as plt
import numpy as np

X_test = np.array([13])
X_train = np.array([3, 4, 4.5, 5,  6,  14,  17,  19,  21])
y_train = np.array([6, 8, 9,  10, 12, 28,  34,  38,  42])

#m = np.linspace(1,4,4)
#b = np.linspace(1,4,4)
# calculate that (|-5| + |5.5|)*0.5

# make different ranges for m and b to see differences
start_m = -5
start_b = -5
stop_m = 5.5
stop_b = 5.5
# different step for m and different step for b
step_m = 0.5
step_b = 0.5

distance_m = int((abs(start_m) + abs(stop_m)) / step_m)
distance_b = int((abs(start_b) + abs(stop_b)) / step_b)


mse_array = np.zeros([distance_m,distance_b]) 

rangeGuesses_m = np.arange(start_m,stop_m,step_m) # the possible values of m and b
rangeGuesses_b = np.arange(start_b,stop_b,step_b)
#print(mse_array)

counter_m = 0
for m in rangeGuesses_m:
    counter_b = 0
    for b in rangeGuesses_b:
        # print(m,b)
        yhat = m * X_train + b # this is the output that the machine learning algorithm thinks
        mse = np.mean((yhat - y_train)**2)
        mse_array[counter_m, counter_b] = mse
        # print(f"m: {m:7.2f}    b: {b:7.2f}    MSE: {mse:7.2f}")
        counter_b += 1
    counter_m += 1

# shows the location of the best m and best b (the best answer)
# finds the best answer when mse array is equal to the smallest number in mse array
# mse_array == np.min(mse_array) creates a mask (only has true and false values) 
# with dimensions that are equal to those of the mse array
# np.argwhere returns all the locations of the true values in the mask
minErrorLoc = np.argwhere(mse_array == np.min(mse_array)) # the location of the minimum error (value of mse_array)

plt.pcolormesh(mse_array)
plt.colorbar()
plt.ylabel("m")
plt.xlabel("b")
plt.title("mse array")
answer_m = rangeGuesses_m[minErrorLoc[0][0]]
answer_b = rangeGuesses_b[minErrorLoc[0][1]]
print(answer_m)
print(answer_b)
