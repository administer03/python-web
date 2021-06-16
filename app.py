from flask import Flask, render_template
import gspread 
from oauth2client.service_account import ServiceAccountCredentials 
from pprint import pprint 
import pandas as pd
import numpy as np


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"] 
creds = ServiceAccountCredentials.from_json_keyfile_name("sheet_bot.json", scope) 
client = gspread.authorize(creds) 


app = Flask(__name__)
	
@app.route('/') # เป็นการเข้าหน้าแรก เสมือน local host:3000

def index():
   sheet = client.open("bot_history").sheet1 
   data = sheet.get_all_values()
   # items = "".join(items)
   df = pd.DataFrame(data)
   html = df.to_html(classes='table table-striped', index = False, header=None)
   return render_template("index.html", content=html) 

if __name__ == '__main__':
   app.run(debug=False)