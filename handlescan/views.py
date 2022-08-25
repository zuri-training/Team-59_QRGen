from django.shortcuts import redirect, render
import os
from django.http import HttpResponse, Http404, HttpResponseRedirect

from qrgen.models import QrCode, File

# for file download
import urllib.request
from urllib.parse import urlparse



# Create your views here.

def dynamic_code_scan(request, code_id, *args, **kwargs):
    qrcode = QrCode.objects.get(id=code_id)

    # getting the no of scans
    
    if qrcode.scan_count is not None:
        qrcode.scan_count += 1
    else:
        qrcode.scan_count = 1

    qrcode.save()

    # get the qrcode action_type
    uploads = ['pdf', 'biz', 'img']

    # if dynamic, these types won't autoredirect, will give us headache instead
    email_txt = ['eml', 'txt']
    print('type: ', qrcode.type)
    if qrcode.action_type not in uploads and qrcode.action_type not in email_txt:
        # get and redirect to the qrcode action_url
        print('qrcode.type not in uploads and qrcode.type not in email_txt')
        return redirect(qrcode.input_url)

    else:
        if qrcode.action_type == 'eml':

            # open the default mail app and compose main to the input email address

            return render(request, 'email.html', {'email':qrcode.input_url})
        
        elif qrcode.action_type == 'txt':

            # for text input
            # 
            # return redirect()
            pass
            
        else:
            # if it was an uploaded file (if qrcode.type in uploads)

            return HttpResponseRedirect('download', args(qrcode.file_id, ))


def download(request, file_id):
    file = File.objects.get(id=file_id)

    if file is not None:
        parse_url = urlparse(file.file.url)
        path = urllib.request.urlopen(file.file.url)
        response = HttpResponse(path.read(), content_type="application/adminupload")
        response['Content-Disposition'] = 'inline;filename=' + os.path.basename(parse_url.path)
        return response
    else:
        return Http404