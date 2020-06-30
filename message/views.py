from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class MessageView(View):
    def get(self, request):
        return HttpResponse("Hello, Django!")

    def post(self, request):
        return redirect('/')
