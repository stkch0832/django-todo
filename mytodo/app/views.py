from django.views.generic import View
from django.shortcuts import render
from .models import Ticket

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
