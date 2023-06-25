from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User



def subcategeory(request):
   return render(request,"subcategeory.html")
def lastpage(request):
    return render(request,"lastpage.html")
def Home(request):
    return render(request,"Home.html")
def login(request):
    return render(request,"login.html")
def signup(request):
    if request.method=='POST':
       uname=request.POST.get('Username')
       email=request.POST.get('email')
       pass1=request.POST.get('psw')
       pass2=request.POST.get('psw-repeat')
       my_user=User.objects.create_user(uname,email,pass1)
       my_user.save()
       return HttpResponse("User has been created sucessfully!!!")
       print(uname,email,pass1,pass2)
       
       
    return render(request,"signup.html")

def Home1(request):
    return render(request,"Home1.html")



