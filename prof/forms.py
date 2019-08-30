from django import forms
from .models import Profile, ResearchArea, MoPB, MoEB, AnH, SponsoredProject, InvitedTalk, CP, Publication
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    designation = forms.CharField(required=False,widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    department = forms.CharField(required=False,widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    residence = forms.CharField(required=False,widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    phone = forms.CharField(required=False,widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    class Meta:
        model = Profile
        fields = ('designation', 'department', 'residence', 'phone')

class ResearchForm(forms.ModelForm):
    RA_area = forms.CharField(required=False,label="Research Area",widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    class Meta:
        model = ResearchArea
        fields = ('RA_area',)

class MoPB_form(forms.ModelForm):
    MoPB_area = forms.CharField(required=False,label="Professional Body",widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    MoPB_year = forms.CharField(required=False, label="Year")
    class Meta:
        model = MoPB
        fields = ('MoPB_area','MoPB_year')

class MoEB_form(forms.ModelForm):
    MoEB_area = forms.CharField(required=False,label="Editorial Board",widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    MoEB_year = forms.CharField(required=False, label="Year")
    class Meta:
        model = MoEB
        fields = ('MoEB_area','MoEB_year')
class AnH_form(forms.ModelForm):
    AnH_area = forms.CharField(required=False,label="Award/Honor",widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    AnH_year = forms.CharField(required=False,label="Year")
    class Meta:
        model = AnH
        fields = ('AnH_area','AnH_year')
class SponsoredProject_form(forms.ModelForm):
    SP_area = forms.CharField(required=False,label="Project Title",widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    SP_PriInv = forms.CharField(required=False, label="Principle Investigator",widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    SP_CoInv = forms.CharField(required=False, label="Co-Investigator",widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    SP_Spons = forms.CharField(required=False, label="Sponsors",widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    SP_year = forms.CharField(required=False, label="Year")
    class Meta:
        model = SponsoredProject
        fields = ('SP_area','SP_PriInv','SP_CoInv','SP_Spons','SP_year')
class InvitedTalk_form(forms.ModelForm):
    IT_area = forms.CharField(required=False,label="Name of the Invited Talk",widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    IT_year = forms.CharField(required=False, label="Year")
    class Meta:
        model = InvitedTalk
        fields = ('IT_area','IT_year')
class CP_form(forms.ModelForm):
    CP_area = forms.CharField(required=False,label="Name of the Conference Presentation",widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    CP_year = forms.CharField(required=False, label="Year")
    class Meta:
        model = CP
        fields = ('CP_area','CP_year')
class Publication_form(forms.ModelForm):
    TYPES = (
        ("JoAr", "Journal Article"),
        ("CoPr", "Conference Proceedings"),
        ("BoCh", "Book Chapters"),
        ("Bk", "Books")
    )
    Pub_type = forms.ChoiceField(required=False,label="Type of Publication",widget=forms.Select(),choices=TYPES)
    Pub_area = forms.CharField(required=False,label="Title of the Publication",widget=forms.TextInput(attrs={'style': 'width:80%; height:20%;'}))
    Pub_year = forms.CharField(required=False, label="Year")
    class Meta:
        model = Publication
        fields = ('Pub_type','Pub_area','Pub_year')