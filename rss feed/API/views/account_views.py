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