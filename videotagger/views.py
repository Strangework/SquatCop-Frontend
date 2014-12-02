from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import UploadVideoForm
from .models import AnnoVideo

def index(request):
  if request.method == 'POST':
    if request.POST['formName'] == 'tagUpload':
      msg = request.POST.get('tags', 'msg')
    else:
      msg = "Video uploaded."
      form = UploadVideoForm(request.POST, request.FILES)
      if form.is_valid():
        video = AnnoVideo(vidpath = request.FILES['video'])
        video.save()
        request.session['vidpath'] = video.vidpath.url
        vidpath = video.vidpath.url
  else:
    msg = 'msg'
    form = UploadVideoForm()
  if 'vidpath' in request.session:
    vidpath = request.session['vidpath']
  else:
    vidpath = ""
  return render(request, 'videotagger/index.html', {'msg': msg, 'form': form, 'vidpath': vidpath})

def upload(request):
  if request.method == 'POST':
    form = UploadVideoForm(request.POST, request.FILES)
    msg = "AGGH"
    if form.is_valid():
      video = AnnoVideo(vidpath = request.FILES['video'])
      video.save()
      request.session['vidpath'] = video.vidpath.url
      msg = "FINALLY."
  else:
    msg = "YOU BITCH"
    form = UploadVideoForm()
  return render(request, 'videotagger/upload.html', {'form': form, 'msg': msg})

