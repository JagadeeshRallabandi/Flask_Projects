from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')
@app.route('/success/<int:score>')
def success(score):
    if score>50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)
@app.route('/fail/<int:score>')
def fail(score):
    return "Impressico failes score "+str(score)
@app.route('/results/<int:score>')
def results(score):
    result=""
    if score<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=score))
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['Science'])
        maths=float(request.method['maths'])
        C=float(request.form['C'])
        datascience=float(request.form['datascience'])
        total_score=(science+maths+C+datascience)/4
    res=""
    return redirect(url_for('success',score=total_score))
if __name__=='__main__':
    app.run(debug=True)