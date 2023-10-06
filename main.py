from flask import Flask,render_template
import  pandas  as pd

app=Flask(__name__)

data=df=pd.read_csv("data/stations.txt",skiprows=17)

@app.route("/")
def home():
    return render_template("home.html",data=data.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    filename="data/TG_STAID"+str(station).zfill(6)+".txt"
    df1=pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    temp =df.loc[df1["    DATE"]==date]["   TG"].squeeze()/10
    return {"station":station,"date":date,"temperature":temp}

@app.route("/api/v1/<station>")
def all_data(station):
    filename="data/TG_STAID"+str(station).zfill(6)+".txt"
    df=pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    result=df.to_dict(orient="records")
    return result

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station,year):
    filename="data/TG_STAID"+str(station).zfill(6)+".txt"
    df=pd.read_csv(filename,skiprows=20)
    df["    DATE"]=df["    DATE"].astype(str)
    result=df[df["    DATE"].str.startswith(str(year))]
    return result.to_dict(orient="records")



if __name__ =="__main__":
    app.run(debug=True,port=5001)
