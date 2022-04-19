import json
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication, permissions

# Create your views here.


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.serializer_class(
            data=request.data)  
        serializer.is_valid(raise_exception=True)  

        user = authenticate(
            email=serializer.validated_data["email"],
            password=serializer.validated_data['password'])  

        if not user:
            data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "invalid email or password. Please try again!!"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
           

        else:
            login(request, user)
            # create a token for user for identification
            token, created = Token.objects.get_or_create(user=user)
            data = {
                "status": status.HTTP_200_OK,
                "user_email": user.email,
                "token": token.key,
                }

            return Response(data, status=status.HTTP_200_OK)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_logout(request):

    Token.objects.get(user=request.user).delete()

    logout(request)
    data = {
        "status": status.HTTP_200_OK,
        "message": "logout successful"
    }

    return Response(data, status=status.HTTP_200_OK)


class internal_check(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get (self, request):
        serializer = bvn_checkserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bvn = serializer.validated_data.get('bvn')

        check_bvn = Liberty_Loan_database.objects.filter(BVN=bvn).first()
        if check_bvn:
            response = {
                        "status": status.HTTP_200_OK,
                        "data": {    
                            "Full_Name":check_bvn.Full_Name,
                            "bvn":check_bvn.BVN,      
                            "loan_status":check_bvn.Loan_Status_Name,
                            "Balance_Amount":check_bvn.Balance_Amount,
                            "Last_Repayment":check_bvn.Last_Repayment,
                            "Borrower_Mobile":check_bvn.Borrower_Mobile,
                            "Loan_Duration":check_bvn.Loan_Duration,
                            "Days_Past_Maturity": check_bvn.Days_Past_Maturity,
                            
                            
                        }             
            }
            return Response(response)

        else: 
            response = {
                        "status": status.HTTP_404_NOT_FOUND,
                        "message": "BVN not found on this database try check blacklist for update"  
            }
            
            return Response(response)