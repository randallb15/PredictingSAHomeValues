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