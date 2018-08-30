#retrieve system variables
import sys
#import plotting
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

#parse inputs, filename should be at index 1
file_list = sys.argv[1:]

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows

# read data into a pandas dataframe and transpose
#filename = 'gapminder_gdp_oceania.csv'
for filename in file_list:
    data = pandas.read_csv(filename, index_col = 'country').T

    # create a plot the transposed data
    ax = data.plot(title=filename)

    #axes labels
    ax.set_xlabel('Year')
    ax.set_ylabel('GDP Per Capita')

    #set axes ticks
    ax.set_xticks(range(len(data.index)))
    ax.set_xticklabels(data.index, rotation=45)

    # display the plot
    plt.show()
