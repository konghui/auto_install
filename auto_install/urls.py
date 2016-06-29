#coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin
from pxe.views import *
from django.views.generic.base import RedirectView
from django.conf import settings
admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'auto_install.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^start/(\d+)',start),
    url(r'^batch_install/$',batch_install,name="batch_install"),
    url(r'^online/(?P<obj_id>\d+)',online_view),
    url(r'^edit/(?P<obj_id>\d+)',edit,name="edit"),
    url(r'^info/(\d+)', info, name='info'),
    url(r'^exe/',exe_page,name="exe"),
    url(r'^$', login_view,name='login'),
    url(r'^find/',find_page,name='find'),
    url(r'^logout/', logout_page, name="logout"),
    url(r'^del/(\d+)',del_obj),
    url(r'^lock/(?P<obj_id>\d+)/(?P<obj_code>True|False)',lock_obj),
    url(r'^post/',register_post),
    url(r'^jindu_post/(?P<get_id>\d+)',jindu_post),
    url(r'^jindu_get/(?P<get_id>\d+)',get_jindu_from_cache),
    url(r'^his/',his_page,name="his"),
    url(r'^finish/',finish_api),
    url(r'^delivery/(?P<obj_id>\d+)',delivery),
    url(r'^batch_delivery/$',batch_delivery,name='batch_delivery'),
    url(r'^ping/(?P<ping_id>\d+)',ping,name='ping'),
    url(r'^piliang/$',piliang,name="piliang"),
    url(r'^export_ip/$',export_ip,name="export_ip"),
    url(r'^upload/$',upload_file,name='upload'),
    url(r'^commit/$',auto_commit,name='commit'),
    url(r'^admin/', include(admin.site.urls)),
]

# ks file download
urlpatterns += [
    url(r'^ks/(?P<get_ks_id>\d+)',kickstart_file_url),
]

# Api file download for memos
urlpatterns += [
    url(r'^(?P<file_name>auto_install.sh|index.py|post.sh|autocommit.csv)',download_file,name="download"),
]
