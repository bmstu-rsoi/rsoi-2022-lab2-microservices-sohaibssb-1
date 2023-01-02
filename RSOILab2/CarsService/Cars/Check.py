from quart import Blueprint, Response


Check_B = Blueprint('Check', __name__, )


@Check_B.route('/manage/check', methods=['GET'])
async def check() -> Response:
    return Response(
        status=200
    )