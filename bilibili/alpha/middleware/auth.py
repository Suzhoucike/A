from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,render

class authmiddleware(MiddlewareMixin):
    def process_request(self,request):

        if request.path_info == '/base/' or request.path_info == '/base/register/':
            return

        info_dict = request.session.get("info")
        if info_dict:

            #print(request.session.get("info"))
            return

        return redirect('/base/')