from flask import Flask, render_template
import pandas as pd
from firebase import firebase

app = Flask(__name__)

url_firebase = 'https://db-bot803-default-rtdb.firebaseio.com/'
messenger = firebase.FirebaseApplication(url_firebase)
	
@app.route('/') # เป็นการเข้าหน้าแรก เสมือน local host:3000
def index():
   try:
      content = messenger.get('/bot_transaction', 'last_action')
      del content[0]
      action = None
      CB = None
      chg = None
      CS = None
      Dt = None
      LP = None
      TPL = None
      for key, values in content[0].items():
         if key == 'Action':
            action = values
         elif key == 'Cash Balance(USD)':
            CB = values
         elif key == 'Change(percent)':
            chg  = values
         elif key == 'Coin Symbol':
            CS = values
         elif key == 'Date-time':
            Dt = values
         elif key == 'Last Price':
            LP = values
         elif key == 'Total Profit Loss':
            TPL = values
               
      return render_template("cm_bot.html",content_act=action, content_CB = CB, content_chg = chg, content_CS = CS,
      content_Dt = Dt, content_LP = LP, content_TPL = TPL)
   except:
      return render_template("cm_bot.html", content='Now nothing has changed.')

@app.route('/buy')
def buy():
   try:
      content = messenger.get('/bot_transaction', 'Bought')
      del content[0]
      df = pd.DataFrame.from_dict(content, orient='columns')
      html = df.to_html(classes='table table-striped', index = False).replace('style="text-align: right;"', '')
      return render_template("buy.html", content=html)
   except:
      return render_template("buy.html", content='Now nothing has changed.')


@app.route('/sell')
def sell():
   try:
      content2 = messenger.get('/bot_transaction', 'Sold')
      del content2[0]
      df2 = pd.DataFrame.from_dict(content2, orient='columns')
      html2 = df2.to_html(classes='table table-striped', index = False).replace('style="text-align: right;"', '')
      return render_template("sell.html", content=html2)
   except:
      return render_template("sell.html", content='Now nothing has changed.')

if __name__ == '__main__':
   app.run(debug=False)