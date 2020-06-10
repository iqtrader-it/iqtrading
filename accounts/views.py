from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from  django.contrib.auth import  authenticate, login, logout


def sign_up(request):
    data = dict()
    data['title'] : 'Sign up'
    if request.method == 'GET':
        return render(request, 'accounts/sign_up.html', context=data)
    elif request.method == 'POST':
        # Extracting data from form
        su_login = request.POST.get('login')
        su_pass1 = request.POST.get('pass1')
        su_pass2 = request.POST.get('pass2')
        su_email = request.POST.get('email')

        #Checking data from form
        if su_pass1 != su_pass2 or len(su_pass1) < 8:
            data['color'] = 'red'
            data['report'] = 'Passwords mismatch or password contains less then 8 symbols. Please try again.'
        # Adding user to database
        else:
            data['login'] = su_login
            data['pass1'] = su_pass1
            data['pass2'] = su_pass2
            data['email'] = su_email
            user = User.objects.create_user(su_login, su_email, su_pass1)
            user.save()
            # Generating report
            data['title'] = 'Report of the registration'
            if user is None:
                data['color'] = 'red'
                data['report'] = 'Registration error'
            else:
                data['color'] = 'blue'
                data['report'] = 'Congratulations! You are registered.'
                login(request, user)
        return render(request, 'accounts/report.html', context=data)



def sign_in(request):
    data = dict()
    data['title'] = 'Sign in'
    if request.method == 'GET':
        return render(request, 'accounts/sign_in.html', context=data)
    elif request.method == 'POST':
        si_login = request.POST.get('login')
        si_pass1 = request.POST.get('pass1')
        user = authenticate(request, username=si_login, password=si_pass1)
        if user is None:
            data['title'] = 'Authentication report'
            data['color'] = 'red'
            data['text'] = 'User is not found'
            return render(request, 'accounts/report.html', context=data)
        else:
            login(request, user)
            return redirect('/home')


def sign_out(request):
    logout(request)
    return redirect('/home')


def profile(request):
    data = dict()
    data['title'] = 'Profile'
    return render(request, 'accounts/profile.html', context=data)


