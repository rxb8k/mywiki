from django.shortcuts import render
from .models import Row

def profile_create(request):
  new_profile=Profile()
  new_profile.subject=request.POST.get('subject')
  new_profile.content=request.POST.get('content')
  return redirect('Profile:detail')
