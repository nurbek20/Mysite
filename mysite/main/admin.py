from django.contrib import admin
from main.models import Contact, Skill, My_Skill

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message", "sent_at")
admin.site.register(Contact, ContactAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "link", "photo", "sent_at")
admin.site.register(Skill, SkillAdmin)

class My_SkillAdmin(admin.ModelAdmin):
    list_display = ('id','title')
admin.site.register(My_Skill, My_SkillAdmin)