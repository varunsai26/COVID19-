# importing Flask and other modules
from sklearn import tree
from flask import Flask, request, render_template
import pickle
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function

@app.route('/',methods=["GET"])
def home():
   return render_template("project1.html")


@app.route('/project2.html', methods =["GET", "POST"])
def predictions():
   res={};
   if request.method == "POST":
      fever=int(request.form['t1'])
      cough=int(request.form['t2'])
      soreThroat=int(request.form['t3'])
      headAche=int(request.form['t4'])
      shortnessOfBreath=int(request.form['t5'])
      diarrhoea=int(request.form['t6'])
      age60AndAbove=int(request.form['t7'])
      gender=int(request.form['t8'])
      filename = 'covid19.sav'
      model = pickle.load(open(filename, 'rb'))
      testcase=[[cough,fever,soreThroat,headAche,shortnessOfBreath,diarrhoea,gender]]
      result3=model.predict(testcase)
      res={};
      if(result3[0]>1):
         res['ans']="There is chance of getting infected with Omicron ... "
         res['color']="red"
      elif(result3[0]>0.06):
         res['ans']="There is chance of getting infected with COVID19 ... " 
         res['color']="red"
      else:
         res['ans']="you are not infected with COVID19...."
         res['color']="green"

      
      print(res)
      return render_template('project2.html',Result=res)
   return render_template('project2.html',Result=res)
if __name__=='main_':
   app.run(debug=True)