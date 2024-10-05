import pandas as pd #type: ignore
import matplotlib.pyplot as plt #type: ignore
from scipy.stats import linregress #type: ignore

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,8))
    scatter = df.plot(kind="scatter",x="Year",y=df.columns[1],ax=ax,color="blue",label=df.columns[1])

    # Create first line of best fit
    slope1, intercept1, *rest = linregress(x=df.iloc[:,0],y=df.iloc[:,1])
    yearRange1 = range(df.Year[0],2051)
    plt.plot(yearRange1,slope1*yearRange1+intercept1, color="green",label="Fitted from 1880")

    # Create second line of best fit
    ## .index returns a list of all indexes which fullfill the criteria
    indexOfYear2000 = df.loc[df.Year==2000].index[0]
    slope2, intercept2, *rest = linregress(x=df.iloc[indexOfYear2000:,0],y=df.iloc[indexOfYear2000:,1])
    yearRange2 = range(df.Year[indexOfYear2000],2051)
    plt.plot(yearRange2,slope2*yearRange2+intercept2, color="red",linestyle="--",label="Fitted from 2000")

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    plt.grid(True)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()