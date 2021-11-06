from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.

def home(request):
    data={
        'id': Profile.id # 이게 맞나?
    }
    return render(request, 'mainpage1.html', data)

def read(request, id):
    profile = get_object_or_404(Profile, pk = id)
    rows = Row.objects.filter(profile=id)
    topics = Topic.objects.filter(profile=id)
    # data={
    #     'username':profile.username,
    #     'profile': profile, 
    #     'row_subject': rows.subject,
    #     'row_content': rows.content,
    #     'topic_subject':topics.subject,
    #     'topic_content':topics.content
    # }
    return render(request, 'read.html', 
    {"profile":profile, "rows":rows, "topics":topics})


def update(req, id):
    data={}
    print(req.POST)
    profile_object=get_object_or_404(Profile, pk=id)
    if req.method=='POST':
        row_object=req.POST.all('subject')
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

        return redirect('/profile/read'+str(id), data)
    data = { 'profile_id': id }
    return render(req, 'update.html')


def view_history(request, id):
    profile = get_object_or_404(Profile, pk = id)
    histories = History.objects.filter(profile=id)

    return render(request, 'history.html', {'profile': profile, 'histories': histories})

    from django.shortcuts import render, get_object_or_404, HttpResponseRedirect


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

        return redirect('/profile/read'+str(id), data)
    data = { 'profile_id': id }
    return render(req, 'update.html', data)


def view_history(request, id):
    profile = get_object_or_404(Profile, pk = id)
    histories = History.objects.filter(profile=id)

    return render(request, 'history.html', {'profile': profile, 'histories': histories})