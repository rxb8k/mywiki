from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from Profile.models import Profile, Row
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'mainpage1.html')

#회원가입
def signup_view(request):
    res_data = {}
    if request.method =='POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
            username = request.POST['username'], 
            password=request.POST['password1'], 
            )
            user.save()
            auth.login(request, user)

            new_profile = Profile()
            new_profile.username=user

            row_aboutme = Row()
            row_aboutme.profile = new_profile
            row_aboutme.subject = "About me"
            row_aboutme.content = ""

            row_aboutme1 = Row()
            row_aboutme1.profile = new_profile
            row_aboutme1.subject = "About me1"
            row_aboutme1.content = ""

            row_aboutme2 = Row()
            row_aboutme2.profile = new_profile
            row_aboutme2.subject = "About me2"
            row_aboutme2.content = ""

            new_profile.save()

            return redirect('/update/'+str(request.POST['username']))# update 페이지로 redirect
    else:
        res_data['error'] = '비밀번호가 다릅니다.'
    return render(request, 'signup.html', res_data)

#로그인
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username = username, password = password)
        print(User)
        if User is not None:
            auth.login(request, User)
            return redirect('/read/'+str(username)) # read 페이지로 redirect
    return render(request, 'login.html') 

#로그아웃
@login_required
def logout_view(request):
    auth.logout(request)
    return redirect('/')