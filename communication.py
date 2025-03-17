from flask import Flask, request, jsonify
import csv

app = Flask(__name__)


CSVFileName = "SavedData.csv" #change this to whatever we want the data saved as

def WriteToFile(data): #function writes to CSV file MAKE SURE FILE ALREADY EXIST
    with open(CSVFileName, "a", newline = "") as file: #writes to file with type a(append) so that the old data is not deleted
        text = csv.writer(file)
        text.writerow([data["Temperature"], data["Humidity"], data["Moisture"], data["Lighting"]])



@app.route('/SensorData', methods=['POST']) #creates API endpoint
def GetData():
    data = request.get_json() #grabs data that the simulation posted
    print("Received data:", data) #print data

    WriteToFile(data) #writes data to csv file
    return jsonify({"status": "success"}), 200 #ensure success DO NOT TAKE OUT or else error

if __name__ == '__main__': #runs the flask server on port 5000
    app.run(host='0.0.0.0', port=5000)