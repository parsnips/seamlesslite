from django.core import serializers
from django.conf import settings
from django.utils import simplejson as json
from seamless.lite.containers import *
import urllib
import urllib2

class Order():
    def add_first_item_and_create_order(self, delivery_type, line_item):
        send_dict = self.create_add_item_dictionary(line_item)
        json_data = json.dumps(send_dict)
        data = json_data
        url='http://qaservices.seamlessweb.com/MemberWebServices/OrderRest.svc/'+delivery_type+'/order/items/?apikey='+settings.API_KEY
        r = urllib2.Request(url = url, data = data)
        r.add_header('Content-Type', 'application/json')
        try:
            response = urllib2.urlopen(r)
            s = response.read()
            response.close()
            return s
        except urllib2.HTTPError, e:
            return None
        except urllib2.URLError, e:
            return None
        
        
    
    def add_item_to_order(self, order_id, line_item):
        send_dict = self.create_add_item_dictionary(line_item)
        json_data = json.dumps(send_dict)
        data = json_data
        url='http://qaservices.seamlessweb.com/MemberWebServices/OrderRest.svc/order/'+order_id+'/items/?apikey='+settings.API_KEY
        r = urllib2.Request(url = url, data = data)
        r.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(r)
        return response.read()
        
        
    
    def create_add_item_dictionary(self, line_item):
        send_dict = {}
        send_dict["CategoryId"] = line_item.category_id
        send_dict["OrderId"] = line_item.order_id
        send_dict["ProductId"] = line_item.item_id
        send_dict["Quantity"] = line_item.quantity
        send_dict["SpecialInstructions"] = line_item.special_instructions
        send_dict["SelectedOptions"] = line_item.options
        send_dict["VendorLocationId"] = line_item.vendor_location_id
        return send_dict
    
class Restaurant():
    def get_restaurants(self, delivery_type, latitude, longitude):
        url = ''
        if delivery_type.lower() == 'delivery':
            url = "http://qaservices.seamlessweb.com/MemberWebServices/VendorInfoRest.svc/vendorlocation/"+delivery_type+"/"+latitude+"/"+longitude+"/?apikey="+settings.API_KEY
        elif delivery_type.lower() == 'pickup':
            url = "http://qaservices.seamlessweb.com/MemberWebServices/VendorInfoRest.svc/vendorlocation/"+delivery_type+"/"+latitude+"/"+longitude+"/mile/1/?apikey="+settings.API_KEY
        else:
            raise ValueError
      
        r = urllib2.Request(url = url)
        response = urllib2.urlopen(r)
        return response.read()
        
