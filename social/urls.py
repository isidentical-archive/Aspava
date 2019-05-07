from collections import UserList
from dataclasses import dataclass
from typing import Optional, Sequence

from django.urls import include, path
from purima.urls import PatternManager, IncludeFilter

from social.views import *


class SocialPatterns(PatternManager):
    home = "", Home
    profile = "people/<slug>/", Profile
    register = "accounts/register/", Register
    
    includes = {
        "accounts/": IncludeFilter(
            "django.contrib.auth.urls", whitelist=("login", "logout")
        ),
        "captcha/": "captcha.urls"
    }

class SocialPostPatterns(PatternManager):
    create_post = "create/post", CreatePost
    create_link = "create/link", CreateLink
    create_snippet = "create/snippet", CreateSnippet

urlpatterns = SocialPatterns() + SocialPostPatterns()

