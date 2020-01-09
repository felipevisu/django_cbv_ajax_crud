from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import BookForm
from .mixins import AjaxCreateMixin, AjaxDeleteMixin, AjaxUpdateMixin
from .models import Book


class BookListView(ListView):
    model = Book


class BookCreateView(AjaxCreateMixin, CreateView):
    model = Book
    form_class = BookForm
    template_partial_form = 'books/book_modal_create_form.html'
    template_partial_list = 'books/book_partial_list.html'
    success_url = reverse_lazy('books:list')


class BookUpdateView(AjaxUpdateMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_partial_form = 'books/book_modal_update_form.html'
    template_partial_list = 'books/book_partial_list.html'
    success_url = reverse_lazy('books:list')


class BookDeleteView(AjaxDeleteMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books:list')
    template_partial_form = 'books/book_modal_delete_form.html'
    template_partial_list = 'books/book_partial_list.html'
    success_url = reverse_lazy('books:list')
