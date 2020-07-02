from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class MessageView(View):
    def get(self, request):
       return render(request, 'index.html')

    def post(self, request):
        return redirect('/')
