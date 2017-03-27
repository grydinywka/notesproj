from notes.models import RequestMy
from django.core.urlresolvers import reverse


class RequestMyMiddleware(object):
    """Middleware for storing requests"""

    def process_request(self, request):
        if request.path != reverse('requests_ajax'):
            RequestMy.objects.create(path=request.path, method=request.method)
        return None
