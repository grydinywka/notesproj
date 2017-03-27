from datetime import datetime
from notes.models import RequestMy
from django.core.urlresolvers import reverse


class RequestMyMiddleware(object):
    """Middleware for storing requests"""

    def process_request(self, request):
        # print(request.path)
        # print(reverse('requests_ajax'))
        if request.path != reverse('requests_ajax'):
            RequestMy.objects.create(path=request.path, method=request.method)
        # print(request.method)
        # print(datetime.now())
        return None