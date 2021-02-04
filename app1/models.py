from django.db import models

class UserDetails(models.Model):
    user_email = models.EmailField(unique = True)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.user_email 

class Audios_Data(models.Model):
    user_email = models.EmailField(blank = True)
    audio_name = models.CharField(default="", max_length=100)
    audio_data = models.FileField(upload_to='files', max_length=100)
    
    def __str__(self):
        return self.audio_name

class TXT_Txt_Speech(models.Model):
    user_email = models.EmailField(blank = True)
    TXT_File_data = models.FileField(upload_to='files', max_length=100)
    TXT_audio_name = models.CharField(default="", max_length=100)
    TXT_audio_data = models.FileField(upload_to='files', max_length=100)
    
    def __str__(self):
        return self.TXT_audio_name