from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request,'home.html')

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