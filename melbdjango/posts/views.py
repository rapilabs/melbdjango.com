from django.views.generic import ListView
from .models import Post

class PostsView(ListView):
    model = Post

    def get_queryset(self):
        return self.model.objects.published()
