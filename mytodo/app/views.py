from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    def get(self, request, *args, **kwargs):
        ticket_data = Ticket.objects.order_by("-id")
        return render(request, 'app/index.html', {
            'ticket_data': ticket_data
        })

class TicketDetailView(View):
    def get(self, request, *args, **kwargs):
        ticket_data = Ticket.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/ticket_detail.html', {
            'ticket_data': ticket_data,
        })

class CreateTicketView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = TicketForm(request.POST or None)

        return render(request, 'app/ticket_form.html', {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST or None)

        if form.is_valid():
            ticket_data = Ticket()
            ticket_data.user = request.user
            ticket_data.title = form.cleaned_data['title']
            ticket_data.description = form.cleaned_data['description']
            ticket_data.save()
            return redirect('ticket_detail', ticket_data.id)

        return render(request, 'app/ticket_form.html', {
                'form': form,
        })
