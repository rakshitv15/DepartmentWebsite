from django.db import models
from django.conf import settings

class Basic_Detail(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=250)
    residence = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100,blank=True)
    department = models.CharField(max_length=250,blank=True)
    residence = models.CharField(max_length=500,blank=True)
    phone = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=100,blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
class ResearchArea(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    RA_area = models.CharField(max_length=250)
    def __str__(self):
        return self.RA_area
class MoPB(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    MoPB_area = models.CharField(max_length=250)
    MoPB_year = models.CharField(max_length=100)
    def __str__(self):
        return self.area
class MoEB(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    MoEB_area = models.CharField(max_length=250)
    MoEB_year = models.CharField(max_length=100)
    def __str__(self):
        return self.MoEB_area
class AnH(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    AnH_area = models.CharField(max_length=500)
    AnH_year = models.CharField(max_length=100)
    def __str__(self):
        return self.AnH_area
class SponsoredProject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    SP_area = models.CharField(max_length=500)
    SP_PriInv = models.CharField(max_length=300)
    SP_CoInv = models.CharField(max_length=300)
    SP_Spons = models.CharField(max_length=500)
    SP_year = models.CharField(max_length=100)
    def __str__(self):
        return self.SP_area
class InvitedTalk(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    IT_area = models.CharField(max_length=500)
    IT_year = models.CharField(max_length=100)
    def __str__(self):
        return self.IT_area
class CP(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CP_area = models.CharField(max_length=500)
    CP_year = models.CharField(max_length=100)
    def __str__(self):
        return self.CP_area
class Publication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Pub_type = models.CharField(max_length=500)
    Pub_area = models.CharField(max_length=500)
    Pub_year = models.CharField(max_length=100)
    def __str__(self):
        return self.area