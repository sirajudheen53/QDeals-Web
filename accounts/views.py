from rest_framework.response import Response
from rest_framework.views import APIView
import requests

FACEBOOK_APP_ID = '459668444482931'
FACEBOOK_APP_SECRET = '89455b4348ff831e3c4a5541aa6467f6'

class LoginView(APIView):
    def post(self, request, format=None):
        access_token = request['access_token']
        provider = request['provider']
        if provider=='facebook':
            print(provider)
        elif provider=='google':
            print(provider)
        else:
            return  Response({'status' : 'failed', 'message' : 'Provide valid login provider'})

    def validateGoogleLogin(self, access_token):
        app_link = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + access_token
        try:
            user = requests.get(app_link).json()['data']
            print(user)
        except (ValueError, KeyError, TypeError) as error:
            return error
        return user

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
