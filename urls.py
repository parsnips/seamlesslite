from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^seamless/', include('seamless.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^$', 'seamless.lite.views.index'),
    (r'^restaurants/(?P<delivery>\w+)/(?P<latitude>\d+\.\d+)/$', 'seamless.lite.views.restaurantsw'),
    (r'^restaurants/(?P<delivery>\w+)/(?P<latitude>-{0,1}\d+\.\d+)/(?P<longitude>-{0,1}\d+\.\d+)/$', 'seamless.lite.views.restaurants'),
    (r'^restaurant/(?P<id>\d+)/menu/$', 'seamless.lite.views.menu'),
    (r'^restaurant/(?P<vendor_location_id>\d+)/menu/item/(?P<item_id>\d+)/(?P<category_id>\d+)/$', 'seamless.lite.views.item'),
    (r'^restaurant/(?P<vendor_location_id>\d+)/menu/item/(?P<item_id>\d+)/optiongroup/(?P<option_group_id>\d+)/$', 'seamless.lite.views.options'),
    (r'^add_item/$', 'seamless.lite.views.add_item_to_order'),
    (r'^order/(?P<order_id>\d+)/$', 'seamless.lite.views.order_summary'),
    #(r'^restaurant/(?P<vendor_location_id>\d+)/menu/category/(?P<category_id>\d+)/items/$', 'seamless.lite.views.items_in_category'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT})
)
