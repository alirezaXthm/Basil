from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from .models import Tour
from .forms import TourForm, TourRegisterForm
from accounts.models import CustomUser
from django.urls import reverse_lazy

from django.views import generic

class TourDetailView(generic.DetailView):
    model = Tour
    template_name = 'tour_detail.html'
    context_object_name = "tour"


# def tour_detail(request, tour_id):
#     tour = get_object_or_404(Tour, pk=tour_id)
#     return render(request, 'tour_detail.html', {'tour': tour})

class TourRegisterView(generic.UpdateView):
    model = CustomUser     
    form_class = TourRegisterForm
    template_name = 'main/tour_register.html'
    # context_object_name = "tour"    
    success_url = reverse_lazy('home')
    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)
    
    

# def fill_form(request, tour_id):
#     tour = get_object_or_404(Tour, pk=tour_id)
#     if request.method == 'POST':
#         form = TourForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             # Redirect to success page or perform any desired action
#             pass
#     else:
#         form = TourForm()
#     return render(request, 'fill_form.html', {'tour': tour, 'form': form})


def home(request):
    return render(request, 'home.html')