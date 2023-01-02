from quart import Blueprint, Response


Check_B = Blueprint('health_check', __name__, )


@Check_B.route('/manage/check', methods=['GET'])
async def health_check() -> Response:
    return Response(
        status=200
    )