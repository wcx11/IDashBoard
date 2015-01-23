from django.conf.urls import patterns, include, url
from django.contrib import admin
from DashBoardView.views import HomePage, RefreshHomePage, login, logout
from VirtualMachines.views import VMState, helloServer
from settings import CSS_DIR, JS_DIR, IMG_DIR

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IDashBoardServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePage),
    url(r'^refreshHomePage/$', RefreshHomePage),
    url(r'^saveVMState/$', VMState),
    url(r'^helloServer/$', helloServer),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^css/(?P<path>.*)','django.views.static.serve',{'document_root': CSS_DIR}),
    url(r'^js/(?P<path>.*)','django.views.static.serve',{'document_root': JS_DIR}),
    url(r'^img/(?P<path>.*)','django.views.static.serve',{'document_root': IMG_DIR}),
)
