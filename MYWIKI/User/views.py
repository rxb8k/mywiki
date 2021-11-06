from django.shortcuts import redirect, render
from django.contrib import auth
from .models import User
from Profile.models import Profile, Row, Topic
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user_model
#User = get_user_model()

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

                row_aboutme1 = Row()
                row_aboutme1.profile = new_profile
                row_aboutme1.subject = "About me"
                row_aboutme1.content = ""

                row_aboutme2 = Row()
                row_aboutme2.profile = new_profile
                row_aboutme2.subject = "About me1"
                row_aboutme2.content = ""

                row_aboutme3 = Row()
                row_aboutme3.profile = new_profile
                row_aboutme3.subject = "About me2"
                row_aboutme3.content = ""

                topic_aboutme1=Topic()
                topic_aboutme1.profile=new_profile
                topic_aboutme1.topic_subject="About me1"
                topic_aboutme1.topic_content=""

                topic_aboutme2=Topic()
                topic_aboutme2.profile=new_profile
                topic_aboutme2.topic_subject="About me1"
                topic_aboutme2.topic_content=""

                topic_aboutme3=Topic()
                topic_aboutme3.profile=new_profile
                topic_aboutme3.topic_subject="About me1"
                topic_aboutme3.topic_content=""

                new_profile.save()
                row_aboutme1.save()
                row_aboutme2.save()
                row_aboutme3.save()
                topic_aboutme1.save()
                topic_aboutme2.save()
                topic_aboutme3.save()

        return redirect('profile/update/'+str(request.POST['username'])) # update 페이지로 redirect
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
            return redirect('profile/read/'+str(username)) # read 페이지로 redirect
    return render(request, 'login.html') 

#로그아웃
@login_required
def logout_view(request):
    auth.logout(request)
    return redirect('/')