# EGR122 - FinalProject
Source code for Engineering Design Summer 2022 Final Project.

Summer Semester 2022
Professor Napisa
EGR122

## Team Members
- Blake Marterella
- Elias AlJariri
- Evan Fillmore
- Gabriel-Marie Chapman
- Mohamed Medani

# How to run...
## Install Dependencies
Firstly, if Python 3.9 is not installed on your machine, go to [Python's Official Website](python.org/downloads/release/python-3913/) to download it.

Once python is installed on your machine, install the project's dependencies
```shell
# Install the pip project dependencies 
pip3 install -r requirements.txt
```

## Running the program
```shell
# Run the python script
python main.py
```

By default, the program will automatically generate all 3 graphs. To isolate a graph, comment out methods in the main functions.

Shown below is the main (run) function. In the sample code provided, I commented out every function except for the function that generates the busiest days graph.
```shell
def run():
    # Initialize and store the dataframe in the variable df. MUST INCLUDE!
    df = initialzie_and_clean()
    
    # Produce average response visual
    # average_response_time(df)
    
    # Produce the busiest hours visual
    busiest_hours(df)
    
    # Produce the busiest days visual
    # busiest_days(df)
```