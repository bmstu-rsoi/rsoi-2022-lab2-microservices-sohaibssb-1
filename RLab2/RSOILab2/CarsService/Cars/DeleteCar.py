import json
from quart import Blueprint, Response, request
from .Models.ModelCars import CarsModel

DeleteCar= Blueprint('DeleteCarRequest', __name__, )


@DeleteCar.route('/api/v1/cars/<string:carUid>/request', methods=['DELETE'])
async def DeleteCarRequest(carUid: str) -> Response:
    try:
        car = CarsModel.select().where(
            CarsModel.car_uid == carUid
        ).get()

        if car.availability is True:
            return Response(
                status=403,
                content_type='application/json',
                response=json.dumps({
                    'errors': ['Car not requested']
                })
            )

        car.availability = True
        car.save()

        return Response(
            status=200
        )
    except:
        return Response(
            status=404,
            content_type='application/json',
            response=json.dumps({
                'errors': ['No id']
            })
        )