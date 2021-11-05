from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.

def read(request,username):
    profile = get_object_or_404(Profile, pk = id)
    rows = Row.objects.filter(profile=id)
    topics = Topic.objects.filter(profile=id)
    keywords = Keyword.objects.filter(profile=id)

    # 키워드 시각화 ?
    return render(request, 'read.html', 
    {'profile': profile, 
    'rows':rows,
    'topics': topics})


def update(req, id):
    profile_object=get_object_or_404(Profile, pk=id)
    if req.method=='POST':
        # profile_object 각각 변수 설정
        # marketPost_object.title=req.POST['title']
        profile_obejct=req.getParameterValues("")
        return redirect('/update'+str(Profile.username))
    return render(req, 'update.html', {'data':profile_object})


def view_history(request, id):
    profile = get_object_or_404(Profile, pk = id)
    histories = History.objects.filter(profile=id)

    return render(request, 'history.html', {'profile': profile, 'histories': histories})
