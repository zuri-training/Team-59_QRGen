from django.shortcuts import render
import qrcode
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import QrCode

# Create your views here.

class QrListView(ListView):

    model = QrCode     

    template_name = 'qrgen/list.html'

    context_object_name = 'qrimage'


class QrDetailView(DetailView):

    model = QrCode

    template_name = 'qrgen/detail.html'

    context_object_name = 'qrimage'


class QrUpdateView(UpdateView):

    template_name = 'qrgen/update.html'

    model = QrCode

    fields = ['title']

    success_url = reverse_lazy('qrimage:list')


class QrDeleteView(DeleteView):

    template_name = 'photoapp/delete.html'

    model = QrCode

    success_url = reverse_lazy('qrimage:list')


def dashboard(request):
    return render(request, 'qrgen/dashboard.html')


def dashboard_website(request):
    data = ''
    img = ''
    if request.method == 'POST':
        data = request.POST['website']
        img = qrcode.make(data)
        img.save('qrgen/static/img/qrcode.png')

    user_dict = {'data': data, 'img': img}
    return render(request, 'qrgen/dashboard.html', user_dict)


def dashboard_email(request):
    data = ''
    img = ''
    if request.method == 'POST':
        data = request.POST['email']
        img = qrcode.make(data)
        img.save('qrgen/static/img/qrcode.png')

    user_dict = {'data': data, 'img': img}
    return render(request, 'qrgen/dashboard.html', user_dict)


def dashboard_text(request):
    data = ''
    img = ''
    if request.method == 'POST':
        data = request.POST['text']
        img = qrcode.make(data)
        img.save('qrgen/static/img/qrcode.png')

    user_dict = {'data': data, 'img': img}
    return render(request, 'qrgen/dashboard.html', user_dict)


def dashboard_whatsapp(request):
    data = ''
    img = ''
    if request.method == 'POST':
        data = request.POST['whatsapp']
        img = qrcode.make(data)
        img.save('qrgen/static/img/')

    user_dict = {'data': data, 'img': img}
    return render(request, 'qrgen/dashboard.html', user_dict)


def dashboard_website_2(request):
    data = ''
    img = ''
    if request.method == 'POST':
        data = request.POST['website']
        img = qrcode.make(data)
        img.save('qrgen/static/img/qrcode.png')

    user_dict = {'img': img}
    return render(request, 'qrgen/dashboard2.html', user_dict)


def dashboard_email_2(request):
    data = ''
    img = ''
    if request.method == 'POST':
        data = request.POST['email']
        img = qrcode.make(data)
        img.save('qrgen/static/img/qrcode.png')

    user_dict = {'img': img}
    return render(request, 'qrgen/dashboard2.html', user_dict)


def dashboard_text_2(request):
    data = ''
    img = ''
    if request.method == 'POST':
        data = request.POST['text']
        img = qrcode.make(data)
        img.save('qrgen/static/img/qrcode.png')

    user_dict = {'img': img}
    return render(request, 'qrgen/dashboard2.html', user_dict)


def dashboard_whatsapp_2(request):
    data = ''
    img = ''
    if request.method == 'POST':
        data = request.POST['whatsapp']
        img = qrcode.make(data)
        img.save('qrgen/static/img/qrcode.png')

    user_dict = {'img': img}
    return render(request, 'qrgen/dashboard2.html', user_dict)


# def website(request):
#     data = ''
#     img = ''
#     if request.method == 'POST':
#         data = request.POST['url']
#         img = qrcode.make(data)

#     user_dict = {'data': data, 'img': img}
#     return render(request, 'qrgen/dashboard.html', user_dict)


# def text(request):
#     data = ''
#     img = ''
#     if request.method == 'POST':
#         data = request.POST['text']
#         img = qrcode.make(data)

#     user_dict = {'data': data, 'img': img}
#     return render(request, 'qrgen/dashboard.html', user_dict)


# def whatsapp(request):
#     data = ''
#     img = ''
#     if request.method == 'POST':
#         data = request.POST['phone_number']
#         img = qrcode.make(data)

#     user_dict = {'data': data, 'img': img}
#     return render(request, 'qrgen/dashboard.html', user_dict)
