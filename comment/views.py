from django.urls import reverse
from django.views import generic

from comment.form import CommentForm


# Create your views here.

class CommentCreateView(generic.CreateView):
    template_name = 'comment/comment_create.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('info-detail')

    def form_valid(self, form):
        form.instance.info_id = self.kwargs.get('info_id')
        return super().form_valid(form)
