import json
from quart import Blueprint, Response, request
from .Models.ModelRental import RentalModel


GetRentalsB = Blueprint('GetRentals', __name__,)


@GetRentalsB.route('/api/v1/rental/', methods=['GET'])
async def get_rentals() -> Response:
    if 'X-User-Name' not in request.headers.keys():
        return Response(
            status=400,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Error User Name']
            })
        )

    user = request.headers['X-User-Name']

    rentals = [rental.to_dict() for rental in RentalModel.select().where(RentalModel.username == user)]

    return Response(
        status=200,
        content_type='application/json',
        response=json.dumps(rentals)
    )