from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def read(request,id):
    profile = get_object_or_404(Profile, pk = id)
    rows = Row.objects.filter(number=id)
    topics = Topic.objects.filter(number=id)
    keywords = Keyword.objects.filter(number=id)

    # 키워드 시각화 ?
    return render(request, 'read.html', {'profile': profile, 'rows':rows, 'topics': topics, 'keywords': keywords})

def view_history(request, id):
    profile = get_object_or_404(Profile, pk = id)
    histories = History.objects.filter(number=id)

    return render(request, 'history.html', {'profile': profile, 'histories': histories})


def update(req):
    profile_obejct=get_object_or_404(Profile, pk=id)
    if req.method=='POST':
        # profile_object 각각 변수 설정
        # marketPost_object.title=req.POST['title']
        profile_obejct=req.getParameterValues("")
        return redirect('/update'+str(Profile.username))
    return render(req, 'update.html', {'data':profile_object}
