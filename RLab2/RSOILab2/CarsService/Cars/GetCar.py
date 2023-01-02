import json
from quart import Blueprint, Response, request
from .Models.ModelCars import CarsModel

GetCarB = Blueprint('GetCar', __name__, )


@GetCarB.route('/api/v1/cars/<string:carUid>', methods=['GET'])
async def GetCar(carUid: str) -> Response:
    try:
        car = CarsModel.select().where(
            CarsModel.car_uid == carUid
        ).get().to_dict()

        return Response(
            status=200,
            content_type='application/json',
            response=json.dumps(car)
        )
    except:
        return Response(
            status=404,
            content_type='application/json',
            response=json.dumps({
                'errors': ['No id']
            })
        )