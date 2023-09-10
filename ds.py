"""Python script to read csv file, 
    generate statistics summary 
        and plot interested columns """
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read csv file "world-small.csv"
data = pd.read_csv("world-small.csv")
# convert "gdppcap08" column to integer
data["gdppcap08"] = data["gdppcap08"].astype("int")
# print out statistics summary of "gdppcap08" & "polityIV"
print(data[["gdppcap08", "polityIV"]].describe())

# scatter plot of "gdpcap08" as x & "polityIV" as y
data.plot.scatter(x="gdppcap08", y="polityIV", alpha=0.5)
plt.show()
plt.savefig('plot.png')