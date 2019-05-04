from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from social.forms import SocialUserCreationForm, SocialUserChangeForm
from social.models import SocialUser, Post

class SocialUserAdmin(UserAdmin):
    add_form = SocialUserCreationForm
    form = SocialUserChangeForm
    model = SocialUser
    list_display = ['email', 'username',]

admin.site.register(SocialUser, SocialUserAdmin)
admin.site.register(Post)
