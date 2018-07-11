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
                try:
                    Category.objects.get(name=each_category['name'])
                except Category.DoesNotExist:
                    serializer.save()
        else:
            print(serializer.errors)
    except Exception as e:
        print(e.args, 'Exception in category')

   # Add Vendors Data
    try:
        for each_vendor in vendors:
            each_vendor['image'] = 'images/%s.jpg' % each_vendor['name']
            serializer = VendorSerializer(data=each_vendor)
            if serializer.is_valid():
                try:
                    Vendor.objects.get(name=each_vendor['name'])
                except Vendor.DoesNotExist:
                    serializer.save()
            else:
                print(serializer.errors)
    except Exception as e:
        print(e.args, 'Exception in Vendors')

        # Add Deals Data
    try:
        for each_deal in deals:

            each_deal['end_date'] = str( datetime.utcnow() + timedelta(days=15) )
            each_deal['start_date'] = str( datetime.utcnow() )

            if 'description' not in each_deal:
                each_deal['description'] = each_deal['title']

            each_deal['category'] = Category.objects.get(name=each_deal['category']).id
            each_deal['vendor'] = Vendor.objects.get(name=each_deal['vendor']).id
            each_deal['image'] = 'images/food.jpg'
            serializer = DealSerializer(data=each_deal)
            if serializer.is_valid():
                try:
                    Deal.objects.get(title=each_deal['title'])
                except Deal.DoesNotExist:
                    serializer.save()
            else:
                print(serializer.errors)
    except Exception as e:
        print(e.args, 'Exception in deal')

    print('Values added')