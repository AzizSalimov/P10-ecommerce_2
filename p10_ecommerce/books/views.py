from django.views.generic import ListView, DetailView, TemplateView

from books.models import Book


class BaseView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class HomeView(ListView):
    queryset = Book.objects.order_by("-id")
    template_name = "home.html"
    context_object_name = "books"


class BooksListView(ListView):
    queryset = Book.objects.order_by("-id")
    template_name = "books/books.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = "books/book_detail.html"
    context_object_name = "book"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     book_id = self.kwargs.get(self.pk_url_kwarg)
    #     context["first_book"] = Book.objects.first()
    #     context["book"] = Book.objects.filter(id=book_id).first()
    #     return context