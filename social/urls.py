from collections import UserList
from django.urls import include, path
from social.views import Home, Register

class PatternManager:
    """No list / dict comp, no context manager
    no abc, its the simplest way to do a PatternManager """
    
    def __init__(self):
        self.data = []
        patterns = dict(filter(lambda member: not member[0].startswith('_'), vars(self.__class__).items()))
        
        if 'includes' in patterns:
            for route, module in patterns.pop('includes').items():
                self.data.append(path(route, include(module)))
                
        for name, route in patterns.items():
            route, view = route
            if hasattr(view, 'as_view'):
                view = view.as_view()
                
            pattern = path(route, view, name=name)
            self.data.append(pattern)
    
        
class SocialPatterns(PatternManager, UserList):
    home = '', Home
    register = 'accounts/register/', Register
    
    includes = {'accounts': 'django.contrib.auth.urls'}

urlpatterns = SocialPatterns()
