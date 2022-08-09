from email.mime import image
from django.shortcuts import render
import qrcode
from .models import *

# Create your views here.


# def dashboard(request):
#     return render(request, 'qrgen/index.html')


def generation_dashboard(request):
    data = ''
    img = ''
    url = ''
    file = ''
    code_generated = ''
    if request.method == 'POST':
        data = request.POST
        if 'generate' in data:
            if 'url' in request.POST:
                url = request.POST['url']
            elif 'file-upload' in request.POST:
                file = request.FILES['file-upload']
        # type = QrType.objects.get(name=request.POST['qrcode_type'])
        # QrCode.objects.create(
        #     user=request.user,
        #     # type=type,
        #     image=request.img
        # )
        if url:
            img = qrcode.make(url)
            img.save('qrgen/static/img/qrcode.png')

        elif file:
            img = qrcode.make(file)
            img.save('qrgen/static/img/qrcode.png')

    user_dict = {'url': url, 'file': file, 'img': img, 'ok': 'yes'}
    return render(request, 'qrgen/index.html', user_dict)


# def dashboard_email(request):
#     data = ''
#     img = ''
#     if request.method == 'POST':
#         data = request.POST['email']
#         img = qrcode.make(data)
#         img.save('qrgen/static/img/qrcode.png')

#     user_dict = {'data': data, 'img': img}
#     return render(request, 'qrgen/dashboard.html', user_dict)


# def dashboard_text(request):
#     data = ''
#     img = ''
#     if request.method == 'POST':
#         data = request.POST['text']
#         img = qrcode.make(data)
#         img.save('qrgen/static/img/qrcode.png')

#     user_dict = {'data': data, 'img': img}
#     return render(request, 'qrgen/dashboard.html', user_dict)


# def dashboard_whatsapp(request):
#     data = ''
#     img = ''
#     if request.method == 'POST':
#         data = request.POST['whatsapp']
#         img = qrcode.make(data)
#         img.save('qrgen/static/img/')

#     user_dict = {'data': data, 'img': img}
#     return render(request, 'qrgen/dashboard.html', user_dict)


# def dashboard_website_2(request):
#     data = ''
#     img = ''
#     if request.method == 'POST':
#         data = request.POST['website']
#         img = qrcode.make(data)
#         img.save('qrgen/static/img/qrcode.png')

#     user_dict = {'img': img}
#     return render(request, 'qrgen/dashboard2.html', user_dict)


# def dashboard_email_2(request):
#     data = ''
#     img = ''
#     if request.method == 'POST':
#         data = request.POST['email']
#         img = qrcode.make(data)
#         img.save('qrgen/static/img/qrcode.png')

#     user_dict = {'img': img}
#     return render(request, 'qrgen/dashboard2.html', user_dict)


# def dashboard_text_2(request):
#     data = ''
#     img = ''
#     if request.method == 'POST':
#         data = request.POST['text']
#         img = qrcode.make(data)
#         img.save('qrgen/static/img/qrcode.png')

#     user_dict = {'img': img}
#     return render(request, 'qrgen/dashboard2.html', user_dict)


# def dashboard_whatsapp_2(request):
#     data = ''
#     img = ''
#     if request.method == 'POST':
#         data = request.POST['whatsapp']
#         img = qrcode.make(data)
#         img.save('qrgen/static/img/qrcode.png')

#     user_dict = {'img': img}
#     return render(request, 'qrgen/dashboard2.html', user_dict)
