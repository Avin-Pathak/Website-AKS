from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'Key Username not found'
                raise Exception('Key Username not found')

            if data.get('password') is None:
                response['message'] = 'Key Password not found'
                raise Exception('Key Password not found')
            
            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user is None:
                response['message'] = 'Invalid Username, user not found'
                raise Exception('Invalid username not found')

            user_obj = authenticate(username = data.get('username'), password = data.get('password'))

            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'Invalid response'
                raise Exception('invalid password')
        
        except Exception as e :
            print (e)
        
        return Response(response)

LoginView = LoginView.as_view()


class RegisterView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'Key Username not found'
                raise Exception('Key Username not found')

            if data.get('password') is None:
                response['message'] = 'Key Password not found'
                raise Exception('Key Password not found')
            
            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user :
                response['message'] = 'Username already taken'
                raise Exception('Username already taken')

            user_obj = User.objects.create(username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()     
            response['message'] = 'User created'
            response['status'] = 200

        
        except Exception as e :
            print (e)
        
        return Response(response)

RegisterView = RegisterView.as_view()