from django.shortcuts import render, get_object_or_404
from .models import Tour
from .forms import TourForm

from django.views import generic

class TourDetailView(generic.DetailView):
    model = Tour
    template_name = 'tour_detail.html'
    context_object_name = "tour"


# def tour_detail(request, tour_id):
#     tour = get_object_or_404(Tour, pk=tour_id)
#     return render(request, 'tour_detail.html', {'tour': tour})


def fill_form(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            # Process the form data
            # Redirect to success page or perform any desired action
            pass
    else:
        form = TourForm()
    return render(request, 'fill_form.html', {'tour': tour, 'form': form})


def home(request):
    return render(request, 'home.html')