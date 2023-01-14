from django.shortcuts import render,redirect,HttpResponse
from django.http import FileResponse
from .models import filed
from captcha.image import ImageCaptcha
from random import randint
from io import BytesIO
from django.contrib import messages
import base64,os
from fileshare import settings
# Create your views here.
def getrandomchar():
    charlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    chars = ''
    for i in range(4):
        chars += charlist[randint(0,35)]
    image = ImageCaptcha().generate_image(chars)
    f = BytesIO()
    image.save(f, 'jpeg')
    data = f.getvalue()
    data = base64.b64encode(data).decode()
    return "data:image/jpg;base64,"+data,chars

def filedef(request):
    obj=filed.objects.all()
    return render(request,'../template/file.html',{'obj':obj})

def fileddef(request,a):
    obj=filed.objects.get(duuid=a)
    return render(request,'../template/filed.html',{'obj':obj})

def fileddefs(request,a):
    obj=filed.objects.get(id=a)
    return redirect('/'+str(obj.duuid)+'/')

def getcaptcha(request):
    img,chars=getrandomchar()
    request.session['captcha']=chars
    return HttpResponse(img)

def downloadfile(request):
    if request.POST.get("captcha")==request.session.get('captcha'):
        obj=filed.objects.get(duuid=request.POST.get("files"))
        filename=os.path.abspath(os.path.join(str(settings.MEDIA_ROOT),str(obj.filedf)))
        fip=open(filename,'rb')
        response=FileResponse(fip)
        response['Content-Type']='application/octet-stream'
        response['Content-Disposition']='attachment;filename="{}"'.format(
            os.path.basename(filename).encode('utf-8').decode('ISO-8859-1')
        )
        return response
    else:
        messages.add_message(request, messages.INFO,'验证码错误')
        return redirect('/'+request.POST.get("files")+'/')