from django.views.generic import ListView, CreateView, TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from notes.models import Note
from notes.forms import CreateNoteUpperForm


class NoteListView(ListView):
    model = Note
    context_object_name = "notes"


class NoteUpperCreateView(CreateView):
    template_name = "notes/note_upper_form.html"
    model = Note
    form_class = CreateNoteUpperForm

    def get_success_url(self):
        messages.success(self.request, "Note uppercase create successfully")
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            print(request.POST)
            return super(NoteUpperCreateView, self).post(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('home'))

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return super(NoteUpperCreateView, self).get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('home'))


class Trycors(TemplateView):
    template_name = None

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(Trycors, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return JsonResponse({"Get": 'get'})

    def post(self, request, *args, **kwargs):
        # if request.is_ajax():
            # print(request.POST)
        return JsonResponse({"post":"All right"})