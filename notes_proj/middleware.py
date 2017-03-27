from datetime import datetime
from notes.models import RequestMy


class RequestMyMiddleware(object):
    """Middleware for storing requests"""

    def process_request(self, request):
        RequestMy.objects.create(path=request.path, method=request.method)
        print(request.method)
        # print(datetime.now())
        return None