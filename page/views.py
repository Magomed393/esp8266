from django.http import HttpResponse, HttpRequest
import time
from django.http import StreamingHttpResponse
import requests as rqs
from django.shortcuts import render



def index(request):
    if request.method == 'GET':
        return render(request, r'D:\prog\project\templates\site.html')


temp_list = []
hum_list = []


def sensor_readings(request):
    if request.method == 'GET':
        request.encoding = 'UTF-8'
        # print(request.encoding)
        x = request.GET.copy()
        temp = x.get('temp')
        hum = x.get('hum')
        global temp_list
        global hum_list
        temp_list.append(temp)
        hum_list.append(hum)
        return HttpResponse(None)


def stream_temp(request):
    def event_stream():
        while True:
            i = temp_list.pop()
            time.sleep(3)
            yield 'data: %s\n\n' % i
            # создал генератор который отправляет данные на Web страничку которая через js прослушивает вьюшку

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


def stream_hum(request):
    def event_stream():
        while True:
            i = hum_list.pop()
            time.sleep(3)
            yield 'data: %s\n\n' % i
            # создал генератор который отправляет данные на Web страничку которая через js прослушивает вьюшку

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


def esp(requests):
    rqs.get('http://192.168.43.91:5553?a=1')

