from quart import Quart
from Rental.Models.ModelRental import RentalModel
from Rental.GetRentals import GetRentalsB
from Rental.GetRental import GetRentalB
from Rental.PostRental import PostRentalB
from Rental.DeleteRental import DeleteRentalB
from Rental.PostRentalF import PostRentalBF
from Rental.Check import Check_B

app = Quart(__name__)
app.register_blueprint(GetRentalB)
app.register_blueprint(GetRentalsB)
app.register_blueprint(PostRentalB)
app.register_blueprint(DeleteRentalB)
app.register_blueprint(PostRentalBF)
app.register_blueprint(Check_B)


def create_tables():
    RentalModel.drop_table()
    RentalModel.create_table()


if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port=8060)