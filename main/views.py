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


class TourListView(generic.ListView):
    model = Tour
    template_name = 'tour_list.html'
    context_object_name = 'tours'


def home(request):
    return render(request, 'home.html')


def tour_register(request):
    if request.method == 'POST':
        print(request)

class TourRegisterView(generic.UpdateView):
    model = CustomUser     
    form_class = TourRegisterForm
    template_name = 'tour_register.html'
    success_url = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            print(f'the request object : \n {self.request.user}')
    # registered_user = self.request.user
        return super(TourRegisterView, self).dispatch(request, *args, **kwargs)


