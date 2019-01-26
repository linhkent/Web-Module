from flask import Flask, render_template
app = Flask(__name__)

@app.route('/BMI/<int:w>/<int:h>')
def BMI(w,h):
  bmi = 10000* w / (h*h)
  if bmi < 16:
    stt = '\n Severely underweight'
  elif bmi < 18.5:
    stt = '\n Underweight'
  elif bmi < 25:
    stt = '\n Normal'
  elif bmi < 30:
    stt = '\n Overweight'
  else:
    stt = '\n Obese'
  return str(bmi) + stt

@app.route('/bmi/<int:w>/<int:h>')
def bmi(w,h):
  bmi = 10000* w / (h*h)
  if bmi < 16:
    stt = '\n Severely underweight'
  elif bmi < 18.5:
    stt = '\n Underweight'
  elif bmi < 25:
    stt = '\n Normal'
  elif bmi < 30:
    stt = '\n Overweight'
  else:
    stt = '\n Obese'
  bmi = str(bmi)
  return render_template('bmi.html', bmi = bmi, stt = stt)  

if __name__ == '__main__':
  app.run(debug=True)