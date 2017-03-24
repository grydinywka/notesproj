"""notes_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from notes.views import NoteListView, NoteCreateView,\
                        NoteUpperCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', NoteListView.as_view(), name='home'),
    url(r'^note/add/$', NoteCreateView.as_view(), name='notes_add'),
    url(r'^note/add-upper/$', NoteUpperCreateView.as_view(),
        name='notes_add_upper'),
]
