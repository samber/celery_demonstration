
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from scanner.jobs.models import Credential
from scanner.jobs.tasks import fill_queue
from scanner.site.forms import SSHBruteforceForm

class Home(FormView):

    template_name = 'home.html'
    form_class = SSHBruteforceForm
    success_url = 'site.home'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['credentials'] = Credential.objects.all()
        return context

    def form_valid(self, form):
        fill_queue.delay({
            "from": "1.0.0.0",
            "gap": 10000,
            "username": form.cleaned_data["username"],
            "password": form.cleaned_data["password"],
        })
        return super(Home, self).form_valid(form)

    def get_success_url(self):
        return reverse(self.success_url)
