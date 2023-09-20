from django.shortcuts import render

# Create your views here.

def home (request):
   if "logged_in" in request.COOKIES and "username" in request.COOKIES:
      context = {
         "username":request.COOKIES["username"],
         "login_status":request.COOKIES.get("logged_in")
      }
      return render(request,'home.html')
   else:
      return render(request,'home.html')
    #return render(request,'home.html')

def login(request):
   
   if request.method=="GET":
      return render(request,'login.html')

   if request.method=="POST":
    username = request.POST.get('email')
    context = {
       
    }
    response = render(request,'home.html', context)
    #seting the cookie
    response.set_cookie('username', username)
    response.set_cookie('login_status', True)

    return response
    return render(request,'login.html')

def logout(request):
    pass