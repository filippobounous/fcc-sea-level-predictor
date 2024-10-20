import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051)
    sea_level_pred = intercept + slope * years_extended
    
    plt.plot(years_extended, sea_level_pred)

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]

    slope_2, intercept_2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended_2 = np.arange(df_recent['Year'].min(), 2051)
    sea_level_pred_2 = intercept_2 + slope_2 * years_extended_2
    
    plt.plot(years_extended_2, sea_level_pred_2)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()