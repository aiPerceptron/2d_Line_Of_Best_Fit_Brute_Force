"""
Instead of following the line of best fit, this code explores all possible options of M

M are a list of numbers defined by a start stop and step variable

There is no B here.
"""
m_array = []
MSE_array = []

X_train = np.array([1,2,3,4,5])
y_train = np.array([4,8,12,16,20])

start = -7
stop = 7.5
step = 0.5

rangeGuesses = np.arange(start,stop,step)

for m in rangeGuesses:
    m_array.append(m)
    squared_error = 0
    
    for i in range(len(X_train)):
        yhat = m * X_train[i] # this is the output that the machine learning algorithm thinks
        error = (yhat - y_train[i])**2
        
        # gradient = (yhat - y_train[i])*X_train[i]
        squared_error += error

    mean_squared_error = squared_error / len(X_train)
    MSE_array.append(mean_squared_error)
        

# make a graph of m  and squared error and verify your calculations
plt.plot(m_array,MSE_array)
plt.ylabel("MSE")
plt.xlabel("choices of slope m")
plt.title("graphing selected options of M and how good they are for multiplication")
