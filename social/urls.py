from collections import UserList
from dataclasses import dataclass
from typing import Optional, Sequence

from django.urls import include, path
from purima.urls import PatternManager, IncludeFilter

from social.views import Home, Profile, Register, Post


class SocialPatterns(PatternManager):
    home = "", Home
    post = "post/", Post
    profile = "people/<slug>/", Profile
    register = "accounts/register/", Register

    includes = {
        "accounts/": IncludeFilter(
            "django.contrib.auth.urls", whitelist=("login", "logout")
        )
    }

urlpatterns = SocialPatterns()

