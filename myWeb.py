from flask import Flask, render_template

app = Flask(__name__)
	
@app.route('/') # เป็นการเข้าหน้าแรก เสมือน local host:3000

def index():
   with open("history.txt", "r") as f: 
      content = f.read() 
   return render_template("index.html", content=content) 

if __name__ == '__main__':
   app.debug = True
   app.run()