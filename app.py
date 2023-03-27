# # import our flask library 
# from flask import Flask 

# # create our app instance         
# app = Flask(__name__)              

# # we create our app route as /, we can use something else as well probably "/hello" 
# @app.route("/")                
# def hello():
#     return "Hello World!"  
  
# # this is to automatically run the app  
# if __name__ == "__main__":         
#     app.run()
    
    
###############################################################################################
###############################################################################################


from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Tiger Home Page')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.run(debug=True)
