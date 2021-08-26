from django.contrib import admin
from . import models


# Register your models here.
# TabularInline allows us to edit the group members in the admin dashboard
class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
