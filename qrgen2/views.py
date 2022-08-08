from django.shortcuts import render
from django.views import View

# Create your views here.


# @login_required
class GenerationDashboardView(View):
    def get(request):
        pass
        # user = request.user

    def post(request):
        pass

# @login_required
class MainDashboardView(View):
    def get(request):
        # user = request.user
        # user_codes = QrCode.objects.all().filter(user_id=user.id)
        # download_options = {1:'png', 2:'jpeg', 3:'pdf'}
        # context
        # - user
        # - user_codes

        # - download_options        
        pass


    def post(request):
        # 
        # delete
        # download
        # 
        pass
