from django.views.generic.base import RedirectView, TemplateView

class HomeViews(RedirectView):
    # url = '/'
    pattern_name = 'index'


class HomeUserView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        if self.request.GET.__contains__('tipe'):
            kwargs['tipe'] = self.request.GET['tipe']

        # context = kwargs
        # return context
        return super().get_context_data(**kwargs)


# inheritance hanya dari base view
class HomeRedirectView(RedirectView):
    pattern_name = 'user'
    permanent = False

    query_string = True

    def get_redirect_url(self, *args, **kwargs):

        if kwargs['user'] == 'alvins':
            kwargs['user'] = 'zukron'
        return super().get_redirect_url(*args, **kwargs)