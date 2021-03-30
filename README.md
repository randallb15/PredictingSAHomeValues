# Predicting Home Values in San Antonio, TX

### Background

Predicting home values is a difficult process.  A home value is really based on what someone will pay for the house which makes things difficult.  People are different and often have different tastes, opinions, and priorities as well as different budgets, risk tolerances, and financial goals.  Local tax jurisdictions assess the value of homes but those values do not often line up with what the homes sell for.  With all of this in mind, we see that predicting a home value is an imperfect process.

However, there are numerous services out there that can get pretty close.  Zillow has a "Zestimate" prediction which boasts a high accuracy of predicted value versus sale price.  According to their website (https://www.zillow.com/z/zestimate/), they have a median error of 1.6% and 87.9% of homes sold have a Zestimate within 5% of the final sale price.  Redfin and Realtor.com also have their own ways of predicting home values.  

This project will use various machine learning techniques to attempt to come up with a home value estimator that is comparable to these services.  Because of the time constraint, it will not be able to be used on current for-sale houses, but it will be used on past data to compare predictions to actual sale prices. 

### The Data

The data was compiled from redfin.com.  It includes sold houses in the San Antonio metro area as well as some surrounding neighborhoods.  It includes 3 years of sold house data.  

#### Features

The features that are automatically pulled when downloading data from redfin are:
1.   SALE TYPE                                                                                   
2.   SOLD DATE                                                                                   
3.   PROPERTY TYPE                                                                               
4.   ADDRESS                                                                                     
5.   CITY                                                                                        
6.   STATE OR PROVINCE                                                                           
7.   ZIP OR POSTAL CODE                                                                          
8.   PRICE                                                                                       
9.   BEDS                                                                                        
10.   BATHS                                                                                       
11.  LOCATION                                                                                    
12.  SQUARE FEET                                                                                 
13.  LOT SIZE                                                                                    
14.  YEAR BUILT                                                                                  
15.  DAYS ON MARKET                                                                              
16.  USD/SQUARE FEET                                                                               
17.  HOA/MONTH                                                                                   
18.  STATUS                                                                                      
19.  NEXT OPEN HOUSE START TIME                                                                  
20.  NEXT OPEN HOUSE END TIME                                                                    
21.  URL (SEE http://www.redfin.com/buy-a-home/comparative-market-analysis FOR INFO ON PRICING)  
22.  SOURCE                                                                                      
23.  MLS#                                                                                        
24.  FAVORITE                                                                                    
25.  INTERESTED                                                                                  
26.  LATITUDE                                                                                    
27.  LONGITUDE 

#### Cleaning

Upon initial inspection, there were several columns that immediately could be dropped (SALE TYPE, PROPERTY TYPE, CITY, STATE OR PROVINCE, STATUS, NEXT OPEN HOUSE START TIME, NEXT OPEN HOUSE END TIME, URL, SOURCE, MLS #, FAVORITE, INTERESTED).  This left the data with 15 primary features that would be more closely inspected.
                                                                                 
2.   SOLD DATE                                                                              
4.   ADDRESS                                                                                     
7.   ZIP OR POSTAL CODE                                                                          
8.   PRICE                                                                                       
9.   BEDS                                                                                        
10.   BATHS                                                                                       
11.  LOCATION                                                                                    
12.  SQUARE FEET                                                                                 
13.  LOT SIZE                                                                                    
14.  YEAR BUILT                                                                                  
15.  DAYS ON MARKET                                                                              
16.  USD/SQUARE FEET                                                                               
17.  HOA/MONTH                                                                                 
26.  LATITUDE                                                                                    
27.  LONGITUDE 

The initial goal of the project was to look at days on the market and predict the price that would allow you to sell your house within 30 or 60 days.  However, when looking at the 'DAYS ON MARKET' column in the data, it appeared that this data was incorrect and could not be used.  The 'DAYS ON MARKET' number was actually just the number of days between the 'SOLD DATE' and the date the data was downloaded (see graph below for visual).  Therefore, this column was dropped.

![DAYS ON MARKET plot](img/soldplot.png)

#### Correlations

It was important to look at which of these features may be highly correlated and therefore should be combined or taken out.  Some of the largest correlations are shown below:

|             |      PRICE |       BEDS |      BATHS |   SQUARE FEET |
|:------------|-----------:|-----------:|-----------:|--------------:|
| PRICE       | nan        | nan        |   0.615053 |      0.744923 |
| BEDS        | nan        | nan        |   0.61592  |      0.667653 |
| BATHS       |   0.615053 |   0.61592  | nan        |      0.792935 |
| SQUARE FEET |   0.744923 |   0.667653 |   0.792935 |    nan        |

Since beds and baths are highly correlated, and baths and square feet are highly correlated, I wanted to combine them all into one feature.  To do this, I made a feature called 'ROOMS PER SQFT * 1000'.  This added the number of bedrooms and bathrooms and divided by the total number of square feet.  In order to get a number that is more easily comparab

















### Future Work

1. Deploy model on AWS with inputs to predict home value
2. Use geocoder to turn address into LAT/LONG for model
3. Use h2o.ai random forest regressor to better handle categorical variables, specifically neighborhood





-----

# Sell Your Home In 30 Days
#### San Antonio, TX edition

Selling a home can be a daunting process.  People need to juggle selling their home for as much as they can get for it, with waiting for the right home buyer.  Many people have a timeline of how long they can wait to get the price they want.  This project attempts to find the price at which the seller should expect to sell their house if they want it sold within thirty days.  

This is an imperfect process and there are many factors that go into how long a house stays on the market.  Some factors that I expect to be important in predicting price and whether the house will sell in thirty days:
1. The time of year the house is being sold
2. The location of the house
3. The house size

There are also some things that will not be in the data that could potentially affect the home sale:
1. Pictures of the house
2. The condition of the house
3. Contingencies of the sale

## Exploratory Data Analysis

First things first, the data was explored to find out what is being worked with.  **Data Density**

#### Features in Original Data

The data was obtained from www.redfin.com and downloaded using a free user account.  This data does not represent the total number of houses sold but does represent over half of the houses sold. A distribution of houses across most of San Antonio was attempted, but there will be some areas that are not represented in the data.

### Correlations

The data was found to have some features that were highly correlated.  Sale Price is highly correlated with the number of baths and square feet and the square feet is highly correlated with sale price, the number of beds and the number of baths.

In order to deal with these correlations, a new feature was created.  This feature was 'the number of rooms per sqft (multiplied by 1000)'.  This was created by adding the number of bedrooms and bathrooms and dividing by the total number of square feet.  It was found that this metric was 99.9% correlated with the price per square foot number.  This makes a lot of sense because as the number of beds goes up, the price should go up.  And as it is all normalized by square foot, it should be even more correlated.

### Neighborhoods

There were a lot of different neighborhoods or locations in the 'LOCATION' column.  Location is not very specific, so there were over 2000 different entries in the dataset.  In order to get something more manageable, I filtered by the 'location' where the sale date was over 100.  That means that houses were sold in that area over 100 different days in the last three years.  This narrowed the dataset down to 73 different 'locations'.

#### One-hot-encoding Neighborhoods

### Sold Date

Used datetime feature to separate out month and year from data

## Model

Initial Random Forest Classifier Model

### Special Considerations

- Stratified K Fold to take into consideration the imbalanced dataset
- 

#### Plots of Important Features

See below for plots

## Building a Model

Model model model