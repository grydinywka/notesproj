from notes.models import RequestMy
from django.core.urlresolvers import reverse
from django.conf import settings


class RequestMyMiddleware(object):
    """Middleware for storing requests"""

    def process_request(self, request):
        # print(request.path)
        # print(settings.MEDIA_URL)
        if request.path != reverse('requests_ajax') and\
            str(request.path).startswith(settings.MEDIA_URL) == False:
            RequestMy.objects.create(path=request.path, method=request.method)
        return None
