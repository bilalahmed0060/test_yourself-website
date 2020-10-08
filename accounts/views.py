from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        user2= auth.signals
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('/accounts/login/')
    else:
        return render(request, 'test_yourself/login.html' )

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,"Username is already taken")
               return redirect('/accounts/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken")
                return redirect('/accounts/register/')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('/accounts/login/')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('/accounts/register/')

        return redirect('/')

    else:
        return render(request,'test_yourself/register.html',)


def logout(request):
    auth.logout(request)
    return redirect('/')