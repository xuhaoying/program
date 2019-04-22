from django.shortcuts import render

# Create your views here.
def parent_views(request):
    uname = 'Parent'
    return render(request, '01-parent.html', locals())

def child_views(request):
    uname = 'Child'
    return render(request, '01-child.html', locals())