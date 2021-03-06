from django.shortcuts import render
from django.http import HttpResponse
from .forms import EncryptForm
from .forms import DecryptForm
from imsafe.settings import MEDIA_ROOT
from django.core.files.uploadedfile import SimpleUploadedFile
# from . import encrypt_img_slice as enc
# from . import encrypt_img_slice as Encryption
# from . import decrypt_img_slice as Decryption
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'web/index.html') 

# def encrypt(request):

#     if request.method == 'POST':
#         form = EncryptForm(request.POST, request.FILES)

#         if form.is_valid():
#             image = request.FILES['image']
#             fs = FileSystemStorage()
#             image_filename = fs.save(image.name, image)
#             uploaded_file_url = fs.url(image_filename)
            
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
            
#             if password == repeat_password:
#                 Encryption.encrypt(password, image_filename)
                
#                 context = {
#                     'form' : EncryptForm(),
#                     'img' : image_filename
#                 }
#             else:
#                 return HttpResponse('don\'t matched')
#         else:
#             return HttpResponse('not valid') 

#     else:
#         context = {
#             'form' : EncryptForm()
#         }
        
#     return render(request, 'web/encrypt.html', {'context': context})

# def decrypt(request):
#     if request.method == 'POST':
#         form = DecryptForm(request.POST, request.FILES)

#         if form.is_valid():
#             image = request.FILES['image']
#             public_key = request.FILES['public_key']
#             signature = request.FILES['signature']

#             fs = FileSystemStorage()
#             public_key_filename = fs.save(public_key.name, public_key)
#             signature_filename = fs.save(signature.name, signature)
#             image_filename = fs.save(image.name, image)
#             uploaded_file_url = fs.url(image_filename)

#             password = form.cleaned_data['password']
            
#             result = Decryption.decrypt(password, image_filename, public_key_filename, signature_filename)

#             if result:
#                 context = {
#                     'form' : DecryptForm(),
#                     'img' : image_filename,
#                 }
#             else:
#                 context = {
#                     'form' : DecryptForm(),
#                     'msg' : 'The signature is not valid!'
#                 }
#     else:
#         context = {
#                 'form' : DecryptForm(),
#             }
            
#     return render(request, 'web/decrypt.html', {'context': context})
