from flask import Flask
from user.user_router import user_app
from machines.machine_router import machine_app
from booking.booking_router import booking_app
from cleaning_and_ironing.cln_ion_routes import cln_ion
from upload_file.upload_file_router import file_upload


app = Flask(__name__) 
app.register_blueprint(user_app) 
app.register_blueprint(machine_app)  
app.register_blueprint(booking_app)
app.register_blueprint(cln_ion)
app.register_blueprint(file_upload)


@app.route('/')
def home_page():
    return ("this is the home page for laundrylink ")
 
 
if __name__ == '__main__':
    app.run(debug=True)
    