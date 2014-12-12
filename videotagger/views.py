import json, subprocess
import time
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import UploadVideoForm
from .models import Video, Tag, Evaluation

from videotagger import overseer

def index(request):
  if request.method == 'POST':
    if request.POST['formName'] == 'tagUpload':
      tags = request.POST.get('tags', 'msg')
      form = UploadVideoForm()
      tags = json.loads(tags)
      vidId = request.session['vidid']
      for t in tags:
        tag = Tag(x = t["x"], y = t["y"], r = t["rad"], time = t["time"], tagNum = t["tagNum"], video = Video.objects.get(pk=vidId))
        tag.save()
      overseer.analyze(str(vidId))
      msg = "Tags received."
#        subprocess.call(['python3', '/home/django/squatcop/videotagger/overseer.py', str(request.session['vidid'])])
#      while(True):
#        setOfEvals = Evaluation.objects.filter(pk=vidId)
#        if (len(setOfEvals) > 0):
#          msg = setOfEvals[0].evaluation
#          break 
#        time.sleep(3)
    else:
      form = UploadVideoForm(request.POST, request.FILES)
      if form.is_valid():
        video = Video(vidpath = request.FILES['video'])
        video.save()
        request.session['vidpath'] = video.vidpath.url
        request.session['vidid'] = video.id
        vidpath = video.vidpath.url
        msg = vidpath
  else:
    msg = ''
    form = UploadVideoForm()
  if 'vidpath' in request.session:
    vidpath = request.session['vidpath']
  else:
    vidpath = ""
  return render(request, 'videotagger/index.html', {'msg': msg, 'form': form, 'vidpath': vidpath})

def results(request):
  vidId = request.session['vidid']
  header = request.session['vidpath']
  evalSet = Evaluation.objects.filter(video_id=vidId)
  if (len(evalSet) > 0):
    results = evalSet
  else:
    results = [] 
  return render(request, 'videotagger/results.html', {'results': results, 'header': header})

def sample(request):
  return render(request, 'videotagger/sample.html')  
