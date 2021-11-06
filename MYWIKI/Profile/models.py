from django.db import models
from django.contrib.auth.models import User
import sys
sys.path.append("..")
from django.conf import settings
# 전체 프로필 모델
class Profile(models.Model):
    username=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image=models.ImageField()
    name=models.CharField(max_length=20, default="")
    bdate=models.CharField(max_length=50, default="")
    bplace=models.CharField(max_length=20, default="")
    organ=models.CharField(max_length=20, default="")
    mbti=models.CharField(max_length=5, default="")
    message=models.CharField(max_length=20, default="")
    sns=models.CharField(max_length=50, default="")
    topic_content=models.CharField(max_length=1000, default="")


# # 문단 모델
# class Topic(models.Model):
#     topic_content=models.CharField(max_length=1000, null=False)
#     profile=models.ForeignKey(Profile, on_delete=models.CASCADE)

# 수정 내역
class History(models.Model):
    writer=models.CharField(max_length=50)
    date=models.DateTimeField(auto_created=True)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)

# 신고
class Report(models.Model):
    writer=models.CharField(max_length=50)
    reason=models.CharField(max_length=100)