from django.shortcuts import render
# from django.http import HttpResponse
# from appTwo.models import User
from main_app.forms import NewUserForm
from django.views.generic import TemplateView

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class BushcraftView(TemplateView):
    template_name = 'bushcraft.html'

class TenkaraView(TemplateView):
    template_name = 'tenkara.html'

class PhotoView(TemplateView):
    template_name = 'photo.html'

class VideoView(TemplateView):
    template_name = 'video.html'

class MessageView(TemplateView):
    template_name = 'message.html'



def index(request):
    my_dict={'insert_me':'Now I am coming from main_app index.html !'}
    return render(request,'main_app/index.html',context=my_dict)

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'main_app/users.html',{'form':form})



# def about(request):
#     return render(request, 'main_app/about.html')
#
# def photo(request):
#     return render(request, 'main_app/photo.html')
#
# def video(request):
#     return render(request, 'main_app/video.html')
#
# def tenkara(request):
#     return render(request,'main_app/tenkara.html')
#
# def bushcraft(request):
#     return render(request,'main_app/bushcraft.html')
