from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def tracker_home(request):
    trackers = Articles.objects.order_by('-date')
    return render(request, 'tracker/tracker_home.html', {'trackers': trackers})

class TrackerDetailView(DetailView):
    model = Articles
    template_name = 'tracker/details_view.html'
    context_object_name = 'tracker'

class TrackerUpdateView(UpdateView):
    model = Articles
    template_name = 'tracker/create.html'
    form_class = ArticlesForm

class TrackerDeleteView(DeleteView):
    model = Articles
    success_url = '/tracker/'
    template_name = 'tracker/tracker-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'tracker/create.html', data)