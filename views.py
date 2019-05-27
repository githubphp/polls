from django.shortcuts import render
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'polls/home.html', context)


def about(request):
    return render(request, 'polls/about.html', {'title': 'About'})







#from django.http import HttpResponse

#def index(request):
 #   return HttpResponse ("You are in polls Index.")

#def detail(request, question_id):
 #   return HttpResponse("You're looking at question %s." % question_id)

#def results(request, question_id):
 #   response = "You're looking at the results of question %s."
  #  return HttpResponse(response % question_id)

#def vote(request, question_id):
 #   return HttpResponse("You're voting on question %s." % question_id)