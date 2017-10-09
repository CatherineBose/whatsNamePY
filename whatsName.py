from flask import Flask, render_template, request, redirect  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
@app.route('/')    
        
def home_page():
  return render_template('nameForm.html')    

@app.route('/process', methods=['POST'])
def about():
  fname = request.form['fname']
  lname= request.form['lname']
  return render_template('result.html',fname=fname,lname=lname)  
  return redirect('/')
app.run(debug=True)                             
