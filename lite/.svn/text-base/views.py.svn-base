# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import Context, RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import simplejson as json
from django.shortcuts import *
from django.db.models import Q
from django.core import serializers
from django.conf import settings
from seamless.lite.containers import *
from seamless.lite.businesslogic import *
import urllib
import urllib2


def index(request):
    return render_to_response('address_entry.html', { }, 
                              context_instance=RequestContext(request))

def add_item_to_order(request):
    quantity = request.POST['quantity']
    item_id = request.POST['item_id']
    vendor_location_id = request.POST['vendor_location_id']
    category_id = request.POST['category_id']
    selected_options = []
    
    item = get_item(vendor_location_id, item_id)

    post_keys = []
    for option_group in item.option_groups:
        post_keys = request.POST.keys()
        if post_keys.__contains__('selected_option_group_'+option_group.option_group_id):
            selected_options.extend(request.POST.getlist('selected_option_group_'+option_group.option_group_id))
    
    line_item = LineItem()
    line_item.category_id = category_id
    line_item.item_id = item_id
    line_item.options = selected_options
    line_item.quantity = quantity
    line_item.vendor_location_id = vendor_location_id
    
    
    o = Order()
    if 'order_id' in request.session:
        o.add_item_to_order(request.session['order_id'], line_item)
    else:
        if 'delivery_type' not in request.session:
            delivery_type = 'delivery'
        else:
            delivery_type = request.session['delivery_type']
        
        summary_string = o.add_first_item_and_create_order(delivery_type, line_item)
        summary_json = json.loads(summary_string)
        order_id = summary_json['OrderId']
        request.session['order_id'] = order_id.strip('"')        
    
    return menu(request, vendor_location_id)    

def get_item(vendor_location_id, item_id):
    url = "http://qaservices.seamlessweb.com/MemberWebServices/VendorInfoRest.svc/vendorlocation/"+vendor_location_id+"/menu/item/"+item_id+"/?apikey="+settings.API_KEY
    f = urllib.urlopen(url)
    s = f.read()
    f.close()
    retval = json.loads(s)
    item = Item()
    item.item_id = retval['ProductId'];
    item.name = retval['Name']
    item.price = retval['Price']
    item.category_id = retval['CategoryId']
    
    item.option_groups = []

    for optiongroupjson in retval['OptionGroups']:
        option_group = OptionGroup()
        option_group.option_group_id = optiongroupjson['OptionGroupId']
        option_group.name = optiongroupjson['Name']
        option_group.included_selections = optiongroupjson['IncludedSelections']
        option_group.maximum_selections = optiongroupjson['MaximumSelections']
        option_group.minimum_selections = optiongroupjson['MinimumSelections']
        option_group.options = []
        for optionjson in optiongroupjson['Options']:
            option = Option()
            option.option_id = optionjson['OptionId']
            option.name = optionjson['Name']
            option.price = optionjson['Price']
            option_group.options.append(option)

        item.option_groups.append(option_group) 
    return item
    
def options(request, vendor_location_id, item_id, option_group_id):
    url = "http://qaservices.seamlessweb.com/MemberWebServices/VendorInfoRest.svc/vendorlocation/"+vendor_location_id+"/menu/item/"+item_id+"/optiongroup/"+option_group_id+"/options/?apikey="+settings.API_KEY
    f = urllib.urlopen(url)
    s = f.read()
    f.close()
    retval = json.loads(s)
    return HttpResponse(json.dumps(retval),
                                    mimetype='application/json')    
    
def item(request, vendor_location_id, item_id, category_id):
    item = get_item(vendor_location_id, item_id)
    item.category_id = category_id
    option_groups = item.option_groups
        
    return render_to_response('item.html', 
                              {'item' : item,'option_groups' : option_groups,'vendor_location_id' : vendor_location_id},
                              context_instance=RequestContext(request))
    
def menu(request, id):
    url = "http://qaservices.seamlessweb.com/MemberWebServices/VendorInfoRest.svc/vendorlocation/"+id+"/menu/?apikey="+settings.API_KEY
    f = urllib.urlopen(url)
    s = f.read()
    f.close()
    retval = json.loads(s)
    menujson = retval['MenuItemsGroupedByCategory'] 
    
    menu = Menu()
    menu.vendor_location_id = id
    menu.categories = []
    for categoryjson in menujson:
        category = Category()
        category.name = categoryjson['Key']
        category.items = []
        for i in categoryjson['Value']:
            item = Item()
            item.name = i['Name']
            item.item_id = i['ProductId']
            item.price = i['Price']
            item.category_id = i['CategoryId']
            category.items.append(item)
        
        menu.categories.append(category)
    order_id = ""
    if 'order_id' in request.session:
        order_id = request.session['order_id']
 
    return render_to_response('restaurant.html', {'menu' : menu,'vendor_location_id' : id, 'order_id' : order_id},
                              context_instance=RequestContext(request))

    
def restaurants(request, delivery, latitude, longitude):
    r = Restaurant()
    s = r.get_restaurants(delivery, latitude, longitude)
    data = json.loads(s)
    request.session['delivery_type'] = delivery
    return HttpResponse(json.dumps(data),
                                    mimetype='application/json')
    
def order_summary(request, order_id):
    url = "http://qaservices.seamlessweb.com/MemberWebServices/OrderRest.svc/order/"+order_id+"/?apikey="+settings.API_KEY
    f = urllib.urlopen(url)
    s = f.read()
    f.close()
    data = json.loads(s)
    return HttpResponse(json.dumps(data),
                                    mimetype='application/json')
