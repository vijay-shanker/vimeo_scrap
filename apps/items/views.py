# Create your views here.
from django.views.generic.base import TemplateView, View
from django.shortcuts  import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import json
from django.core import serializers
json_serializer = serializers.get_serializer("json")()

from apps.items.models import Item
class Home(View):
    def get(self,request, *args, **kwargs):
        return render_to_response('items/search_page.html', context_instance = RequestContext(request) )

def search_core(request):
    keyword = request.GET['keyword']
    filter_q = request.GET['filter']
    if keyword:
        response_obj = Item.objects.filter(username__icontains=keyword)
    else:
        response_obj = Iem.objects.all()
    if filter_q == 'all':
        pass
    elif filter_q == 'paying':
        response_obj = response_obj.filter(is_paying_user=True)[:10]
    elif filter_q == 'uploaded':
        response_obj = response_obj.filter(has_uploaded=True)[:10]
    elif filter_q == 'staff_pick':
        response_obj = response_obj.filter(is_staff_pick=True)[:10]
    if response_obj.count() == 0:
        return HttpResponse('No results Found')
    response_string = []
    response_string.append('<table>')
    for each in response_obj:
        response_string.append('<tr><td>username: %s </td><tr><td>Profile link: %s </td></tr>\
    <tr><td>is_paying_user: %s</td></tr>\
    <tr><td>is staff pick: %s</td></tr><tr><td><td></tr><'%(each.username, each.userprofile,each.is_paying_user,each.is_staff_pick))
    response_string.append('</table>')
    response_string = ''.join(response_string)
    return HttpResponse(response_string)
