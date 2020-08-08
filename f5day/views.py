from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages

from .models import Activity, Participants


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_activity_list'

    def get_queryset(self):
        return Activity.objects.filter(
            f5_date__lte=timezone.now()
        ).order_by('id')

class DetailView(generic.DetailView):
    model = Activity
    template_name = 'detail.html'


def register(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    if activity.is_register_possible():
        try:
            participate_activity = Participants.objects.get(emp_id=request.POST['emp_id'])
        except Participants.DoesNotExist:
            Participants.objects.create(activity=activity, emp_id=request.POST['emp_id'])
            return HttpResponseRedirect(reverse('f5day:index'))
        else:
            if participate_activity.activity == activity:
                return render(request, 'detail.html', {
                    'activity': activity,
                    'error_message': 'You are already registering for another activity.'
                })
            else:
                return render(request, 'detail.html', {
                    'activity': activity,
                    'error_message': 'You are already registering for another activity.'
                })
