from django.http import HttpResponseRedirect
from .models import House
from django.views.generic import ListView, DetailView, CreateView
from .forms import HouseForm, TaskForm
from django.urls import reverse_lazy


class StatsListView(ListView):
    template_name = 'brick_counter/stats.html'
    model = House
    queryset = House.objects.order_by('-task__date_and_time')
    paginate_by = 10


class HouseDetailView(DetailView):
    model = House
    template_name = 'brick_counter/house_page.html'


class CreateHouse(CreateView):
    template_name = 'brick_counter/building.html'
    form_class = HouseForm

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(reverse_lazy('brick_counter:house_page', args=[self.object.pk]))


class CreateTask(CreateView):
    template_name = 'brick_counter/create_task.html'
    form_class = TaskForm

    def form_valid(self, form):
        house = self.get_initial().get('house')
        self.object = form.save(commit=False)
        self.object.house = house
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('brick_counter:house_page', args=[house.pk]))

    def get_initial(self, *args, **kwargs):
        initial = super(CreateTask, self).get_initial(**kwargs)
        house = int(self.request.path.split('/')[2])
        house = House.objects.get(pk=house)
        initial['house'] = house
        return initial


