from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from .models import QUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

FACEBOOK_APP_ID = '459668444482931'
FACEBOOK_APP_SECRET = '89455b4348ff831e3c4a5541aa6467f6'

class LoginView(APIView):
    def post(self, request, format=None):
        access_token = request.data['access_token']
        provider = request.data['provider']
        if provider=='facebook':
            print(provider)
        elif provider=='google':
            response = self.validateGoogleLogin(access_token)
            return Response(response)
        else:
            return  Response({'status' : 'failed', 'message' : 'Provide valid login provider'})

    def validateGoogleLogin(self, access_token):
        app_link = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + access_token
        try:
            user = requests.get(app_link).json()
            print(user, '\n\n')
            first_name = user['given_name']
            last_name = user['family_name']
            email = user['email']
            picture = user['picture']
            try:
                print(user)
                current_user = QUser.objects.get(user__email=email)
                token = Token.objects.get(user=current_user.user)
                print(token, 'first token')
            except QUser.DoesNotExist:
                if first_name is not None:
                    new_user = User.objects.create(email=email, first_name=first_name, last_name=last_name)
                    new_user.save()
                    new_quser = QUser.objects.create(user=User.objects.get(email=email), profile_picture=picture, provider='google')
                    new_quser.save()
                    token = Token.objects.get(user=new_user)
                    print(token, 'second token')
                else :
                   return {"status": "failed", "message" : "something went wrong with server"}
            print({"status" : "success", "token" : token.key}, 'response')
            return  {"status" : "success", "token" : token.key}

        except (ValueError, KeyError, TypeError) as error:
            print(error)
            return Response({"status": "failed", "message": "something went wrong with server"})

    def validateFacebookLogin(self, access_token):
        appLink = 'https://graph.facebook.com/oauth/access_token?client_id='\
                  + FACEBOOK_APP_ID + '&client_secret='\
                  + FACEBOOK_APP_SECRET + '&grant_type=client_credentials'

        appToken = requests.get(appLink).json()['access_token']
        link = 'https://graph.facebook.com/debug_token?input_token=' + access_token + '&access_token=' + appToken
        try:
            user = requests.get(link).json()['data']
            print(user)
        except (ValueError, KeyError, TypeError) as error:
            return error
        return user

