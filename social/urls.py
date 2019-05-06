from collections import UserList
from dataclasses import dataclass
from typing import Optional, Sequence

from django.urls import include, path
from purima.urls import PatternManager, IncludeFilter

from social.views import Home, Profile, Register, Post, Link, Snippet


class SocialPatterns(PatternManager):
    home = "", Home
    post = "share/post/", Post
    link = "share/link/", Link
    snippet = "share/snippet/", Snippet
    profile = "people/<slug>/", Profile
    register = "accounts/register/", Register
    
    includes = {
        "accounts/": IncludeFilter(
            "django.contrib.auth.urls", whitelist=("login", "logout")
        )
    }

urlpatterns = SocialPatterns()

