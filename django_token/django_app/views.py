from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_app import utils


@api_view(http_method_names=["GET", "POST"])
def api(request):
    return Response(data={"message": "OK"})


@api_view(http_method_names=["GET", "POST"])
def token(request):
    if request.method == "GET":
        return Response(data={"message": "OK"})
    elif request.method == "POST":
        try:
            username = request.data["username"]
            password = request.data["password"]
            if username and password and utils.check_password(password):
                token = utils.generate_token(password)
                return Response(data={"message": {"token": token}})
            return Response(data={"message": "Invalid username or password"})
        except Exception as error:
            return Response(data={"message": str(error)})
