from django.shortcuts import redirect
from handlescan.models import File
import os

from django.views import View
from django.http import HttpResponse, Http404, HttpResponseRedirect

# from qrgen.models import QrCode
from .models import QrCode 
# 
from .models import File

# Create your views here.

def dynamic_code_scan(request, code_id, *args, **kwargs):
    qrcode = QrCode.objects.get(id=code_id)
    qrcode.scan_count += 1

    # get the qrcode action_type

    if qrcode.type != 'PDF':
        qrcode.scan_count += 1
        qrcode.save()
        # get and redirect to the qrcode action_url
        return redirect(qrcode.action_url)

    else:
        # get file_id from code
        # file = File.objects.get(id=qrcode.file_id)
        qrcode.scan_count += 1
        qrcode.save()
        return HttpResponseRedirect('download', args=(qrcode.file_id,))

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
