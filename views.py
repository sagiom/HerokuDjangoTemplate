# encoding: utf-8
"""
views.py

Created by morgan chang on 2010-09-03.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
from django.shortcuts import render_to_response
#from jinja_helper import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings

#load db
#from db.models import *

#add protection
from django.views.decorators.csrf import csrf_exempt, csrf_protect

#load login_required fund…
#from functions import web_login_required
#from util import *

import sys
import os

def index(request):
	msg = u'站台首頁'
	
#	nwObjs = news.objects.filter(position=u'首頁消息')

	return render_to_response('index.html',{'msg':msg})
