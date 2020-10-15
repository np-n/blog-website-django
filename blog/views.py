from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# To check if user is not login in class based view
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin



# # Creating dummy data
# posts = [
#             {
#                 'author':'Netra Prasad Neupane',
#                 'title':'Blog Post 1',
#                 'content':'First blog post content',
#                 'date_posted':'october 7 2020'
#             },
#             {
#                 'author':'Nimesh Neupane',
#                 'title':'Blog Post 2',
#                 'content':'Second blog post content',
#                 'date_posted':'october 8 2020'
#             },

#         ]


# This is function bashed views
def home(request):

    # passing dicionary
    context = {

        # Getting and passing actual post model from database
        'posts' : Post.objects.all()

        # # Passing  above dummy data as a dictionary
        # 'posts' : posts
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    # For second argument it looks subsirectory of templates inside app
    return render(request,'blog/home.html',context)


# Class bashed views for post homepage
class PostListView(ListView):
    # model variable defines model to query in order to get ListView
    # for post listview
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['date_posted'] # Old to new
    ordering = ['-date_posted'] # new to old


# Detail views of individual posts
class PostDetailView(DetailView):
    model = Post


# To create post
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# To update post
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

# To delete post
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    # Here we are directly passing  title without creating dictionary

    # return HttpResponse('<h1>Blog about</h1>')
    return render(request,'blog/about.html',{'title':'About'})


# blog -> templates -> blog -> template.htmlcon
