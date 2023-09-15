from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from accounts.authentication import create_access_token,create_refresh_token,decode_access_token,decode_refresh_token
from API.serializers.account_serializer import AccountSerializer
from accounts.models import Account


app_name="API"
class RegisterAPIView(APIView):

    def post(self, request):
        
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

app_name="API"
class LoginAPIView(APIView):
    def post(self, request):
        account = Account.objects.filter(email=request.data["email"]).first()

        if not account:
            raise APIException("Invalid credentials!")

        if not account.check_password(request.data["password"]):
            raise APIException("Invalid credentials!")

        access_token = create_access_token(account.id)
        refresh_token = create_refresh_token(account.id)

        response = Response()

        response.set_cookie(key="refreshToken", value=refresh_token, httponly=True)
        response.data = {"token": access_token}

        return response