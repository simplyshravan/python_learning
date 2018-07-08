from flask import Flask
from multiprocessing import Process

app = Flask(__name__) #creates instance of web applition.
# __name__ is variable in python that is equal to __main__

@app.route("/my") #route of webservice. we can give /home then it will take localhost:5000/home
def hello(): #defining the funtion that will eexcuted on route
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)#this will run the app 
    #debug==true will show error in browser
#shutdown_server()
server = Process(target=app.run)
#server.start()
# ...
#server.terminate()
server.join()