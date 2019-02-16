from flask import Flask, request, render_template, redirect
app = Flask(__name__)
import mlab
from food import Food
from mongoengine import Document,StringField, IntField

class User(Document):
    user = StringField()
    password = StringField()


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
        return redirect('/menu')

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

@app.route('/update_food/<food_id>', methods = ['GET','POST'])
def update_food(food_id):

    if request.method == "GET":
        mlab.connect()
        return render_template("update_food_form.html",f = Food.objects.with_id(food_id))
    elif request.method == "POST":
        mlab.connect()
        form = request.form
        t = form["title"]
        l = form["link"]
        f = Food.objects.with_id(food_id)
        f.update(set__title=t,set__link=l)
        f.reload()
        link = "/menu"
        return redirect(link)

@app.route('/login', methods=['GET','POST'])
def login():

    mlab.connect()

    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form 
        user = form['user']
        password = form['password']
        u = User.objects(user=user).first()
        if u != None:
            if u.password == password:
                return redirect('/menu')
            else:
                return ('Sai password')
        else:
            return 'Tên đăng nhập không tồn tại'


@app.route('/register',methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    elif request.method == "POST":
        mlab.connect()
        form = request.form 
        user = form['user']
        password = form['password']
        u = User(user=user,password=password)
        u.save()
        return redirect('/login')
        






if __name__ == '__main__':
    app.run(debug=True)