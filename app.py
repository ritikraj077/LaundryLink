from flask import Flask
from user.user_router import user_app

app = Flask(__name__) 
app.register_blueprint(user_app)   


@app.route('/')
def home_page():
    return ("this is the home page for laundrylink ")
 
 
if __name__ == '__main__':
    app.run(debug=True)
    