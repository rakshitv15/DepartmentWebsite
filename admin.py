from django.contrib import admin
from .models import Profile, ResearchArea, MoEB, MoPB, AnH, SponsoredProject, InvitedTalk, CP, Publication

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'designation', 'photo', 'department', 'residence', 'phone']
@admin.register(ResearchArea)
class ResearchAreasAdmin(admin.ModelAdmin):
    list_display = ['RA_area',]
@admin.register(MoPB)
class MoPBAdmin(admin.ModelAdmin):
    list_display = ['MoPB_area',]
@admin.register(MoEB)
class MoEBAdmin(admin.ModelAdmin):
    list_display = ['MoEB_area',]
@admin.register(AnH)
class AnHAdmin(admin.ModelAdmin):
    list_display = ['AnH_area','AnH_year']
@admin.register(SponsoredProject)
class SponsoredProjectAdmin(admin.ModelAdmin):
    list_display = ['SP_area','SP_PriInv','SP_CoInv','SP_Spons']
@admin.register(InvitedTalk)
class InvitedTalkAdmin(admin.ModelAdmin):
    list_display = ['IT_area',]
@admin.register(CP)
class CPAdmin(admin.ModelAdmin):
    list_display = ['CP_area',]
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['Pub_type','Pub_area']