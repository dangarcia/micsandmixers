from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


# this is a login decorator it will not allow any view 
# without authentication
@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")