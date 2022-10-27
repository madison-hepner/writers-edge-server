from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from writersedgeapi.views import register_user, login_user
from writersedgeapi.views import PromptTypeView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'prompt_types', PromptTypeView, 'prompt_types')

urlpatterns = [
    path('login', login_user),
    path('register', register_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
