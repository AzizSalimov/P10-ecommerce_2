# from django.contrib.auth.views import LoginView
# from django.shortcuts import render, redirect
#
# from account.forms import CustomAuthenticationForm
#
#
# class AccountLoginView(LoginView):
#     template_name = "account/login.html"
#
#
# def profile(request):
#     return render(request)


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from account.forms import CustomAuthenticationForm


class AccountLoginView(LoginView):
    template_name = "account/login.html"
    next_page = 'account:profile'

def login_view(request):
    if request.user.is_authenticated:
       return redirect('profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'account/account.html', {'error_message': error_message})
    else:
        return render(request, 'account/account.html')


def profile_view(request):
    user = request.user
    orders = user.objects.all()
    return render(request, 'account/profile.html', {'user': user, 'orders': orders})

def logout_view(request):
    logout(request)
    return redirect('account:login')
