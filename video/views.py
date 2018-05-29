from __future__ import unicode_literals

from django.conf import settings
from django.views import generic


class HomepageView(generic.TemplateView):
    template_name = 'video/homepage.html'

    def get_context_data(self):
        context = super().get_context_data()
        opentok_session = settings.OPENTOK.create_session()
        session_id = opentok_session.session_id
        opentok_token = settings.OPENTOK.generate_token(session_id)
        context['OPENTOK'] = dict(
            key=settings.OPENTOK_API_KEY, session=session_id,
            token=opentok_token)
        return context


class LoginView(generic.TemplateView):
    template_name = 'video/login.html'
