from django.http import HttpResponse, HttpRequest
# import re
import django
from time import sleep
from django.shortcuts import render
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from requests import Response
from django_eventstream import send_event
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from json import loads

class DB():
    def __init__(self):
        try:
            # Подключение к существующей базе данных
            self.connection = psycopg2.connect(user="postgres",
                                               # пароль, который указали при установке PostgreSQL
                                               password="123456",
                                               host="127.0.0.1",
                                               port="5433",
                                               database="django_db")
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            # Курсор для выполнения операций с базой данных
            self.cursor = self.connection.cursor()
            print('База данных готова к работе')
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        # finally:
        # if self.connection:
        # self.cursor.close()
        # else:
        # self.connection.close()
        # print("Соединение с PostgreSQL закрыто")

    def create_table(self, name_table):
        self.cursor.execute(f'create table {name_table} (id integer primary key, name text);')
        print(f'База данны {name_table} создана!')

    def insert_table(self, form):
        self.cursor.execute(
            f'''insert into form (name,surname,gender) values ('{form.cleaned_data['name']}','{form.cleaned_data['surname']}','{form.cleaned_data['gender']}');''')

    def delete_line(self, name_table, column, value):
        self.cursor.execute(f'''delete from '{name_table}' where '{column}'='{value}';''')

    def select_data(self):
        self.cursor.execute(f'select * from form;')
        data = self.cursor.fetchone()
        return print(data)


class NameForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    surname = forms.CharField(label='Фамилия', max_length=100)
    gender = forms.ChoiceField(label='Пол', choices=[('man', 'М'), ('woman', 'Ж')])

my_db = DB()

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # global my_db
            # my_db.insert_table(form=form)
            # b = my_db.select_data()
            return HttpResponseRedirect('https://vk.com')
            return HttpResponse(b)
    else:
        form = NameForm()
        return render(request, 'name.html', {'form': form})


def get_name1(request):
     if request.method == 'POST':
     #if request.method == 'POST':
         # { % csrf_token %} в форме обязательно указать а то не будет работать
        # request.encoding = 'UTF-8'
        # print(request.encoding)
        x = request.POST.copy()
        print(x)
        # x = request.GET.copy()
        # запрос обрабатывается WSGI который переводит заголовки HTTP запроса
        # в переменные окружения, т.е. они становятся аргументами объекта request
        # request.POST возвращает QueryDict - словарь тела запроса (в которой передается форма)
        # где занчение предствалено списком
        s = x.items()
        # возвращает генератор
        #print('Влажность {}'.format(x.get('hum')))
        #print('Температура {}'.format(x.get('temp')))
        # temp = x.get('temp')
        # global temp_list
        # temp_list.append(temp)
        # print(temp_list)
        for i in range(len(x)):
                 print(next(s))
            # итерируется по генератору и выдает значения ключ и значения в виде tuple
         # name = request.POST.get('name')
          #return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        return HttpResponse("<h2>Hello</h2>")
     else:
        return render(request, r'D:\prog\project\templates\post_json.html')


def get_name_json(request):
    if request.method == 'POST':
        data = loads(request.body)
        del data['csrfmiddlewaretoken']
        print(data)
        data_list = []
        for key, val in data.items():
            data_list.append(val)
        print(data_list)
        return HttpResponse("<h2>Hello</h2>")
    else:
        return render(request, r'D:\prog\project\templates\post_json.html')
