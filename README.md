# List and description of Projects

## 1. Numpystats
Performing statistical analysis using numpy

Function cal() in module stats.py checks if the input list has 9 elemnts, if yes, it arranges the list in a numpy array 3x3 matrix and performs a statitical analysis(mean,variance,standard deviation, maximum, minimum, sum) of the elements in in matrix (row-wise, column-wise, flattened matrix), if not, throws a Value error.

The test cases are in the test.py file using "unittest" module. 

The inspiration was taken from the course project on freecodecamp.org 


## 2. Medical Data Analysis
In this project, we will visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. 
The dataset values were collected during medical examinations.

The inspiration was taken from the course project on freecodecamp.org 


## 3. Time Series Visualizer
In this project we will visualize time series data using a line chart, bar chart, and box plots.
We will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03.
The data visualizations will help understand the patterns in visits and identify yearly and monthly growth.

The inspiration was taken from the course project on freecodecamp.org 


## 4. Demographic Data Analyzer

Analyze demographic data using Pandas given a dataset of demographic data that was extracted from the 1994 Census database. Here is a sample of what the data looks like:

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |

Use Pandas to answer the following questions:
* How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (`race` column)
* What is the average age of men?
* What is the percentage of people who have a Bachelor's degree?
* What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
* What percentage of people without advanced education make more than 50K?
* What is the minimum number of hours a person works per week?
* What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
* What country has the highest percentage of people that earn >50K and what is that percentage?
* Identify the most popular occupation for those who earn >50K in India. 

Unit tests are written for you under `test.py`.

The inspiration was taken from the course project on freecodecamp.org 

