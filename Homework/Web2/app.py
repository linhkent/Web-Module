from flask import Flask, render_template, request
app = Flask(__name__)
import mlab
from bike import Bike

@app.route('/new_bike',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        mlab.connect()
        form = request.form
        model = form['model']
        fee = form['fee']
        link = form['link']
        year = form['year']
        b = Bike(model = model, fee = int(fee), link = link, year = int(year))
        b.save()
        print(model,fee,link,year)
        return ('HOST')
    
  

if __name__ == '__main__':
  app.run(debug=True)