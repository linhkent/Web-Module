from flask import Flask, request, render_template
app = Flask(__name__)
import mlab
from food import Food

@app.route('/add_food', methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('food_form.html')
    elif request.method == "POST":
        form = request.form
        t = form['title']
        l = form['link']
        mlab.connect()
        f = Food(title=t, link=l)
        f.save()  
        return 'Created'

# f_list = [
#     {
#         "title" : "com",
#         "link" : "https://via.placeholder.com/200x200",

#     },
#     {
#         "title" : "pho",
#         "link" : "https://via.placeholder.com/200x200",
#     }
# ]
@app.route('/menu')
def menu():
    mlab.connect()
    f_list = Food.objects()
    return render_template('menu.html',food_list=f_list)
@app.route('/food/<food_id>')
def food_detail(food_id):
    mlab.connect()
    f = Food.objects().with_id(food_id)
    return render_template ("food_detail.html", food = f)

if __name__ == '__main__':
    app.run(debug=True)