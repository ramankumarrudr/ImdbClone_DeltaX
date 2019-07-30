from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib import messages
from app.models import Actor,Movie,Tvshow
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.form import UserForm,ActorForm,TvshowForm
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
#from . import form
def index(request):
        movie_eng = Movie.objects.filter(lang='ENGLISH')
        movie_tel = Movie.objects.filter(lang='TELUGU')
        movie_hin = Movie.objects.filter(lang='HINDHI')
        movie_tam = Movie.objects.filter(lang='TAMIL')
        paginator1 = Paginator(movie_eng, 30)
        paginator2 = Paginator(movie_hin, 30)
        paginator3 = Paginator(movie_tam, 30)
        paginator4 = Paginator(movie_tel, 30)
        page = request.GET.get('page')
        template = 'app/index.html'
        mov_eng =  paginator1.get_page(page)
        mov_hin =  paginator2.get_page(page)
        mov_tam =  paginator3.get_page(page)
        mov_tel =  paginator4.get_page(page)
        return render(request,template,{'mov_eng':mov_eng,'mov_hin':mov_hin,'mov_tam':mov_tam,'mov_tel':mov_tel,'eng':movie_eng,'hin':movie_hin,'tam':movie_tam,'tel':movie_tel})

def tvshows(request):
        tvshow = Tvshow.objects.order_by('release_date')
        tvshow_recent = Tvshow.objects.filter(status='RecentlyAdded')
        tvshow_tr = Tvshow.objects.filter(status='TopRated')
        tvshow_mw = Tvshow.objects.filter(status='MostWatched')
        paginator = Paginator(tvshow, 10)
        page = request.GET.get('page')
        template = 'app/tvshow.html'
        tvshows = paginator.get_page(page)
        return render(request,template,{'tvshow':tvshows,'tvshow_recent':tvshow_recent,'toprated':tvshow_tr,'mostwatched':tvshow_mw})                        


def formexit(request):
    exit_stat = {'exit-stat':"Click to Exit"}
    return render(request,'app/form_exit.html',context=exit_stat)    

def post(request):
        if request.method == 'POST':
                form = UserForm(request.POST or None, request.FILES or None)
                if form.is_valid():
                        form.save()   
                        form = UserForm() 
                        print('saved succesfully')                  
                        return redirect('index')

        else:
                form = UserForm(request.POST or None, request.FILES or None)         
        return render(request,'app/form.html',{'form':form})

def post_tvshow(request):
        if request.method == 'POST':
                show_form = TvshowForm(request.POST or None, request.FILES or None)
                if show_form.is_valid():
                        show_form.save()   
                        show_form = TvshowForm() 
                        print('saved succesfully')                  
                        return redirect('tvshow')

        else:
                show_form = TvshowForm(request.POST or None, request.FILES or None)         
        return render(request,'app/tvshow_form.html',{'show_form':show_form})

def actor(request):
        if request.method == 'POST':
                actor_form = ActorForm(request.POST or None, request.FILES or None)
                if actor_form.is_valid():
                        actor_form.save()   
                        actor_form = ActorForm()
                        return redirect('exit') 

        else:
                actor_form = ActorForm(request.POST or None, request.FILES or None)         
        return render(request,'app/actor_form.html',{'actor_form':actor_form})         

def movie_update(request,id=None):
        instance = get_object_or_404(Movie,id=id)
        if request.method == "POST":
                form = UserForm(request.POST or None, request.FILES or None,instance=instance)
                if form.is_valid():
                        form.save()
                        return redirect('index')           

        else:
                form = UserForm(request.POST or None, request.FILES or None,instance=instance)     
        context = {
                        "movie":instance.movie,
                        "instance":instance,
                        "form" : form,
                }            
        return render(request,'app/form.html',context)   



def movie_delete(request,id=None):
        if not request.user.is_staff or not request.user.is_superuser :
                raise Http404
        instance = get_object_or_404(Movie,id=id)
        instance.delete()
        messages.success(request,"Sucessfully Deleted")
        return redirect('index')        

def tvshow_update(request,id=None):
        instance_tvshow = get_object_or_404(Tvshow,id=id)
        if request.method == "POST":
                form = TvshowForm(request.POST or None, request.FILES or None,instance=instance_tvshow)
                if form.is_valid():
                        form.save()
                        return redirect('tvshow')           

        else:
                form = TvshowForm(request.POST or None, request.FILES or None,instance=instance_tvshow)     
        context = {
                        "tvshow":instance_tvshow.tvshow,
                        "instance":instance_tvshow,
                        "show_form" : form,
                }            
        return render(request,'app/tvshow_form.html',context)   

def tvshow_delete(request,id=None):
        if not request.user.is_staff or not request.user.is_superuser :
                raise Http404
        instance_tvshow = get_object_or_404(Tvshow,id=id)
        instance_tvshow.delete()
        messages.success(request,"Sucessfully Deleted")
        return redirect('tvshow')   

def actor_images(request):
        actor = Actor.objects.all()
        paginator = Paginator(actor, 14)
        page = request.GET.get('page')
        template = 'app/actors.html'
        actors = paginator.get_page(page)
        return render(request,template,{'actors':actors})






