from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from DashBoardUser.models import DashBoardUser
from django.contrib import auth

# Create your views here.
def saveUserInfo(request):
    if request.user.is_authenticated():
        u = User.objects.filter(id=request.user.id)
        if len(u) != 0:
            if request.method == "POST":
                try:
                    profile = u[0].dashboarduser
                except:
                    profile = DashBoardUser(user=u[0])
                    profile.save()

                if request.POST.get('username',''):
                    u[0].username = request.POST.get('username','')
                if request.POST.get('email',''):
                    u[0].email = request.POST.get('email','')
                if request.POST.get('phone',''):
                    profile.phone = request.POST.get('phone','')
                if request.POST.get('department',''):
                    profile.department = request.POST.get('department', '').encode('utf-8')
                u[0].save()
                profile.save()
            else:
                pass
        else:
            pass
        return HttpResponseRedirect('/settings/')
    else:
        return HttpResponseRedirect('/')

def changePassword(request):
    if request.user.is_authenticated():
        u = request.user
        username = u.username
        if request.method == "POST":
            if request.POST.get('password',''):
                pwd = request.POST.get('password','')
            if request.POST.get('newpassword',''):
                newpwd = request.POST.get('newpassword','')
            if (not pwd) or (not newpwd):
                return HttpResponseRedirect('/settings/')
            if u.check_password(pwd):
                try:
                    u.set_password(newpwd)
                    u.save()
                    return HttpResponseRedirect('/settings/')
                except Exception, e:
                    print e
                    return HttpResponseRedirect('/settings/')

    return HttpResponseRedirect('/')