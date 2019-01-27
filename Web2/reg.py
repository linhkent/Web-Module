from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template ('reg.html')
    elif request.method == 'POST':
        form = request.form 
        print (form['user'], form['pass'])
        return 'POST'

  

if __name__ == '__main__':
  app.run(debug=True)