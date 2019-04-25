# In django, HttpResponse can respond to a piece of text in the client browser
from django.http import HttpResponse

def show_views(request):
    """
    View handlers that handle the business
    :param request:  The request object of this request encapsulates all the information in the request
    :return: The content of the response to the client
    """
    return HttpResponse("This is my first Django application.")

