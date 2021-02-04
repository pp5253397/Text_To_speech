from django.shortcuts import render,redirect,HttpResponse
from .models import UserDetails, Audios_Data, TXT_Txt_Speech
from gtts import gTTS
from MainPro.settings import BASE_DIR
import os
import calendar; 
import time; 

import speech_recognition as sr 
import pyttsx3  
from .forms import UserForm

from googletrans import Translator
import googletrans



def LoginView(request):
    if request.POST:
        try:
            model = UserDetails.objects.get(user_email = request.POST['user_email'])
            if model.password == request.POST['password']:
                request.session['email'] = model.user_email
                return redirect('index')
            else:
                return HttpResponse("<a href = ''>Incorrect Details</a>")
        except:
            return HttpResponse("<a href = ''>Incorrect Details</a>")
    return render(request,'login.html')

def RegisterView(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request,'registration.html')


def IndexView(request):
    if request.session.has_key('email'):
        
        user = request.session['email']
        if request.POST:
            text_data = request.POST['Text_DAta']
            lang_data = request.POST['language']
            print(lang_data)
            print(text_data)
            # lang = ""
            # if lang_data == 'hindi':
            #     lang = 'hi'
            # elif lang_data == 'gujarati':
            #     lang = 'gu'
            # elif lang_data == 'marathi':
            #     lang = 'mr'
            # else:
            #     lang = 'en'
                
            file = gTTS(text_data,lang=lang_data)
            print(file)
            
            # gmt stores current gmtime 
            gmt = time.gmtime() 
            print("gmt:-", gmt) 
            
            # ts stores timestamp 
            ts = calendar.timegm(gmt) 
            print("timestamp:-", ts) 
            
            path_name = "files\\" + str(ts) + ".mp3"
            file.save(os.path.join(BASE_DIR, path_name))
            
            obj = Audios_Data()
            obj.audio_name = str(ts)
            obj.audio_data = str(ts) + ".mp3"
            obj.save()
            # link = os.path.join(BASE_DIR, "files/" + str(ts) + ".mp3")
            
        data = Audios_Data.objects.order_by('-id')[0]
        lang_trans = googletrans.LANGUAGES
        
        if request.GET:
            translator = Translator()
            text_trans = str(request.GET.get('text_translate'))
            from_lang = str(request.GET.get('from_lang'))   
            to_lang = str(request.GET.get('to_lang'))  
            result = translator.translate(text_trans, src=from_lang, dest=to_lang)
            print(result.text)
            return render(request,'index.html',{'user':user,'data':data,'lang_trans':lang_trans,'result':result.text})
        return render(request,'index.html',{'user':user,'data':data,'lang_trans':lang_trans})
    else:
        return redirect('login')

def logout(request):
    if request.session.has_key('email'):
        user = request.session['email']
        del user
        return redirect('login')
    else:
        return redirect('login')