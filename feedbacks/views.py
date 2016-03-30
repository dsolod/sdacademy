from django.shortcuts import render
from feedbacks.models import Feedback
from django import forms
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ()


class FeedbackView(CreateView):
    model = Feedback
    success_url = reverse_lazy('feedback:index')
    form = FeedbackForm
    template_name = '../templates/feedback.html'
    fields = '__all__'
    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form, **kwargs):

        #print settings.ADMINS
        ADMINS = []
        for i in range(len(settings.ADMINS)):
            print settings.ADMINS[i][1]
            ADMINS.append(settings.ADMINS[i][1])
        #print ADMINS

        send_mail(self.request.POST['subject'], self.request.POST['message'], 
            self.request.POST['from_email'], [str(ADMINS)], fail_silently=False)

        messages.success(self.request, 'Thank you for your feedback!'
            ' We will keep in touch with you very soon!')       
        return super(FeedbackView, self).form_valid(form)
