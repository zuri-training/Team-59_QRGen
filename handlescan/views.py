from django.shortcuts import redirect
import os
from django.http import HttpResponse, Http404, HttpResponseRedirect

from qrgen.models import QrCode, File

# Create your views here.

def dynamic_code_scan(request, code_id, *args, **kwargs):
    qrcode = QrCode.objects.get(id=code_id)

    # getting the no of scans
    
    if qrcode.scan_count is not None:
        qrcode.scan_count += 1
    else:
        qrcode.scan_count = 1

    # get the qrcode action_type
    uploads = ['pdf', 'biz', 'img']

    if qrcode.type not in uploads:
        # get and redirect to the qrcode action_url
        return redirect(qrcode.input_url)

    else:
        # get file_id from code
        # file = File.objects.get(id=qrcode.file_id)
        return HttpResponseRedirect('handlescan:download', args=(qrcode.file_id,))

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
