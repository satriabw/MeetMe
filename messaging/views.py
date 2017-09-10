from rest_framework.views import APIView
from .models import MessageModel
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import MessageSerialzer
from account.models import UserProfile
from time import gmtime, strftime
from rest_framework.response import Response
from rest_framework import status
import json
import requests
import rest_framework.generics as generics

FCM_KEY = "AAAAcJ8hJc4:APA91bHmmushor9vha7xMyxXHXXUDOAXO8YyCZxCBCzYFk99qGlCI_5uN9Y1hh2uqamtY9it8_iVYBxA7_xXFaYFIwx6UjNECDftutXK1SEdg_JRdssIe4agO0uLCrxhm3mB18vuLMLS"
BASE_URL = "https://fcm.googleapis.com/fcm/send"
HOST = "https://meetme-gemastik.herokuapp.com/"
# HOST = "http://127.0.0.1:8000/"
# Create your views here.


class ListMessageView(generics.ListCreateAPIView):
    model = MessageModel
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerialzer
    permission_classes = (IsAuthenticated,)


class MessageEngine(APIView):
    permission_classes = (IsAuthenticated, )

    # taken from github.com/aufahr
    def send_blocking_fcm(self, target, title, body):

        payload = {
            "to": target,
            "notification": {
                "title": title,
                "body": body
            }
        }

        headers = {
            'authorization': "key="+FCM_KEY,
            'content-type': "application/json",
            'cache-control': "no-cache",
        }
        response = requests.post(BASE_URL, data=json.dumps(payload), headers=headers)

    def create_message(self, sender, body , recipient, token):
        url = HOST + "api/v1/messaging/message/"
        data = {
            'sender' : sender,
            'body' : body,
            'recipient' : recipient,
        }

        headers = {
            "content-type": "application/json",
            'Authorization' : 'jwt ' + token
        }

        response = requests.post(url, data=json.dumps(data), headers=headers)

    def post(self, request, format=None):
        data = request.data
        user_sender_id = data.get('user')
        recipient_id = data.get('recipient')
        message = data.get('message')
        token = data.get('token')
        #create db
        self.create_message(user_sender_id, message, recipient_id, token)
        recipient_obj = UserProfile.objects.get(pk=recipient_id)
        target_token = recipient_obj.device_token
        title = "Message from: " + str(recipient_obj.user.username)
        body = {
            'sender_id' : user_sender_id,
            'message' : message,
            'timestamp' : strftime("%Y-%m-%d %H:%M:%S", gmtime())
        }
        self.send_blocking_fcm(target_token, title, body)
        return Response(body,status=status.HTTP_200_OK)



