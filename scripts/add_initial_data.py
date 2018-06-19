from deals.models import Category, Vendor, Deal
from deals.serializers import CategorySerializer, VendorSerializer, DealSerializer
import json
from datetime import datetime, timedelta

with open('Initial Data/categories.json') as data_file:
    categories = json.load(data_file)

with open('Initial Data/vendors.json') as data_file:
    vendors = json.load(data_file)

with open('Initial Data/deals.json') as data_file:
    deals = json.load(data_file)


def run():


    #Add Category Data
    try:
        for each_category in categories:
            each_category['image'] = 'images/food.jpg'
            serializer = CategorySerializer(data=each_category)
            if serializer.is_valid():
                if not Category.objects.get(name=each_category['name']):
                    serializer.save()
        else:
            print(serializer.errors)
    except Exception as e:
        print('%s (%s)' % (e.message, type(e)))

   # Add Vendors Data
    try:
        for each_vendor in vendors:
            each_vendor['image'] = 'images/%s.jpg' % each_vendor['name']
            serializer = VendorSerializer(data=each_vendor)
            if serializer.is_valid():
                if not Vendor.objects.get(name=each_category['name']):
                    serializer.save()
            else:
                print(serializer.errors)
    except Exception as e:
        print('%s (%s)' % (e.message, type(e)))

        # Add Deals Data
    try:
        for each_deal in deals:

            todayDate = datetime.now()
            todayDateString = todayDate.strftime("%Y-%m-%d %H:%M:%S")
            expiryDate = todayDate + timedelta(days=15)
            expiryDateString = expiryDate.strftime("%Y-%m-%d %H:%M:%S")

            each_deal['end_date'] = expiryDateString
            each_deal['start_date'] = todayDateString

            if 'description' not in each_deal:
                each_deal['description'] = each_deal['title']

            each_deal['category'] = Category.objects.get(name=each_deal['category']).id
            each_deal['vendor'] = Vendor.objects.get(name=each_deal['vendor']).id
            each_deal['image'] = 'images/food.jpg'
            serializer = DealSerializer(data=each_deal)
            if serializer.is_valid():
                if not Deal.objects.get(name=each_category['title']):
                    serializer.save()
            else:
                print(serializer.errors)
    except Exception as e:
        print ('%s (%s)' % (e.message, type(e)))

    print('Values added')