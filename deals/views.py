from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DealsListSerilaizer
from .models import Deal, WishList, Purchase
from rest_framework import authentication, permissions
from datetime import datetime
from django.contrib.auth.models import User

class AllDealsList(APIView):
    def get(self, request, format=None):
        try:
            all_deals = Deal.objects.all()
            all_deals_data = DealsListSerilaizer(all_deals, many=True).data
            return Response({'status': 'success', 'data' : all_deals_data})
        except:
            return Response({'status' : 'failure', 'message' : 'could not find deals list'})

class AddToWishList(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request, format=None):
        try:
            user = request.user
            deal_id = request.data['deal_id']
            deal = Deal.objects.get(id=deal_id)
            if deal.end_date>datetime.now():
                return Response({'status': 'failure', 'message': 'provided deal is expired already'})
            else:
                new_entry = WishList.objects.create(user=user, deal=deal)
                new_entry.save()
        except Deal.DoesNotExist:
            return Response({'status' : 'failure', 'message' : 'could not find any deal with given id'})
        except:
            return Response({'status' : 'failure', 'message' : 'request does not comply paramters'})

class MakePurchase(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def isUserPurchaseValid(self):
        return True

    def post(self, request, format=None):
        try:
            user = request.user
            deal_id = request.data['deal_id']
            deal = Purchase.objects.get(id=deal_id)
            if not self.isUserPurchaseValid():
                return Response({'status': 'failure', 'message': 'It is not a valid purchase'})
            elif deal.end_date>datetime.now():
                return Response({'status': 'failure', 'message': 'provided deal is expired already'})
            else:
                active_old_purchases_count = Purchase.objects.filter(user=user, deal=deal, isUsed=False, expiry__gt=datetime.now()).count
                if active_old_purchases_count >= deal.number_of_simultaneous_purchase:
                    return Response({'status': 'failure', 'message': 'You can only purchase %d numbers simultaneouly for this deal'})
                else:
                    new_purchase_entry = Purchase.objects.create(user=user, deal=deal, expiry_date=datetime.now()+1)
                    new_purchase_entry.save()
        except Deal.DoesNotExist:
            return Response({'status' : 'failure', 'message' : 'could not find any deal with given id'})
        except:
            return Response({'status' : 'failure', 'message' : 'request does not comply paramters'})





