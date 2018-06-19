from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DealsListSerilaizer
from .models import Deal

class AllDealsList(APIView):
    def get(self, request, format=None):
        try:
            all_deals = Deal.objects.all()
            all_deals_data = DealsListSerilaizer(all_deals, many=True).data
            return Response({'status': 'success', 'data' : all_deals_data})
        except:
            return Response({'status' : 'failure', 'message' : 'could not find deals list'})

