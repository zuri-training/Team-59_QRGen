from django.shortcuts import render
from django.views import View
import qrcode
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
# for manipulating our models
from .models import QrCode, QrType, File
# for the ajax request
from django.http import JsonResponse
from django.core import serializers
# for manipulating folders
from QRGenProject.settings import BASE_DIR
import os
# for image conversion
from PIL import Image


def create_or_get_types():

    if (len(QrType.objects.all())) == 0:
        code_types = ['dynamic', 'static']

        for code_type in code_types:
            QrType.objects.create(
                name=code_type
            )

    return QrType.objects.all()

# @login_required(login_url='/admin/login/')
# this should be the default user login (i.e. /accounts/login/)
# note: this is for FBV, for CBV, we use LoginRequiredMixin


class GenerationDashboardView(LoginRequiredMixin, View):
    login_url = '/admin/login/'

    def get(self, request):

        QrTypes = create_or_get_types()

        context = {
            'code_types': QrTypes,
        }

        return render(request, 'qrgen/generation.html', context)

    def post(self, request):

        # if request.is_ajax

        if 'generate' in request.POST:

            # collecting form data (url...qrcode_type, action_type)

            form_data = request.POST

            # get qr_type (from database)

            type = QrType.objects.get(name=request.POST['qrcode_type'])

            # partially create a qrcode object

            QrCode.objects.create(
                user=request.user,
                type=type,
                action_type=form_data['action_type'],
            )

            uploads = ['pdf', 'img', 'biz']

            # add the qrcode object's action url

            # - get the last added qrcode object
            this_qrcode = QrCode.objects.all().last()

            if this_qrcode.action_type not in uploads:
                # it is a url not a file uploaded
                this_qrcode.input_url = form_data['url']
                this_qrcode.save()

            else:
                # it is either a pdf or image upload
                # create a File object
                File.objects.create(
                    user=request.user,
                    name=request.FILES['upload_file'].name,
                    file=request.FILES['upload_file'],
                )

                # get the created file
                created_file = File.objects.all().last()

                # add the created file to the QrCode object
                this_qrcode.file = created_file
                this_qrcode.save()

            if this_qrcode.type.name == 'dynamic':
                # - this is the url that the qrcode should point to either ways
                # --- (be it upload or url, so long as it is dynamic)
                this_qrcode.action_url = request.build_absolute_uri(
                    f'/dynamic/{this_qrcode.id}')

            else:
                this_qrcode.is_dynamic = False

                # qrcode is static type
                this_qrcode.action_url = form_data['url']

            this_qrcode.save()

            # having saved the QrCode object, (and a File object (if it was and uploaded file)),
            # we now generate a qrcode image with the QrCode's action_url
            # create a folder to store all the qrcode images if it doesn't exist

            folder_path = BASE_DIR / 'qrgen/static/img/qrcodes/'
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            print(folder_path)
            qr_img = qrcode.make(this_qrcode.action_url)
            
            # folder for the qrcode being created

            qr_folder_path = BASE_DIR / f'qrgen/static/img/qrcodes/{this_qrcode.id}/'

            if not os.path.exists(qr_folder_path):
                os.makedirs(qr_folder_path)
            print(qr_folder_path)
            img_path = f'qrgen/static/img/qrcodes/{this_qrcode.id}/qrcode-{this_qrcode.id}.png'
            qr_img.save(img_path)

            # add the qr_img to the QrCode object
            this_qrcode.img = img_path

            this_qrcode.save()
            
            # Converting the png QR code to JPG
            img_png = Image.open(img_path)
            img_path = img_png.convert("RGB")
            img_path = f'qrgen/static/img/qrcodes/{this_qrcode.id}/qrcode-{this_qrcode.id}.jpeg'
            qr_img.save(img_path)

            # Converting the png QR code to PDF 
            img_path = img_png.convert("RGB")
            img_path = f'qrgen/static/img/qrcodes/{this_qrcode.id}/qrcode-{this_qrcode.id}.pdf'
            qr_img.save(img_path)

            # serialize the new qrcode object
            ser_qrcode = serializers.serialize('json', [this_qrcode, ])
            # send to client site
            return JsonResponse({"qrcode": ser_qrcode}, status=200)
        else:
            return JsonResponse({"error": ""}, status=400)



class MainDashboardView(LoginRequiredMixin, View):
    login_url = '/admin/login'

    def get(self, request):
        user_codes = QrCode.objects.all().filter(user_id=request.user.id).order_by('-date_gen')
        download_options = {1: 'png', 2: 'jpeg', 3: 'pdf'}
        active_codes = user_codes.filter(is_active=True)

        context = {
            'qrcodes': user_codes,
            'code_count': user_codes.count(),
            'active_codes': active_codes,
            'active_count': active_codes.count(),
            'download_options': download_options,
        }
        return render(request, 'qrgen/dashboard.html', context)

    def post(request):
        return HttpResponseRedirect(reverse('qrgen:dashboard'))


class EditQrCode(LoginRequiredMixin, View):
    login_url = '/admin/login'

    def get(self, request):
        return HttpResponseRedirect(reverse('qrgen:dashboard'))
    
    def post(self, request, code_id):
        qrcode = QrCode.objects.get(id=code_id)
        if 'change_content' in request.POST:
            new_url = request.POST['new_content']
            qrcode.input_url = new_url
        elif 'change_title' in request.POST:
            new_title = request.POST['new_title']
            qrcode.title = new_title
        qrcode.save()

        return HttpResponseRedirect(reverse('qrgen:dashboard'))
    
class DeleteQrCode(LoginRequiredMixin, View):
    login_url = '/admin/login'

    def get(self, request, code_id):
        qrcode = QrCode.objects.get(id=code_id)
        qrcode.delete()
        return HttpResponseRedirect(reverse('qrgen:dashboard'))
    
    def post(self, request, code_id):
        return HttpResponseRedirect(reverse('qrgen:dashboard'))


def download(request, code_id, type):
    try:
        file_path = BASE_DIR / f'qrgen/static/img/qrcodes/{code_id}/qrcode-{code_id}.{type}'
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    except:
        # return HttpResponse('File does not exit!!!')
        raise HttpResponse('error')
