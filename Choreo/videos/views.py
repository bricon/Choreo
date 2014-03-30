from django.shortcuts import render, get_object_or_404
from videos.models import Video
from django.http import HttpResponse

def index(request):
    latest_video_list = Video.objects.all().order_by('-pub_date')[:5]
    context = {'latest_video_list': latest_video_list}
    return render(request, 'videos/index.html', context)

def detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'videos/detail.html', {'video': video})