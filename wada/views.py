from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from wada.models import Imggal


def image_display(request):
    res_display = Imggal.objects.order_by('-created_date')
    return render(request, 'index.html', {'Imggal': res_display})


class SearchResultsView(ListView):
    model = Imggal
    template_name = 'search_results.html'

    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = super().get_queryset()
        search_answer = "Nothing"
        if search:
            return queryset.filter(
                Q(img_title__icontains=search) | Q(img_description__icontains=search)
            )
        else:
            return search_answer, queryset
