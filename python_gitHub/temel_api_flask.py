from flask import Flask
uygulama= Flask(__name__)
@uygulama.route("/")
def helloWorld():
    return "<p>Hello,World!</p>"

@uygulama.route("/merhabaDunya")
def merhabaDunya():
    return "<p>Merhaba!</p>"

if __name__ == "__main__":
    uygulama.run(debug=True,host="localhost",port=22222)

    

