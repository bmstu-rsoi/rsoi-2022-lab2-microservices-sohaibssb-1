from quart import Quart
from Gateway.GetCarsB import GetCarsB
from Gateway.GetRentalsB import GetRentalsB
from Gateway.GetRentalB import GetRentalB
from Gateway.PostRentalB import PostRentalsB
from Gateway.DeleteRentalB import DeleteRentalB
from Gateway.PostRentalF import PostRentalFinishB
from Gateway.CheckB import Check_B

app = Quart(__name__)
app.register_blueprint(GetCarsB)
app.register_blueprint(GetRentalsB)
app.register_blueprint(PostRentalsB)
app.register_blueprint(DeleteRentalB)
app.register_blueprint(PostRentalFinishB)
app.register_blueprint(GetRentalB)
app.register_blueprint(Check_B)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
