from notes.models import RequestMy
from django.core.urlresolvers import reverse
from django.conf import settings


class RequestMyMiddleware(object):
    """Middleware for storing requests"""

    def process_request(self, request):
        if request.path != reverse('requests_ajax') and\
                    not request.path.startswith(settings.MEDIA_URL):
            RequestMy.objects.create(path=request.path, method=request.method)
        return None
