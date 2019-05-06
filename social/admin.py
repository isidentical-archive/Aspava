from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from social.forms import SocialUserChangeForm, SocialUserCreationForm
from social.models import Link, Post, Snippet, SocialUser
from django.contrib.auth import get_user_model


class SocialUserAdmin(UserAdmin):
    add_form = SocialUserCreationForm
    form = SocialUserChangeForm
    model = get_user_model()
    list_display = ["email", "username"]


admin.site.register(SocialUser, SocialUserAdmin)
admin.site.register(Post)
admin.site.register(Snippet)
admin.site.register(Link)
