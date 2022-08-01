from django.shortcuts import  render
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404

from .forms import PdfUploadForm
from qrgen.models import File

import os

# Create your views here.

def home(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'home.html', context)

def dashboard(request, pk):
    user = User.objects.get(id=pk)

    if request.method == 'GET':
        context = {
                'user': user,
                'form': PdfUploadForm,
                'codes': reload_user_files(request, pk),
            }
        return render(request, 'dashboard.html', context)

    elif request.method == 'POST':
        context = {
                'user': user,
                'form': PdfUploadForm,
                'codes': reload_user_files(request, pk),
            }
        
        '''
        At this point, a QRCode is generated using the link to the file download
        ie. request.build_absolute_uri(f"/download/{file.id}")

        After which it is save as a QRCode object (qrgen.models.QRCode)
        '''

        File.objects.create(
            user_id=pk,
            name=request.FILES['file'].name,
            file = request.FILES['file']
        )

        return render(request, 'dashboard.html', context)

def download(request, pk):
    try:
        file = File.objects.get(id=pk)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = BASE_DIR + file.file.url
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    except:
        # return HttpResponse('File does not exit!!!')
        raise Http404


def reload_user_files(request, user_id):
    user_files = File.objects.all().filter(user_id=user_id)
    user_qrcodes = {}
    
    for file in user_files:
        user_qrcodes[file.name] = str(request.build_absolute_uri(f'/download/{file.id}'))
    
    return user_qrcodes

