from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms


def indexpage(request):
    return redirect(reverse_lazy("base:books"))

class Bookview(LoginRequiredMixin, View):

    def get(self, request, slug=None):
        if slug == "add":
            return render(request, "addbook.html")
        if slug is not None:
            return render(request, "book.html", context={"book": models.BookModel.objects.filter(slug=slug)[0]})
        return render(request, "books.html", context={"books": models.BookModel.objects.all()})

    def post(self, request, add=None):
        addbookform = forms.BookForm(request.POST, request.FILES)
        if addbookform.is_valid():
            addbookform.save()
        print(addbookform.errors)
        return redirect(reverse_lazy("base:books"))
