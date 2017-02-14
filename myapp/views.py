from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import ugettext as _

from django.utils import translation
from django.utils.translation import activate


# Create your views here.
class MyApp(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request,
                      context={'serverTitle_i18n': _("__server_title__"),
                               'serverBody_i18n': _("__server_body__")},
                      template_name='myapps.html')

    def post(self, request, *args, **kwargs):
        pass
