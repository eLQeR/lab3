from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def about(request):
    return render(request, 'index.html', context=None)

def about_company(request):
    return render(request, 'index.html', context=None)
