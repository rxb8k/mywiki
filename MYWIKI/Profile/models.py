from django.db import models
from django.contrib.auth.models import User
import sys
sys.path.append("..")
from django.conf import settings
# 전체 프로필 모델
class Profile(models.Model):
    username=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image=models.ImageField()

# 테이블의 각 행별 모델
class Row(models.Model):
    subject=models.CharField(max_length=20, null=False)
    content=models.CharField(max_length=50, null=False)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)

# 문단 모델
class Topic(models.Model):
    topic_subject=models.CharField(max_length=10, null=False)
    topic_content=models.CharField(max_length=1000, null=False)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)

# 키워드 모델
class Keyword(models.Model):
    keyword1=models.CharField(max_length=10, null=False)
    keyword2=models.CharField(max_length=10, null=False)
    keyword3=models.CharField(max_length=10, null=False)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)

# 수정 내역
class History(models.Model):
    writer=models.CharField(max_length=50)
    date=models.DateTimeField(auto_created=True)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)

# 신고
class Report(models.Model):
    writer=models.CharField(max_length=50)
    reason=models.CharField(max_length=100)