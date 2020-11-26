from .models import EnglishWord
from django.shortcuts import render, get_object_or_404, redirect




def home(request):
    EnglishWords = EnglishWord.objects.order_by('?')
    context = {'EnglishWords': EnglishWords}
    return render(request, 'polls/home.html', context)

def detail(request, EnglishWord_id):
    EnglishWord_detail = get_object_or_404(EnglishWord, pk = EnglishWord_id)
    return render(request, 'polls/detail.html', {'EnglishWord': EnglishWord_detail})

def create(request):
    return render(request, 'polls/create.html')

def add(request):
    EnglishWords = EnglishWord()
    EnglishWords.mean = request.GET['mean']
    EnglishWords.word = request.GET['word']
    EnglishWords.save()
    return render(request, 'polls/create.html')

def delete(request, EnglishWord_id):
    EnglishWords = EnglishWord.objects.get(id=EnglishWord_id)
    EnglishWords.delete()
    return redirect('/')
