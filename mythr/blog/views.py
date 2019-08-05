from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, NewPostForm
from django.views.generic.edit import FormView
# Create your views here.


def home(request):
    title = 'Home Page'
    posts = list(Post.objects.all())
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, 'home.html', context=context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'postdetail.html', context={'post': post})


class NewPostView(FormView):
    template_name = 'newpost.html'
    form_class = NewPostForm
    success_url = '/'
    def form_valid(self, form):
        form.create_post()
        return super().form_valid(form)

def new_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(content=form.cleaned_data['content'], author=form.cleaned_data['author'], post=post)
            comment.save()
            return redirect('blog-post-detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'newcomment.html', context={'form': form})

