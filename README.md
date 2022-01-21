# phase-5-project

## Outline of this repo
Contained in this repo I have  files I have
1. phase5_final : this is the notebook which has all the data code for this project
2. readme: this contains information on what is in this repo and how to go through it
3. phase5_pp: this is a power point presentation of this project
4. layout: This is the dayout for the dash dashboard
5. main: This is main file which pulls together the layoud and the process inputs to generate a final price prediction in the dashboard
6. process_inputs: This transforms the data inputted in the dashboard into a format readable by the model then predicts the price using the model
7. listings_december: data for listings in December
8. listings_november: data for listings in December

# Introduction

### I am an enterprising entrepreneur. I have developed a product for Airbnb. This product will (1) Increase Airbnbs client satisfaction, (2) increase Airbnb client sales, (3) increase Airbnb revenue.  

## The story
I started of as a young professional in London. I had a two bedroom flat. To generate some additional income I decided to rent one of the bedrooms. To register my room in airbnb the the process was more convoluted and complicated that i expencted. Then came the time where I was to decide the price i should list the room for. The advice from airbnb was the following:


#### *'What to charge? It’s up to you, but these tips could help you decide:'*

As a first time renter i had no Idea where to start. As a result, I thought that it would be a good idea to use data to reach some conclusion. 


## The business case
I found that airbnb share a lot of their data publically. I wanted to find a way to predict the market value of your said property per night. This is valuable for three main reasons. 

1. Increase Airbnbs client satisfaction - Users like me have do doubt had similar conundrums. I hope this will allow for users to have a better and easier experience while listing properties in Airbnb. 

2. Increase Airbnb client sales - Not being able to value your property is a serious problem. This has significant impacts on your ability to sell your product. Being able to accuratley price your product should incrase the clients revenue.

3. Increase Airbnb revenue - The more sales that happen on Airbnb the higher the Airbnb revenue. Accurate pricing will bring in customers who would have bought other products (hotel rooms etc) more sales for Airbnb customers will mean more revenue for Airbnb. 


## The Idea

I will build a model that will predict the price of Airbnb's. 

I will use this to build a dashboard so that people can input details about their property and for an estimate price to be generated.


# phase5_final
I found great and extensive data from Airbnb. 

I analysed this data and performed a lot of data manipulation to make sure that it is usabel for us. 

(House prices by borough of London)
![image](https://user-images.githubusercontent.com/59200380/150589901-2a732ebf-68a2-460b-8a6a-4fd6b2640199.png)


(House prices by room type)
![image](https://user-images.githubusercontent.com/59200380/150589911-be22d889-11b0-4932-9f85-7261dbad6b93.png)


We created an XGBoost model to predict the value of an airbnb property. 

We hyper tuned this model to find the ideal parameters. Below is a graph showing the accuracy of our model.

![image](https://user-images.githubusercontent.com/59200380/150589763-1ab74ce6-049f-4ab5-a431-c6f4f656f264.png)


We then saved this model and created a dashboard to predict the value of a new property. 

We used dash to create the dashboard. We had to manipulate the data that is inputted into the dashboard so that it is in the right format for the model. We then run the inputed data through our model and we thus generate a price which we display in our dashboard.

![image](https://user-images.githubusercontent.com/59200380/150589875-4d3be762-2957-4699-80f1-fd752b1f150b.png)



