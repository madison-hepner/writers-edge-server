from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from writersedgeapi.views import register_user, login_user
from writersedgeapi.views import PromptTypeView
from writersedgeapi.views import PromptView
from writersedgeapi.views import PromptPostView
from writersedgeapi.views import PostView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'prompt_types', PromptTypeView, 'prompt_types')
router.register(r'prompts', PromptView, 'prompts')
router.register(r'prompt_posts', PromptPostView, 'prompt_posts')
router.register(r'posts', PostView, 'posts')

urlpatterns = [
    path('login', login_user),
    path('register', register_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
