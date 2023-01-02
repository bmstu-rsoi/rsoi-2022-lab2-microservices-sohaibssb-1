import json
from quart import Blueprint, Response, request
from .Models.ModelCars import CarsModel

PostCarB = Blueprint('PostCarRequest', __name__, )


@PostCarB.route('/api/v1/cars/<string:carUid>/request', methods=['POST'])
async def post_car_order(carUid: str) -> Response:
    try:
        car = CarsModel.select().where(
            CarsModel.car_uid == carUid
        ).get()

        if car.availability is False:
            return Response(
                status=403,
                content_type='application/json',
                response=json.dumps({
                    'errors': ['Error Car Booked']
                })
            )

        car.availability = False
        car.save()

        return Response(
            status=200,
            content_type='application/json',
            response=json.dumps(car.to_dict())
        )
    except:
        return Response(
            status=404,
            content_type='application/json',
            response=json.dumps({
                'errors': ['No Id']
            })
        )