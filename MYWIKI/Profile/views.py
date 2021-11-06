from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.

def read(request, id):
    profile = get_object_or_404(Profile, pk = id)
    rows = Row.objects.filter(profile=id)
    topics = Topic.objects.filter(profile=id)
    
    data={
        'username':profile.username,
        'profile': profile, 
        'rows':rows,
        'topics': topics
    }

    return render(request, 'read.html', data)


def update(req, id):
    data={}
    print(req.POST)
    profile_object=get_object_or_404(Profile, pk=id)
    if req.method=='POST':
        row_subject_object=req.POST.getlist('subject[]')
        row_content_object=req.POST.getlist('content[]')
        topic_subject_object=req.POST.getlist('topic_subject[]')
        topic_content_object=req.POST.getlist('topic_content[]')

        data={
            'username' : profile_object.username,
            'subject[]': row_subject_object,
            'content[]': row_content_object,
            'topic_subject[]':topic_subject_object,
            'topic_content[]':topic_content_object,
        }

        return redirect('/profile/update'+str(id))
    return render(req, 'update.html', data)


def view_history(request, id):
    profile = get_object_or_404(Profile, pk = id)
    histories = History.objects.filter(profile=id)

    return render(request, 'history.html', {'profile': profile, 'histories': histories})
