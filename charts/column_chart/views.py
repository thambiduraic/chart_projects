import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
 
def index(request):
    data_points = [
        { "label": "apple",  "y": 10  },
        { "label": "orange", "y": 15  },
        { "label": "banana", "y": 25  },
        { "label": "mango",  "y": 30  },
        { "label": "grape",  "y": 28  }
    ]
    return render(request, 'column_chart/index.html', { "data_points" : json.dumps(data_points) })

def multi_column_view(request):
  datapoints = [
    { "x": 10, "y": 171 },
    { "x": 20, "y": 155},
    { "x": 30, "y": 150 },
    { "x": 40, "y": 165 },
    { "x": 50, "y": 195 },
    { "x": 60, "y": 168 },
    { "x": 70, "y": 128 },
    { "x": 80, "y": 134 },
    { "x": 90, "y": 114}
  ]
 
  datapoints2 = [
    { "x": 10, "y": 71 },
    { "x": 20, "y": 55},
    { "x": 30, "y": 50 },
    { "x": 40, "y": 65 },
    { "x": 50, "y": 95 },
    { "x": 60, "y": 68 },
    { "x": 70, "y": 28 },
    { "x": 80, "y": 34 },
    { "x": 90, "y": 14 }
  ]
 
  return render(request, 'column_chart/multi_column.html', { "datapoints" : json.dumps(datapoints), "datapoints2": json.dumps(datapoints2) })  