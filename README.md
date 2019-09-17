# s3-payment-analytics
Proof Of Concept for Payment Analytics including forecasting

# Clone the repo

##  $ git clone https://github.com/S3Infosoft/s3-payment-analytics

# Install dependencies in requirements and execute the following

## python api.py

## Docker Build 
``` docker build -t s3-payment-analytics:latest . ```

## Docker Run
``` docker run --rm -p 5000:5000 -d --name s3infosoft s3-payment-analytics:latest ```

# APIs
### main
#### http://127.0.0.1:5000/

### adult_dataframe
#### http://127.0.0.1:5000/adult_dataframe

### children record
#### http://127.0.0.1:5000/children_dataframe

### observed trend
#### http://127.0.0.1:5000/trends

### predicted adult occupancy
#### http://127.0.0.1:5000/adult_prediction

### predicted children occupancy
#### http://127.0.0.1:5000/children_occupancy
