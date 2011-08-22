# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
		(r'^registration/?$', 'wsgiadmin.domains.views.registration'),
		(r'^check/?$', 'wsgiadmin.domains.views.check'),
		(r'^add/?$', 'wsgiadmin.domains.views.add'),
		(r'^show/?$', 'wsgiadmin.domains.views.show'),
		(r'^show/([0-9]{1,11})/?$', 'wsgiadmin.domains.views.show'),
		(r'^rm/([0-9]{1,11})/?$', 'wsgiadmin.domains.views.rm'),
)
