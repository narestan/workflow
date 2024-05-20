# reqmat/models.py

from reqmat.forms import ProfitRequestForm, GlassRequestForm, OtherRequestForm
from reqmat.models import ProfitRequest, GlassRequest, OtherRequest
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

class RequestListView(ListView):
    template_name = 'reqmat/request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return {
            'profit_requests': ProfitRequest.objects.all(),
            'glass_requests': GlassRequest.objects.all(),
            'other_requests': OtherRequest.objects.all(),
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request_types'] = ['profit', 'glass', 'other']
        return context

@login_required
def create_profit_request(request):
    if request.method == 'POST':
        form = ProfitRequestForm(request.POST)
        if form.is_valid():
            profit_request = form.save(commit=False)
            profit_request.requester = request.user
            profit_request.department = request.user.department
            profit_request.save()
            return redirect('reqmat:request_list')
    else:
        form = ProfitRequestForm()
    return render(request, 'reqmat/profit_request_form.html', {'form': form})

@login_required
def create_glass_request(request):
    if request.method == 'POST':
        form = GlassRequestForm(request.POST)
        if form.is_valid():
            glass_request = form.save(commit=False)
            glass_request.requester = request.user
            glass_request.department = request.user.department
            glass_request.save()
            return redirect('reqmat:request_list')
    else:
        form = GlassRequestForm()
    return render(request, 'reqmat/glass_request_form.html', {'form': form})

@login_required
def create_other_request(request):
    if request.method == 'POST':
        form = OtherRequestForm(request.POST)
        if form.is_valid():
            other_request = form.save(commit=False)
            other_request.requester = request.user
            other_request.department = request.user.department
            other_request.save()
            return redirect('reqmat:request_list')
    else:
        form = OtherRequestForm()
    return render(request, 'reqmat/other_request_form.html', {'form': form})
