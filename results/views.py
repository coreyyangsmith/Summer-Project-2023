from django.shortcuts import render
from django.http import HttpResponse

from main.models import Metric

def index(response):
    return render(response, 'results/results.html',{})


def charts(response):
    labels = []
    data = []

    queryset = Metric.objects.order_by('-actual_value')[:10]
    for metric in queryset:
        labels.append(metric.name)
        data.append(metric.actual_value)

    # create context
    ctx = {
        'labels': labels,
        'data': data
    }
    
    return render(response, 'results/charts.html', ctx)
