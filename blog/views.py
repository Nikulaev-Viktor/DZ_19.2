from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview')

    # success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_published:
        blog_item.is_published = False
    else:
        blog_item.is_published = True

    blog_item.save()
    return redirect(reverse('blog:list'))


def CreateBlogList(request):
    blog_list = Blog.objects.all()
    context = {
        'object_list': blog_list,

    }

    return render(request, 'blog/toggle.html', context)
