from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # Nếu gọi trang chủ thì
def home(): #binding, view function
    return "Hello World, this is flask homepage"

@app.route('/c4e25')
def c4e25():
    return "ABCDEF"

@app.route('/c4e25/Huy')
def hi_huy():
    return "Hi Huy"

@app.route('/hi/<name>')
def hi(name):
    return(name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return(str(num1+num2))

@app.route('/simple_html')
def simple_html():
    return "<h3>AAAAAAAAAAAAAAAAA</h3>"

@app.route('/html')
def html():
    return render_template('Sample.html')

food_list =[
    "bún đậu",
    "bún chả",
    "gà rán"
]
detail = {
    'title': 'Thịt chó',
    'image': 'http://sohanews.sohacdn.com/thumb_w/660/2018/9/13/photo1536808346867-15368083468671055464984.jpg'
}

@app.route('/food/<int:no>') #detail
def food(no):
    return render_template('food.html',tittle=food_list[no])

@app.route('/menu')
def menu():
    return render_template('menu.html',food_list=food_list)
@app.route('/food/detail')
def food_detail():
    return render_template('food_detail.html', detail = detail)
if __name__ == "__main__":
    app.run(debug=True)