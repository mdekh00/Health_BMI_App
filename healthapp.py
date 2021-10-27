#import required libraries

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')
@app.route('/results', methods=['POST'])
def results():
    #Get values from html
    if request.method == "POST":
        gender = request.form.get('gender')
        age = int(request.form.get('age'))
        ft = int(request.form.get('ft'))
        inch = float(request.form.get('inch'))
        wt = float(request.form.get('wt'))
        #Calculate bmi
        bmi = 703*wt/(ft*12 + inch)**2
        #calculate body fat percentage
        if gender == 'Male' and age >= 18:
            bfp = 1.20*bmi + 0.23*age - 16.2
        elif gender == 'Female' and age >= 18:
            bfp = 1.20*bmi + 0.23*age- 5.4
        elif gender == 'Male' and age < 18:
            bfp = 1.51*bmi -0.70*age -2.2
        else:
            bfp = 1.51*bmi-0.70 *age+1.4
            
    return render_template('results.html', bmi=round(bmi, 2), bfp = round(bfp, 2), gender = gender, age=age, ft=ft, inch=inch,wt= round(wt,2))
if __name__ == '__main__':
    app.run(debug=True)



