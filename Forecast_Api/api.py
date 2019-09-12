from flask import Flask,render_template,url_for,session,request,make_response,send_file

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas  import DataFrame,read_csv
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
from fbprophet import Prophet

festivals=pd.DataFrame({
    'holiday':(['New Year Day', 'Guru Govind Singh Birthday',
'Makar Sankranti',
'Pongal',
'Republic Day',
'Basant Panchami',
'Guru Ravidas Birthday',
'Shivaji Jayanti',
'Swami Dayananda Saraswati Jayanti',
'Maha Shivaratri/Shivaratri',
'Hazarat Ali Birthday',
'Holika Dahana',
'Holi',
'Chaitra Sukladi/Gudi Padava/Ugadi/Cheti Chand',
'Rama Navami',
'Mahavir Jayanti',
'Good Friday',
'Easter Day',
'Mesadi',
'Vaisakhi/Vishu',
'Vaisakhadi(Bengal)/Bahag Bihu (Assam)',
'Guru Rabindranath birthday',
'Buddha Purnima',
'Jamat Ul-Vida',
'Idul Fitr',
'Rath Yatra',
'Id-ul-Zuha(Bakrid)',
'Independence Day',
'Raksha Bandhan (Rakhi)',
'Parsi New Year day',
'Janmashtarni',
'Onam',
'Muharram',
'Ganesh Chaturthi',
'Mahatma Gandhi Jayanti',
'Dussehra',
'Maharishi Valmiki Birthday',
'Karaka Chaturthi (Karva Chouth)',
'Naraka Chaturdasi',
'Diwali (Deepavali)',
'Govardhan Puja',
'Bhai Duj',
'Chhat Puja',
'Milad-un-Nabi or Id-e- Milad',
'Guru Nanaks Birthday',
'Guru Teg Bahadur Martyrdom Day',
'Christmas Eve',
'Christmas Day',
'New Year Day',
'Guru Gobind Singh Jayanti',
'Lohri',
'Pongal, Uttarayan, Makar Sankranti',
'Republic Day',
'Vasant Panchami',
'Guru Ravidas Jayanti',
'Maharishi Dayanand Saraswati Jayanti',
'Mahashivratri',
'Holika Dahan',
'Holi',
'Ugadi, Gudi Padwa',
'Bank Holiday',
'Ram Navami',
'Mahavir Jayanti',
'Good Friday',
'Easter',
'Baisakhi',
'Budh Purnima, Rabindranath Tagore Jayanti',
'Eid-al-Fitr / Ramadan',
'Jagannath Rath Yatra',
'Guru Purnima',
'Hariyali Teej',
'Bakrid',
'Raksha Bandhan',
'Janmashtami',
'Independence Day',
'Ganesha Chaturthi',
'Muharram',
'Onam',
'Gandhi Jayanti',
'Dussehra',
'Id-e-Milad',
'Valmiki Jayanti',
'Karva Chauth',
'Dhanteras',
'Diwali, Narak Chaturdashi, Children’s day',
'Govardhan Puja',
'Bhai Dooj',
'Chhath Puja',
'Guru Nanak Birthday',
'Christmas'
 
]),
'ds':([
'Jan-1-2019',
'Jan-13-2019',
'Jan-14-2019',
'Jan-15-2019',
    
'Jan-26-2019',
'Feb-10-2019',
'Feb-19-2019',
'Feb-19-2019',
'Mar-1-2019',
'Mar-4-2019',
'Mar-19-2019',
'Mar-20-2019',
'Mar-21-2019',
    
'Apr-6-2019',
'Apr-13-2019',
'Apr-17-2019',
'Apr-19-2019',
'Apr-21-2019',
'Apr-13-2019',
'Apr-14-2019',
'Apr-14-2019',
'May-9-2019',
'May-18-2019',
'May-31-2019',
'Jun-5-2019',
'Jul-4-2019',
'Aug-12-2019',
'Aug-15-2019',
    'Aug-15-2019',
'Aug-17-2019',
'Aug-24-2019',
'Sep-11-2019',
'Sep-10-2019',
'Sep-2-2019',
'Oct-2-2019',
'Oct-7-2019',
'Oct-13-2019',
'Oct-17-2019',
'Oct-27-2019',
'Oct-27-2019',
'Oct-28-2019',
'Oct-29-2019',
'Nov-2-2019',
'Nov-10-2019',
'Nov-12-2019',
'Nov-24-2019',
'Dec-24-2019',
'Dec-25-2019',
'Jan-1-2020',
'Jan-2-2020',
'Jan-14-2020',
'Jan-15-2020',
'Jan-26-2020',
'Jan-29-2020',
    
'Feb-9-2020',
'Feb-18-2020',
'Feb-21-2020',
'Mar-9-2020',
'Mar-10-2020',

'Mar-25-2020',
'Apr-1-2020',
'Apr-2-2020',
'Apr-6-2020',
'Apr-10-2020',
'Apr-12-2020',
'Apr-13-2020', 
'May-7-2020', 
'May-24-2020', 
'Jun-23-2020', 
'Jul-5-2020', 
'Jul-23-2020', 
'Jul-31-2020',
'Aug-3-2020', 
'Aug-11-2020',
'Aug-15-2020',
'Aug-22-2020',
    'Aug-23-2020',
'Aug-29-2020', 
'Aug-31-2020', 
'Oct-2-2020', 
'Oct-25-2020',
'Oct-29-2020',
'Oct-31-2020',
    'Nov-4-2020',
    'Nov-12-2020',
'Nov-14-2020', 
'Nov-15-2020',
'Nov-16-2020',
 
'Nov-30-2020', 
'Dec-25-2020'])
    
    
    
})



holidays=festivals.filter(['holiday','ds'])
holidays['ds']=pd.to_datetime(festivals['ds'])




file=r'E:\Forecast_Api\forecasting-prj-sample-data-v0.1.csv'
df=pd.read_csv(file)
df.to_html(header="true",table_id="table")

app=Flask(__name__)


app.config['SECRET_KEY']='f2091f20a36545a4ffe6ef38439845f5'


frame1=df.filter(['Date','Occupancy Adults'])
frame1['Date']=pd.to_datetime(df['Date'])
frame1=frame1.set_index('Date')

f_frame1=frame1.reset_index().dropna()
f_frame1.to_html(header="true",table_id="table")


@app.route("/")
@app.route("/adult_dataframe",methods=["POST","GET"])
def html_table():
    return render_template('adult_table.html',tables=[f_frame1.to_html(classes='data',header="true")])
    



frame2=df.filter(['Date','Occupancy Children'])
frame2['Date']=pd.to_datetime(df['Date'])
frame2=frame2.set_index('Date')

f_frame2=frame2.reset_index().dropna()
f_frame2.to_html(header="true",table_id="table")


@app.route("/children_dataframe",methods=["POST","GET"])
def child_table():
      return render_template('children_table.html',tables=[f_frame2.to_html(classes='data',header="true")])
 

@app.route("/trends",methods=["GET"])
def plot_png():
    fig=create_figure()
    output=io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(),mimetype='image/png')


def create_figure():
    fig=Figure(figsize=(25,20))
    
    axis=fig.add_subplot(2,1,1)
    xs=f_frame1['Date']
    ys=f_frame1['Occupancy Adults']

    axis.plot(xs,ys)
    axis.set_title('Adult occupancy')
    axis.set_xlabel('Date')
    axis.set_ylabel('Adults')
    axis=fig.add_subplot(2,1,2)
    xs=f_frame2['Date']
    ys=f_frame2['Occupancy Children']

    axis.plot(xs,ys)
    axis.set_title('Children occupancy')
    axis.set_xlabel('Date')
    axis.set_ylabel('Children')
    return fig


def chartTest():
    return render_template('plot.html',name=plt.show(),name2=model.plot_components(forecast))





prophetframe1=df.filter(['Date','Occupancy Adults'])
prophetframe1['Date']=pd.to_datetime(df['Date'])
prophetframe1=prophetframe1.set_index('Date')

prophet_frame1=prophetframe1.reset_index().dropna()
prophet_frame1.columns=['ds','y']

model=Prophet(yearly_seasonality=True,weekly_seasonality=True,holidays=holidays)
model.fit(prophet_frame1)
future1=model.make_future_dataframe(periods=36,freq='MS')
forecast=model.predict(future1)





@app.route("/adult_prediction",methods=["GET"])
def predict_adult():
     fig=create_adults()
     output=io.BytesIO()
     FigureCanvas(fig).print_png(output)
     return Response(output.getvalue(),mimetype='image/png')
     


def create_adults():
    fig=Figure(figsize=(25,20))
    fig=model.plot_components(forecast)
    return fig

def show_prophet():
    return render_template('adult_prophetgraph.html',name=model.plot_components(forecast))
 




prophetframe2=df.filter(['Date','Occupancy Children'])
prophetframe2['Date']=pd.to_datetime(df['Date'])
prophetframe2=prophetframe2.set_index('Date')
prophet_frame2=prophetframe2.reset_index().dropna()
prophet_frame2.columns=['ds','y']



model2=Prophet(yearly_seasonality=True,weekly_seasonality=True,daily_seasonality=True,holidays=holidays)
model2.fit(prophet_frame2)
future2=model2.make_future_dataframe(periods=36,freq='MS')
forecast2=model.predict(future2)




@app.route("/children_occupancy")
def predict_children():
     fig=create_children()
     output=io.BytesIO()
     FigureCanvas(fig).print_png(output)
     return Response(output.getvalue(),mimetype='image/png')
     


def create_children():
    fig=Figure(figsize=(25,20))
    fig=model2.plot_components(forecast2)
    return fig

def show_prophetchild():
    return render_template('children_prophetgraph.html',name=model2.plot_components(forecast2))



if __name__=='__main__':
    app.run(debug=True)
