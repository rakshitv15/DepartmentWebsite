from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.models import User
from .models import ResearchArea, MoPB, MoEB, AnH, SponsoredProject, InvitedTalk, CP, Publication
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import LoginForm, UserEditForm, ProfileEditForm, ResearchForm, MoEB_form, MoPB_form, AnH_form, SponsoredProject_form, InvitedTalk_form, CP_form, Publication_form

"""def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated ')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})"""
def profile(request, user_ID = None):
    if user_ID == 0:
        currentuser = User.objects.get(username="atasimohanty")
    if user_ID == 1:
        currentuser = User.objects.get(username="banibhattacharya")
    if user_ID == 2:
        currentuser = User.objects.get(username="jiaulpaik")
    if user_ID == 3:
        currentuser = User.objects.get(username="kaushalkumarbhagat")
    if user_ID == 4:
        currentuser = User.objects.get(username="manjirasinha")
    if user_ID == 5:
        currentuser = User.objects.get(username="plabankumarbhowmick")
    if user_ID == 6:
        currentuser = User.objects.get(username="rajibmall")
    if user_ID == 7:
        currentuser = User.objects.get(username="rajlakshmiguha")
    if user_ID == 8:
        currentuser = User.objects.get(username="shyamalkumardasmandal")
    userRA = ResearchArea.objects.filter(user=currentuser)
    userMoPB = MoPB.objects.filter(user=currentuser).order_by('MoPB_year')
    userMoEB = MoEB.objects.filter(user=currentuser).order_by('MoEB_year')
    userAnH = AnH.objects.filter(user=currentuser).order_by('AnH_year')
    userSP = SponsoredProject.objects.filter(user=currentuser).order_by('SP_year')
    userIT = InvitedTalk.objects.filter(user=currentuser).order_by('IT_year')
    userCP = CP.objects.filter(user=currentuser).order_by('CP_year')
    userPub = Publication.objects.filter(user=currentuser).order_by('Pub_year')
    JoAr = Publication.objects.filter(user=currentuser,Pub_type="JoAr").order_by('Pub_year')
    CoPr = Publication.objects.filter(user=currentuser, Pub_type="CoPr").order_by('Pub_year')
    BoCh = Publication.objects.filter(user=currentuser, Pub_type="BoCh").order_by('Pub_year')
    Bk = Publication.objects.filter(user=currentuser, Pub_type="Bk").order_by('Pub_year')
    profile = currentuser.profile
    return render(request, 'account/profile.html', {'JoAr': JoAr, 'CoPr': CoPr, 'BoCh': BoCh, 'Bk': Bk, 'profile': profile, 'userRA': userRA, 'userMoPB': userMoPB, 'userMoEB': userMoEB, 'userAnH': userAnH, 'userSP': userSP, 'userIT': userIT, 'userCP': userCP, 'userPub': userPub})

@login_required
def dashboard(request):
    userRA = ResearchArea.objects.filter(user=request.user)
    userMoPB = MoPB.objects.filter(user=request.user).order_by('MoPB_year')
    userMoEB = MoEB.objects.filter(user=request.user).order_by('MoEB_year')
    userAnH = AnH.objects.filter(user=request.user).order_by('AnH_year')
    userSP = SponsoredProject.objects.filter(user=request.user).order_by('SP_year')
    userIT = InvitedTalk.objects.filter(user=request.user).order_by('IT_year')
    userCP = CP.objects.filter(user=request.user).order_by('CP_year')
    userPub = Publication.objects.filter(user=request.user).order_by('Pub_year')
    index = None
    if request.method == 'POST':
        research_form = ResearchForm()
        MoPBform = MoPB_form()
        MoEBform = MoEB_form()
        AnHform = AnH_form()
        SPform = SponsoredProject_form()
        ITform = InvitedTalk_form()
        CPform = CP_form()
        Pubform = Publication_form()
        userRA = ResearchArea.objects.filter(user=request.user)
        userMoPB = MoPB.objects.filter(user=request.user).order_by('MoPB_year')
        userMoEB = MoEB.objects.filter(user=request.user).order_by('MoEB_year')
        userAnH = AnH.objects.filter(user=request.user).order_by('AnH_year')
        userSP = SponsoredProject.objects.filter(user=request.user).order_by('SP_year')
        userIT = InvitedTalk.objects.filter(user=request.user).order_by('IT_year')
        userCP = CP.objects.filter(user=request.user).order_by('CP_year')
        userPub = Publication.objects.filter(user=request.user).order_by('Pub_year')
        flag = 0
        for element in userRA:
            if element.RA_area == request.POST['RA_area']:
                flag = 1
        if not request.POST['RA_area']:
            flag = 1
        if flag == 0:
            rs = ResearchArea.objects.create(user=request.user)
            research_form = ResearchForm(instance=rs, data=request.POST)
            if research_form.is_valid():
                research_form.save()
                userRA = ResearchArea.objects.filter(user=request.user)
        else:
            research_form = ResearchForm(instance=request.user, data=request.POST)
        flag = 0
        for element in userMoPB:
            if element.MoPB_area == request.POST['MoPB_area']:
                flag = 1
        if not request.POST['MoPB_area']:
            flag = 1
        if flag == 0:
            moPb = MoPB.objects.create(user=request.user)
            MoPBform = MoPB_form(instance=moPb, data=request.POST)
            if MoPBform.is_valid():
                MoPBform.save()
                userMoPB = MoPB.objects.filter(user=request.user)
        else:
            MoPBform = MoPB_form(instance=request.user, data=request.POST)
        flag = 0
        for element in userMoEB:
            if element.MoEB_area == request.POST['MoEB_area']:
                flag = 1
        if not request.POST['MoEB_area']:
            flag = 1
        if flag == 0:
            moEb = MoEB.objects.create(user=request.user)
            MoEBform = MoEB_form(instance=moEb, data=request.POST)
            if MoEBform.is_valid():
                MoEBform.save()
                userMoEB = MoEB.objects.filter(user=request.user)
        else:
            MoEBform = MoEB_form(instance=request.user, data=request.POST)
        flag = 0
        for element in userAnH:
            if element.AnH_area == request.POST['AnH_area']:
                flag = 1
        if not request.POST['AnH_area']:
            flag = 1
        if flag == 0:
            anh = AnH.objects.create(user=request.user)
            AnHform = AnH_form(instance=anh, data=request.POST)
            if AnHform.is_valid():
                AnHform.save()
                userAnH = AnH.objects.filter(user=request.user)
        else:
            AnHform = AnH_form(instance=request.user, data=request.POST)
        flag = 0
        for element in userSP:
            if element.SP_area == request.POST['SP_area']:
                flag = 1
        if not request.POST['SP_area']:
            flag = 1
        if flag == 0:
            sp = SponsoredProject.objects.create(user=request.user)
            SPform = SponsoredProject_form(instance=sp, data=request.POST)
            if SPform.is_valid():
                SPform.save()
                userSP = SponsoredProject.objects.filter(user=request.user)
        else:
            SPform = SponsoredProject_form(instance=request.user, data=request.POST)
        flag = 0
        for element in userIT:
            if element.IT_area == request.POST['IT_area']:
                flag = 1
        if not request.POST['IT_area']:
            flag = 1
        if flag == 0:
            it = InvitedTalk.objects.create(user=request.user)
            ITform = InvitedTalk_form(instance=it, data=request.POST)
            if ITform.is_valid():
                ITform.save()
                userIT = InvitedTalk.objects.filter(user=request.user)
        else:
            ITform = InvitedTalk_form(instance=request.user, data=request.POST)
        flag = 0
        for element in userCP:
            if element.CP_area == request.POST['CP_area']:
                flag = 1
        if not request.POST['CP_area']:
            flag = 1
        if flag == 0:
            cp = CP.objects.create(user=request.user)
            CPform = CP_form(instance=cp, data=request.POST)
            if CPform.is_valid():
                CPform.save()
                userCP = CP.objects.filter(user=request.user)
        else:
            CPform = CP_form(instance=request.user, data=request.POST)
        flag = 0
        for element in userPub:
            if element.Pub_area == request.POST['Pub_area']:
                flag = 1
        if not request.POST['Pub_area']:
            flag = 1
        if flag == 0:
            pub = Publication.objects.create(user=request.user)
            Pubform = Publication_form(instance=pub, data=request.POST)
            if Pubform.is_valid():
                Pubform.save()
                userPub = Publication.objects.filter(user=request.user)
        else:
            Pubform = Publication_form(instance=request.user, data=request.POST)

        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        research_form = ResearchForm(instance=request.user)
        MoPBform = MoPB_form(instance=request.user)
        MoEBform = MoEB_form(instance=request.user)
        AnHform = AnH_form(instance=request.user)
        SPform = SponsoredProject_form(instance=request.user)
        ITform = InvitedTalk_form(instance=request.user)
        CPform = CP_form(instance=request.user)
        Pubform = Publication_form(instance=request.user)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        research_form = ResearchForm(instance=request.user)
        MoPBform = MoPB_form(instance=request.user)
        MoEBform = MoEB_form(instance=request.user)
        AnHform = AnH_form(instance=request.user)
        SPform = SponsoredProject_form(instance=request.user)
        ITform = InvitedTalk_form(instance=request.user)
        CPform = CP_form(instance=request.user)
        Pubform = Publication_form(instance=request.user)
    return render(request, 'account/dashboard.html', {'index': index, 'user_form': user_form, 'profile_form': profile_form, 'research_form': research_form, 'MoPBform': MoPBform, 'MoEBform': MoEBform, 'AnHform': AnHform, 'SPform': SPform, 'ITform': ITform, 'CPform': CPform, 'Pubform': Pubform, 'userRA': userRA, 'userMoPB': userMoPB, 'userMoEB': userMoEB, 'userAnH': userAnH, 'userSP': userSP, 'userIT': userIT, 'userCP': userCP, 'userPub': userPub})

@login_required
def editfunction(request, id =None, index = None):
    research_form = ResearchForm(instance=request.user, data=request.POST)
    MoPBform = MoPB_form(instance=request.user, data=request.POST)
    MoEBform = MoEB_form(instance=request.user, data=request.POST)
    AnHform = AnH_form(instance=request.user, data=request.POST)
    SPform = SponsoredProject_form(instance=request.user, data=request.POST)
    ITform = InvitedTalk_form(instance=request.user, data=request.POST)
    CPform = CP_form(instance=request.user, data=request.POST)
    Pubform = Publication_form(instance=request.user, data=request.POST)
    if index == 0:
        object = ResearchArea.objects.get(pk=id)
        research_form = ResearchForm(instance=request.user, data={'RA_area': object.RA_area})
    if index == 1:
        object = MoPB.objects.get(pk=id)
        MoPBform = MoPB_form(instance=request.user, data={'MoPB_area': object.MoPB_area})
    if index == 2:
        object = MoEB.objects.get(pk=id)
        MoEBform = MoEB_form(instance=request.user, data={'MoEB_area': object.MoEB_area})
    if index == 3:
        object = AnH.objects.get(pk=id)
        AnHform = AnH_form(instance=request.user, data={'AnH_area': object.AnH_area,'AnH_year': object.AnH_year})
    if index == 4:
        object = SponsoredProject.objects.get(pk=id)
        SPform = SponsoredProject_form(instance=request.user, data={'SP_area':object.SP_area, 'SP_PriInv':object.SP_PriInv,'SP_CoInv':object.SP_CoInv,'SP_Spons':object.SP_Spons})
    if index == 5:
        object = InvitedTalk.objects.get(pk=id)
        ITform = InvitedTalk_form(instance=request.user, data={'IT_area': object.IT_area})
    if index == 6:
        object = CP.objects.get(pk=id)
        CPform = CP_form(instance=request.user, data={'CP_area': object.CP_area})
    if index == 7:
        object = Publication.objects.get(pk=id)
        Pubform = Publication_form(instance=request.user, data={'Pub_type': object.Pub_type ,'Pub_area': object.Pub_area})
    object.delete()
    _index = index
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    userRA = ResearchArea.objects.filter(user=request.user)
    userMoPB = MoPB.objects.filter(user=request.user)
    userMoEB = MoEB.objects.filter(user=request.user)
    userAnH = AnH.objects.filter(user=request.user)
    userSP = SponsoredProject.objects.filter(user=request.user)
    userIT = InvitedTalk.objects.filter(user=request.user)
    userCP = CP.objects.filter(user=request.user)
    userPub = Publication.objects.filter(user=request.user)
    return render(request, 'account/dashboard.html', {'index': _index, 'user_form': user_form, 'profile_form': profile_form, 'research_form': research_form, 'MoPBform': MoPBform, 'MoEBform': MoEBform, 'AnHform': AnHform, 'SPform': SPform, 'ITform': ITform, 'CPform': CPform, 'Pubform': Pubform, 'userRA': userRA, 'userMoPB': userMoPB, 'userMoEB': userMoEB, 'userAnH': userAnH, 'userSP': userSP, 'userIT': userIT, 'userCP': userCP, 'userPub': userPub})

@login_required
def delfunction(request,id =None, index = None):
    if index == 0:
        object = ResearchArea.objects.get(pk=id)
    if index == 1:
        object = MoPB.objects.get(pk=id)
    if index == 2:
        object = MoEB.objects.get(pk=id)
    if index == 3:
        object = AnH.objects.get(pk=id)
    if index == 4:
        object = SponsoredProject.objects.get(pk=id)
    if index == 5:
        object = InvitedTalk.objects.get(pk=id)
    if index == 6:
        object = CP.objects.get(pk=id)
    if index == 7:
        object = Publication.objects.get(pk=id)
    object.delete()
    _index = index
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    research_form = ResearchForm(instance=request.user, data=request.POST)
    MoPBform = MoPB_form(instance=request.user, data=request.POST)
    MoEBform = MoEB_form(instance=request.user, data=request.POST)
    AnHform = AnH_form(instance=request.user, data=request.POST)
    SPform = SponsoredProject_form(instance=request.user, data=request.POST)
    ITform = InvitedTalk_form(instance=request.user, data=request.POST)
    CPform = CP_form(instance=request.user, data=request.POST)
    Pubform = Publication_form(instance=request.user, data=request.POST)
    userRA = ResearchArea.objects.filter(user=request.user)
    userMoPB = MoPB.objects.filter(user=request.user)
    userMoEB = MoEB.objects.filter(user=request.user)
    userAnH = AnH.objects.filter(user=request.user)
    userSP = SponsoredProject.objects.filter(user=request.user)
    userIT = InvitedTalk.objects.filter(user=request.user)
    userCP = CP.objects.filter(user=request.user)
    userPub = Publication.objects.filter(user=request.user)
    return render(request, 'account/dashboard.html', {'index': _index, 'user_form': user_form, 'profile_form': profile_form, 'research_form': research_form, 'MoPBform': MoPBform, 'MoEBform': MoEBform, 'AnHform': AnHform, 'SPform': SPform, 'ITform': ITform, 'CPform': CPform, 'Pubform': Pubform, 'userRA': userRA, 'userMoPB': userMoPB, 'userMoEB': userMoEB, 'userAnH': userAnH, 'userSP': userSP, 'userIT': userIT, 'userCP': userCP, 'userPub': userPub})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'user_form': user_form,'profile_form': profile_form})