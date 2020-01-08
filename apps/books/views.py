from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import BookForm
from .models import Book


class BookListView(ListView):
    model = Book


class AjaxResponseMixin:
    template_partial_form = ''
    template_partial_list = ''

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            form_class = self.get_form_class()
            try:
                form = form_class(instance=self.get_object())
                obj = self.get_object()
            except:
                form = form_class()
                obj = None
            data = dict()
            data['html_form'] = render_to_string(self.template_partial_form, {'form': form, 'object': obj}, request=request)
            return JsonResponse(data)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = dict()
            obj_list = self.model.objects.all()
            list_name = self.get_context_object_name(self.object) + '_list'
            data['form_is_valid'] = True
            data['html_list'] = render_to_string(self.template_partial_list, {list_name:  obj_list})
            return JsonResponse(data)
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            data = dict()
            try:
                obj = self.get_object()
            except:
                obj = None
            data['form_is_valid'] = False
            data['html_form'] = render_to_string(self.template_partial_form, {'form': form, 'object': obj}, request=request)
            return JsonResponse(data)
        return super().form_invalid(form)


class BookCreateView(AjaxResponseMixin, CreateView):
    model = Book
    form_class = BookForm
    template_partial_form = 'books/book_modal_form.html'
    template_partial_list = 'books/book_partial_list.html'
    success_url = reverse_lazy('books:list')


class BookUpdateView(AjaxResponseMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_partial_form = 'books/book_modal_form.html'
    template_partial_list = 'books/book_partial_list.html'
    success_url = reverse_lazy('books:list')


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('books:list')
