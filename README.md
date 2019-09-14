# s3-payment-analytics
Proof Of Concept for Payment Analytics including forecasting


# Forecast_API using prophet
api.py


#Dataframes used-

##path to the dataset-'E:\Forecast_Api\forecasting-prj-sample-data-v0.1.csv'

## holidays- used as the parameter 'holidays' in the profit model. This is a self created dataframe which 
includes the public holidays for the year 2020.


#consists of 5 sections. 

## "/adult_dataframe"-shows the record of adult occupancy in the form of dataframe with columns 'Date' and 'Occupancy Adults'


##"/children_dataframe"- shows the record of children occupancy in form of dataframe with columns 'Date' and 'Occupancy Children'


##"/trends"- shows the trend observed in the used dataset, in the form of graphs('Date' vs 'Occupancy')


##"/adult_prediction"- uses prophet model for prediction. adult occupancy dataframe fit to the model.
shows the prediction on daily, monthly and yearly basis in the form of plots


##"/children_occupancy"- uses prophet model for prediction fit to the children occupancy record and shows the prediction on daily,
monthly and yearly basis in the form of plots




# to clone the api-

##  go to command prompt and Change the current working directory to the location where you want the cloned directory to be made.

##  $ git clone https://github.com/S3Infosoft/s3-payment-analytics


# to run the api-

##go to command prompt- change the current directory to the location where you cloned the repository

## $python api.py


# links:-
main-				                  http://127.0.0.1:5000/
adult_dataframe-		          http://127.0.0.1:5000/adult_dataframe
children record-		          http://127.0.0.1:5000/children_dataframe
observed trend-			          http://127.0.0.1:5000/trends
predicted adult occupancy-	  http://127.0.0.1:5000/adult_prediction
predicted children occupancy-	http://127.0.0.1:5000/children_occupancy


