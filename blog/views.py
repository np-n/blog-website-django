from django.shortcuts import render
# from django.http import HttpResponse

posts = [
            {
                'author':'Netra Prasad Neupane',
                'title':'Blog Post 1',
                'content':'First blog post content',
                'date_posted':'october 7 2020'
            },
            {
                'author':'Nimesh Neupane',
                'title':'Blog Post 2',
                'content':'Second blog post content',
                'date_posted':'october 8 2020'
            },

        ]

def home(request):

    # passing dicionary
    context = {
        # Passing as posts variable
        'posts' : posts
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    # For second argument it looks subsirectory of templates inside app
    return render(request,'blog/home.html',context)

def about(request):
    # Here we are directly passing  title without creating dictionary

    # return HttpResponse('<h1>Blog about</h1>')
    return render(request,'blog/about.html',{'title':'About'})


# blog -> templates -> blog -> template.htmlcon
