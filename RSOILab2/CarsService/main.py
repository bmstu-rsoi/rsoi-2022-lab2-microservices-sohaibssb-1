from quart import Quart
from Cars.Models.ModelCars import CarsModel
from Cars.GetCars import GetCarsB
from Cars.GetCar import GetCarB
from Cars.PostCar import PostCarB
from Cars.DeleteCar import DeleteCar
from Cars.Check import Check_B

app = Quart(__name__)
app.register_B(GetCarsB)
app.register_B(GetCarB)
app.register_B(PostCarB)
app.register_B(DeleteCar)
app.register_B(Check_B)


def create_tables():
    CarsModel.drop_table()
    CarsModel.create_table()

    CarsModel.get_or_create(
        id=1,
        car_uid="109b42f3-198d-4c89-9276-a7520a7120ab",
        brand="Mercedes Benz",
        model="GLA 250",
        registration_number="ЛО777Х799",
        power=249,
        type="SEDAN",
        price=3500,
        availability=True
    )


if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port=8070)