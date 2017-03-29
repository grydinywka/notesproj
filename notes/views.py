from django.views.generic import ListView, CreateView, TemplateView, View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from notes.models import Note, RequestMy
from notes.forms import CreateNoteUpperForm


def get_last_ten_requests():
    return RequestMy.objects.order_by('-id')[:10]


def get_count_unviewd_req(requests_qs):
    ids = [r.id for r in requests_qs]
    return RequestMy.objects.filter(pk__in=ids, is_viewed=False).count()


def set_viewed_reqs(requests_qs):
    for obj in requests_qs:
        obj.is_viewed = True
        obj.save()


class NoteListView(ListView):
    """
    The view for render list of notes
    """
    model = Note
    context_object_name = "notes"


@method_decorator(csrf_exempt, name='dispatch')
class NoteCreateView(CreateView):
    """
    The view for creating new uppercase note objects.
    If user make POST - response will JSON.
    If GET - html template with form.
    Make post may do from other domains
    """
    template_name = "notes/note_form.html"
    model = Note
    form_class = CreateNoteUpperForm

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # print(form.cleaned_data)
        note = Note.objects.create(text=form.cleaned_data['text'],
                                   image=form.cleaned_data['image'])
        new_count = Note.objects.count()
        if note.image:
            image_url = note.image.url
        else:
            image_url = "static/img/default.jpg"
        return JsonResponse({"status": "created", "note_id": note.id,
                             "new_count": new_count, "image_url": image_url})

    def form_invalid(self, form):
        errors = {}
        for field, errs in form.errors.items():
            errors[field] = errs
        return JsonResponse({"status": "errors", "errors": errors,
                             "data": form.data})


class NoteRandomView(View):
    """View for return random note object(text)"""

    def get(self, request, *args, **kwargs):
        note = Note.objects.order_by('?')[0]
        return JsonResponse({"note": note.text})


class RequestListView(ListView):
    """View for getting 10 last request"""

    template_name = 'notes/requestmy_list.html'
    model = RequestMy
    context_object_name = 'requests'

    def get_queryset(self):
        return get_last_ten_requests()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unviewed'] = get_count_unviewd_req()

        return context

    def get(self, request, *args, **kwargs):
        viewed = request.GET.get('viewed')
        if viewed == 'true':
            set_viewed_reqs(self.get_queryset())

        return super().get(request, *args, **kwargs)


class RequestListViewForAjax(View):
    """View for getting 10 last requests in ajax mode"""

    def get(self, request, *args, **kwargs):
        viewed = request.GET.get('viewed')
        requestsmy = get_last_ten_requests()
        if viewed == 'true':
            set_viewed_reqs(requestsmy)

        requests = [r.__str__() for r in requestsmy]
        unviewed = get_count_unviewd_req(requestsmy)
        return JsonResponse({"requests": requests,
                             "unviewed": unviewed})
