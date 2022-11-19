AMZN = [
    [129.479996,129.820007,133.270004,136.449997,126.82,128.550003,126.279999],
    [123.529999,124.660004,122.190002,118.540001,117.309998,113.779999,115.150002],
    [114.410004,118.010002,114.800003,113,115.879997,121.089996,120.949997],
    [120.300003,114.559998,113.669998,112.209999,112.900002,112.529999,106.900002],
    [113.790001,116.360001,115.07,115.25,119.32,119.82,120.599998],
    [115.660004,110.959999,103.410004,102.440002,96.790001,92.120003,89.300003],
    [90.980003,90.529999,89.980003,86.139999,96.629997,100.790001,98.489998,98.940002]
]

META = [
    [160.389999,162.059998,169.149994,168.960007,153.130005,151.470001,149.550003],
    [146.289993,148.020004,146.089996,142.119995,142.820007,140.410004,136.369995],
    [134.399994,141.610001,136.410004,135.679993,138.610001,140.279999,138.979996],
    [139.070007,133.449997,133.789993,128.539993,127.5,130.289993,126.760002],
    [134.039993,132.800003,133.229996,131.529999,130.009995,129.720001,137.509995],
    [129.820007,97.940002,99.199997,93.160004,95.199997,90.540001,88.910004],
    [90.790001,96.720001,96.470001,101.470001,111.870003,113.019997,114.220001,117.080002]
]

import statistics as stats
import math
import matplotlib.pyplot as plt

def stock_dev(lst,name):
    """Calculates standard deviation in META and AMZN stock

    Parameters
    ----------
    lst : list of stock data
        AMZN & META stock data
    name : str
        Name of stock

    Returns
    -------
    return stock_dev    

    """
    week_num = 0
    for week in lst:
        week_num += 1
        print(f"{name} Week {week_num} Standard deviation is {stats.pstdev(week)}")
    return stock_dev

#stock_dev(META, "META")
#stock_dev(AMZN, "AMZN")

# Formulas for: 
    # stdev = sqrt(variance)
    # variance = sumofsquareddifferences / (len)
    # squareddiff = mean - each element
    # mean = sum() / len()

def nonfunctional_stdev(lst,name):
    """Calculates standard deviation in META and AMZN stock

    Parameters
    ----------
    lst : list of stock data
        AMZN & META stock data
    name : str
        Name of stock

    Returns
    -------
    return new_list    

    """
    week_num = 0
    new_list = []
    for i in lst:
        week_num += 1
        mean = sum(i)/len(i)
        var = ([(var - mean) **2 for var in i ])
        var_mean = (sum(var) / len(i)) 
        stdev_lst = (var_mean ** .5)
        new_list.append(stdev_lst)
        print(f"{name}) Week {week_num} Standard deviation is {stdev_lst}")
    return (new_list)

Stdev_meta = (nonfunctional_stdev(META, "META"))
Stdev_amzn = (nonfunctional_stdev(AMZN, "AMZN"))


plt.xlabel('Week')
plt.ylabel("StDev by Week")
plt.title("AMZN and META Standard Deviations")
x1 = [i for i in range(1, len(Stdev_meta)+1)]
y1 = Stdev_meta
x2 = [i for i in range(1, len(Stdev_amzn)+1)]
y2 = Stdev_amzn
plt.plot(x1,y1, label = "META", color = 'red', linestyle = 'dashed')
plt.plot(x2,y2, label = "AMZN", color = 'blue', linestyle = 'dashed')
plt.legend()
plt.show()
