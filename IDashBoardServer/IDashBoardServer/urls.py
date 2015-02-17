from django.conf.urls import patterns, include, url
from django.contrib import admin
from settings import CSS_DIR, JS_DIR, IMG_DIR, LIB_DIR

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'DashBoardView.views.HomePage'),
    url(r'^home/$', 'DashBoardView.views.home'),
    url(r'^detail/\d+/$', 'DashBoardView.views.detail'),
    url(r'get-detail/(?P<vm_id>\d+)/$', 'DashBoardView.views.get_detail'),
    url(r'^refreshHomePage/$', 'DashBoardView.views.RefreshHomePage'),
    url(r'^refreshSimplePage/$', 'DashBoardView.views.RefreshSimplePage'),
    url(r'^saveVMState/$', 'VirtualMachines.views.VMState'),
    url(r'^helloServer/$', 'VirtualMachines.views.helloServer'),
    url(r'^login/$', 'DashBoardView.views.login'),
    url(r'^logout/$', 'DashBoardView.views.logout'),
    url(r'^css/(?P<path>.*)', 'django.views.static.serve', {'document_root': CSS_DIR}),
    url(r'^js/(?P<path>.*)', 'django.views.static.serve', {'document_root': JS_DIR}),
    url(r'^img/(?P<path>.*)', 'django.views.static.serve', {'document_root': IMG_DIR}),
    url(r'^lib/(?P<path>.*)', 'django.views.static.serve', {'document_root': LIB_DIR}),
)
