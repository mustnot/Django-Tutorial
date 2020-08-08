from django.contrib import admin
from .models import Activity, Participants

class ParticipantsInline(admin.TabularInline):
    model = Participants
    extra = 1

class ActivityAdmin(admin.ModelAdmin):
    inlines = [ParticipantsInline]

admin.site.register(Activity, ActivityAdmin)