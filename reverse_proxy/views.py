from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from wsgiref.util import is_hop_by_hop
from django.shortcuts import render
from django.contrib.auth import logout

def login_view(request):
    return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
@login_required
def reverse_proxy(request):
    """
    Reverse proxy for a remote service.
    """
    path = request.get_full_path()
    #Optionally, rewrite the path to fit whatever service we're proxying to.
    
    url = "http://%s%s" % ("localhost:8080", path)

    import requests
    requestor = getattr(requests, request.method.lower())
    
    proxied_response = requestor(url, data=request.body, files=request.FILES)
    
    from django.http.response import HttpResponse
    response = HttpResponse(proxied_response.content, content_type=proxied_response.headers.get('content-type'))
    for header_key, header_value in proxied_response.headers.items():
        if is_hop_by_hop(header_key) or header_key.lower() == 'set-cookie':
            continue
        else:
            response[header_key] = header_value
    return response
