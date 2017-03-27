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
from django.conf.urls.static import static
from django.conf import settings

from notes.views import NoteListView, RequestListView,\
                        NoteCreateView, NoteRandomView,\
                        RequestListViewForAjax

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', NoteListView.as_view(), name='home'),
    url(r'^note/add/$', NoteCreateView.as_view(),
        name='notes_add'),
    url(r'^note/random/$', NoteRandomView.as_view(),
        name='note_random'),
    url(r'^requests/$', RequestListView.as_view(),
        name='requests_list'),
    url(r'^requests-ajax/$', RequestListViewForAjax.as_view(),
        name='requests_ajax'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
