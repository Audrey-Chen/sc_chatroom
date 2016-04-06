from django.conf.urls import url

import im.views

urlpatterns = [
    url(r'^login', im.views.login, name='login'),
    url(r'^message', im.views.msg_handler, name='message'),
] 