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

# def update(request):



    
def marketPost_edit(req, id):
    marketPost_object=get_object_or_404(marketPost, pk=id)
    if req.method=='POST':
        marketPost_object.title=req.POST['title']
        marketPost_object.body=req.POST['content']
        marketPost_object.image=req.POST['image']
        marketPost_object.writer=req.user #수정에도 들어가나?
        marketPost_object.hashtag=req.POST['hashtag']
        
        marketPost_object.state=req.POST['state']
        marketPost_object.price=req.POST['price']
        marketPost_object.save()
        return redirect('/board/market/'+str(marketPost.id))
    return render(req,'11market_edit.html',{'data':marketPost_object})