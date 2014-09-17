from django.shortcuts import render,get_object_or_404,render_to_response
from models import Story,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def notice_detail(request,slug):
    story = get_object_or_404(Story,slug=slug)
    return render(request, 'notice_detail.html', {'story': story})

def category(request, slug):
    """Given a category slug, display all items in a category."""
    category = get_object_or_404(Category, slug=slug)
    object_list = Story.objects.filter(category=category)
    
    paginator = Paginator(object_list, 25) # Show 25 contacts per page
    page = 1
    if request.GET.get('page'):
        page = request.GET.get('page')
    try:
        story_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        story_list = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        story_list = paginator.page(paginator.num_pages)

#    heading = "category: %s" % category.label
    heading = { "category" : category}
    return render_to_response("story_list.html", locals())