from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def Welcome():
    return "Jagadeesh"
@app.route('/success/<int:score>')
def success(score):
    return "Impressico score "+str(score)
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
if __name__=='__main__':
    app.run(debug=True)