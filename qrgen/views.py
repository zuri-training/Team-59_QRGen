from django.shortcuts import render
import qrcode

# Create your views here.


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
