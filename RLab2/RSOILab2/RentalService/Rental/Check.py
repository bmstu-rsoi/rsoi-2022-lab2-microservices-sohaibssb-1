from quart import Blueprint, Response


Check_B = Blueprint('CheckH', __name__, )


@Check_B.route('/manage/health', methods=['GET'])
async def CheckH() -> Response:
    return Response(
        status=200
    )