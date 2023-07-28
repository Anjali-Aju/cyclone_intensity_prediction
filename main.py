from flask import Flask,render_template,request,url_for,jsonify
import util
import pandas as pd

app=Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict_cyclone_intensity',methods=['GET','POST'])
def predict_cyclone_intensity():
    if request.method=='POST':
        value=[]
        for row in range(3,-1,-1):
            lat = int(request.form[f'latitude{row}'])
            long = int(request.form[f'longitude{row}'])
            ws = int(request.form[f'windSpeed{row}'])
            value_row = [lat,long,ws]
            value.append(value_row)
        dataframe = pd.DataFrame(value, columns=['latitude', 'longitude', 'windspeed'])  
        print(dataframe)
        response = util.get_predicted_intensity(dataframe)
        res=response[0][0]
        return render_template('home.html',r=res)
    return render_template('home.html')



if __name__=="__main__":
    print("Starting Python Flask Server For Cyclone Intensity Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)