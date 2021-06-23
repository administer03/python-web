from flask import Flask, render_template
import pandas as pd
from firebase import firebase

app = Flask(__name__)

url_firebase = 'https://db-bot803-default-rtdb.firebaseio.com/'
messenger = firebase.FirebaseApplication(url_firebase)
	
@app.route('/') # เป็นการเข้าหน้าแรก เสมือน local host:3000
def index():
   return render_template("cm_bot.html")

@app.route('/buy')
def buy():
   content = messenger.get('/bot_transaction', 'Bought')
   del content[0]
   df = pd.DataFrame.from_dict(content, orient='columns')
   html = df.to_html(classes='table table-striped', index = False).replace('style="text-align: right;"', '')
   return render_template("buy.html", content=html)

@app.route('/sell')
def sell():
   content2 = messenger.get('/bot_transaction', 'Sold')
   del content2[0]
   df2 = pd.DataFrame.from_dict(content2, orient='columns')
   html2 = df2.to_html(classes='table table-striped', index = False).replace('style="text-align: right;"', '')
   return render_template("sell.html", content=html2)

if __name__ == '__main__':
   app.run(debug=False)