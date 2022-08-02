# Import all of the necessary dependencies
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

def initialzie_and_clean():
    '''Import and format the sample dataset
        
        Import the sample dataset from the CSV located at the root level
        and check that each of the column datatypes are in the correct format
        
        Args:
            no arguments
            
        Returns:
            The data frame imported from the CSV
        
        Throws:
            FileNotFoundError if the path to the dataset is incorrect
    '''
    # Import the sample dataset csv 
    df = pd.read_csv('./SampleDataset.csv')
    
    # Change column the datatypes
    df['dirtied_datetime'] = pd.to_datetime(df['dirtied_datetime'])
    df['cleaned_datetime'] = pd.to_datetime(df['cleaned_datetime'])
    df['sensor_id'] = df['sensor_id'].astype('int')
    df['sensor_alias'] = df['sensor_alias'].astype('string')
    
    # print the datatype for each column
    # print(df.dtypes)
    
    # Return the dataframe
    return df

def average_response_time(df):
    '''Calculate the average response time per table

        Args:
            df: the dataframe to run calculations on
            
        Returns:
            void
    '''
    # Create a column for the response time
    df['response_time'] = df['cleaned_datetime'] - df['dirtied_datetime']
    # Convert the response time column into minutes
    df['response_time'] = df['response_time'].astype('timedelta64[m]').astype(int)
    df = df.sort_values('sensor_alias')
    
    # Get the subarrays from the dataframe to graph
    names = df['sensor_alias'].unique()
    avg_response = np.zeros(len(names))
    for i in range(len(avg_response)):
        avg_response[i] = df.loc[df['sensor_alias']  == names[i]]['response_time'].mean() 
    
    # Create a bar graph
    plt.bar(names, avg_response, width=.4)
    
    # Add the average response time label for each bar
    for i in range(len(names)):
        plt.text(i, avg_response[i], round(avg_response[i], 2), ha = 'center',
                bbox = dict(facecolor = 'white', alpha = 0.8))

    # Add all of the decorative pieces to the graph
    plt.xlabel('Table at Restaurant')
    plt.xticks(rotation=30)
    plt.ylabel('Average Response Time (minutes)')
    plt.yticks(np.linspace(1., 13., 10))
    plt.title('Average Sanitization Response Time per Table')
    # Show the graph
    plt.show()
    
    
def run():
    # Initialize and store the dataframe in the variable df
    df = initialzie_and_clean()
    # Produce first visual
    average_response_time(df)

if __name__ == "__main__":
    run()