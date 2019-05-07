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
    create_post = "post/create", CreatePost
    delete_post = "post/delete/<int:pk>", DeletePost
     
    create_link = "link/create", CreateLink
    delete_link = "link/delete/<int:pk>", DeleteLink
    
    create_snippet = "snippet/create", CreateSnippet
    delete_snippet = "snippet/delete/<int:pk>", DeleteSnippet

urlpatterns = SocialPatterns() + SocialPostPatterns()

