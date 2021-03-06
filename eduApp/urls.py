"""eduApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from eduApp.backend.account import views

urlpatterns = [
    path('', include('eduApp.frontend.urls')),
    path('study-program/', include('eduApp.backend.study_program.urls')),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('account/login', views.signin, name='login'),
    path('logout', views.signout, name='logout'),
    path('admin/', include('eduApp.backend.account.urls')),
    path('about_us/', include('eduApp.backend.about_us.urls')),
]

# Cấu hình Debug Toolbar Django
if settings.DEBUG:
    import debug_toolbar

    # urlpatterns = [
    #     path('__debug__/', include(debug_toolbar.urls)),
    # ] + urlpatterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)