
from django.shortcuts import render_to_response,get_object_or_404
from notice.models import Story,Category

# Create your views here
def home(request):
    base_qset = Story.objects.all().filter(status=3)
    latest_notice_list = base_qset.filter(category__id__exact=2)[:10]
    notice_category = get_object_or_404(Category, id=2)
    
    latest_news_list = base_qset.filter(category__id__exact=1)[:10]
    news_category = get_object_or_404(Category, id=1)
     
    latest_trends_list = base_qset.filter(category__id__exact=3)[:10]
    trends_category = get_object_or_404(Category, id=3)
    
    latest_media_list = base_qset.filter(category__id__exact=4)[:10]
    media_category = get_object_or_404(Category, id=4)
     
    context = {'notice':{'category':notice_category,'items': latest_notice_list}, 
              'news':{'category':news_category,'items': latest_news_list}, 
              'trends':{'category':trends_category,'items': latest_trends_list},
              'media':{'category':media_category,'items': latest_media_list}}
    return render_to_response('index.html', context)
def about_us(request):
    return render_to_response('about_us.html')
def info_center(request):
    base_qset = Story.objects.all().filter(status=3)
    latest_notice_list = base_qset.filter(category__id__exact=2)[:10]
    notice_category = get_object_or_404(Category, id=2)
    
    latest_news_list = base_qset.filter(category__id__exact=1)[:10]
    news_category = get_object_or_404(Category, id=1)
     
    latest_trends_list = base_qset.filter(category__id__exact=3)[:10]
    trends_category = get_object_or_404(Category, id=3)
    
    latest_media_list = base_qset.filter(category__id__exact=4)[:10]
    media_category = get_object_or_404(Category, id=4)
     
    context = [{'category':notice_category,'items': latest_notice_list}, 
              {'category':news_category,'items': latest_news_list}, 
              {'category':trends_category,'items': latest_trends_list},
              {'category':media_category,'items': latest_media_list}]
    return render_to_response('info_center.html', {'content_list':context})
    
def recruitment(request):
    recinfo_list = Story.objects.all().filter(status=3,category__id__exact=5)[:10]
    category = get_object_or_404(Category, id=5)
     
    context = {'category':category,'story_list': recinfo_list} 
    return render_to_response('recruitment.html', context)
def search(request):
    return render_to_response('search.html')
    