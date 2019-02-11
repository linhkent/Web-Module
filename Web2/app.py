from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/add_food', methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('food_form.html')
    elif request.method == "POST":
        form = request.form
        t = form['title']
        l = form['link']
          
        print (t,l)
        return 'HOST' 

if __name__ == '__main__':
    app.run(debug=True)