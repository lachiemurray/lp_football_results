from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
import simplejson
import urllib2
from datetime import datetime, timedelta
import time
import hashlib
import json

def edition(request):
       
    if not request.GET.get('competition', False):
        return HttpResponse("Error: No competition was provided", status=400)
    
    
    # Get competition
    competition = request.GET['competition']
    
    tomorrow = datetime.now() + timedelta(days=1)
     
    # Get fixtures - need good API

    # Check if there are games today
    #if not data
    #    return HttpResponse("No fixtures today", status=406)
    
    context = { 'greeting' : 'blank' }
    response = render(request, 'lp_football_results/index.html', context)
    response['ETag'] = hashlib.sha224(competition+datetime.now().strftime('%d%m%Y')).hexdigest()
    
    return response

def sample(request):
    
    competition = 'Premier League'
    
    fixtures = [
    {'team_1':'Arsenal','team_2':'Liverpool','kick_off':'15:00','score_1':'4','score_2':'0','status':'R'},
    {'team_1':'Bolton','team_2':'Fulham','kick_off':'15:00','score_1':'1','score_2':'3','status':''},
    {'team_1':'Everton','team_2':'Stoke City  ','kick_off':'15:00','score_1':'3','score_2':'1','status':'R'},
    {'team_1':'Hull City','team_2':'Newcastle','kick_off':'15:00','score_1':'1','score_2':'1','status':'R'},
    {'team_1':'Man United','team_2':'Liverpool','kick_off':'15:00','score_1':'1','score_2':'4','status':'R'},
    {'team_1':'Middlesbrough','team_2':'Portsmouth','kick_off':'15:00','score_1':'1','score_2':'1','status':'R'},
    {'team_1':'Sunderland','team_2':'Wigan','kick_off':'15:00','score_1':'1','score_2':'2','status':'R'},
    ]
    
    context = { 'competition' : competition, 'fixtures' : fixtures }
    
    response = render(request, 'lp_football_results/index.html', context )
    response['ETag'] = hashlib.sha224(competition+(time.strftime('%d%m%Y'))).hexdigest()
    
    return response

@csrf_exempt
def validate_config(request):
    
    json_response = {'errors': [], 'valid': True}

    # Extract config from POST
    user_settings = json.loads(request.POST['config'])
    
    # If the user did choose a competition:
    if not user_settings.get('competition', None):
        json_response['valid'] = False
        json_response['errors'].append('Please select a language from the select box.')

    # Create response
    response = HttpResponse(json.dumps(json_response), mimetype='application/json')

    return response


# Alternatively, configure webserver to serve this content
def meta_json(request):
    
    return HttpResponseRedirect('/static/lp_hello_django/meta.json')

# Alternatively, configure webserver to serve this content
def icon(request):
    
    return HttpResponseRedirect('/static/lp_hello_django/icon.png')
    
    
    
    
    
    
    
    
