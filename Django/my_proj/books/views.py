from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from books.models import Book

class BookList(ListView):
    model = Book
    template_name = 'book_list.html'  # Nome do template, se necessário

class BookView(DetailView):
    model = Book
    template_name = 'book_detail.html'  # Nome do template, se necessário

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')
    template_name = 'book_form.html'  # Nome do template, se necessário

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')
    template_name = 'book_form.html'  # Nome do template, se necessário

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    template_name = 'book_confirm_delete.html'  # Nome do template, se necessário
