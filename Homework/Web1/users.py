Users = {
'huy' :{
            'name' : 'Nguyen Quang Huy',
            'age' : 29,
            'height' : '1m70',
            'weight' :  '75 kg',
            'favorite club' : 'Manchester United'
       },
'tuananh' : {
            'name' : 'Huynh Tuan Anh',
            'age' : 22,
            'height' : '1m75',
            'weight' : '78 kg',
            'favorite club' : 'Arsenal'
       }
}
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/user/<username>')
def user(username):

       if username.lower() not in Users.keys():
              return 'User is not valid'
       else:
              user = Users[username.lower()]
              return render_template('users.html', user = user)

if __name__ == '__main__':
       app.run(debug=True)