from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
# Create your views here.

def home(request):
    return render(request, 'mainpage1.html')

def read(request, id):
    profile = get_object_or_404(Profile, pk = id)
    return render(request, 'read.html', {'profile': profile})

def update(req, id):
    profile_object=get_object_or_404(Profile, pk=id)
    if req.method=='POST':
        #profile_object.image=req.POST['image']
        profile_object.image=req.FILES.get('image')
        profile_object.name=req.POST['name']
        profile_object.bdate=req.POST['bdate']
        profile_object.bplace=req.POST['bplace']
        profile_object.organ=req.POST['organ']
        profile_object.mbti=req.POST['mbti']
        profile_object.message=req.POST['message']
        profile_object.sns=req.POST['sns']
        profile_object.topic_content=req.POST['topic_content']
        profile_object.save()
        
        new_history = History()
        new_history.profile = profile_object
        new_history.date = timezone.now()
        new_history.writer = req.user
        new_history.save()
        return redirect('/profile/read/'+str(id), {'profile':profile_object})
    return render(req, 'update.html', {'profile':profile_object})

# def read(request, id):
#     profile = get_object_or_404(Profile, pk = id)
#     rows = Row.objects.filter(profile=id)
#     topics = Topic.objects.filter(profile=id)
#     # data={
#     #     'username':profile.username,
#     #     'profile': profile, 
#     #     'row_subject': rows.subject,
#     #     'row_content': rows.content,
#     #     'topic_subject':topics.subject,
#     #     'topic_content':topics.content
#     # }
#     return render(request, 'read.html', 
#     {"profile":profile, "rows":rows, "topics":topics})

def view_history(request, id):
    profile = get_object_or_404(Profile, pk = id)
    histories = History.objects.filter(profile=id)

    return render(request, 'history.html', {'profile': profile, 'histories': histories})