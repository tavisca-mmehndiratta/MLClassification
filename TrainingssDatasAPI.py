from flask import Flask, request
import pandas as pd
import numpy as np
import csv
from sklearn import tree
from sklearn import datasets
from sklearn import datasets, metrics
from sklearn.metrics import classification_report,confusion_matrix

app = Flask(__name__)

@app.route('/getDataForTraining')
def trainedData():
    distance=request.args.get('distance', default = 0, type = int)
    duration=request.args.get('duration', default = 0, type = int)
    train = pd.read_csv("C:/Users/mmehndiratta/Downloads/TrainingDataProvider/TrainingsData.csv")
    test = pd.read_csv("C:/Users/mmehndiratta/Downloads/TrainingDataProvider/TestingsData.csv")
    print(distance)
    print(duration)
    feature_cols=['Distance','Duration']
    X=train.loc[:,feature_cols]
    print("training Data")
    print(X)
    y=train.Output
    print("training Output")
    print(y)
    clf=tree.DecisionTreeClassifier()
    clf.fit(X,y)
##    train = pd.read_csv("C:/Users/mmehndiratta/Downloads/TestingData.csv")
    inpdataframe=pd.DataFrame({"Distance":[distance],"Duration":[duration]})
    outputPredicted=clf.predict(inpdataframe)
    outputPredicted.astype(int)
    
        
    
        
    dataFrameAddedFiles = pd.DataFrame({"Distance":distance,"Duration":duration,"Output":outputPredicted})
    dataFrameAddedFiles.to_csv("C:/Users/mmehndiratta/Downloads/TrainingDataProvider/TestingsData.csv",index=False)
    dataFrameToCsvFile= pd.read_csv("C:/Users/mmehndiratta/Downloads/TrainingDataProvider/TestingsData.csv")
    out=train.append(dataFrameToCsvFile)
    print(out)
    out.to_csv(r"C:/Users/mmehndiratta/Downloads/TrainingDataProvider/TrainingsData.csv", index=False)
##    out.to_csv(r"C:/Users/mmehndiratta/Downloads/TestingData.csv", index=False)
    print("output")
    print(out)
    if outputPredicted==0:
        return "Flight"
    elif outputPredicted==1:
        return "Car"
    elif outputPredicted==2:
        return "Flights And Hotels"
    else:
        return "Cars And Hotels"
    return "hello"

if __name__ == '__main__':
     app.run(host='172.16.14.216',debug=True)
     
