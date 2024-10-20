from django.core.paginator import Paginator
from django.http import  HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

@login_required

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Perform actions (e.g., send email)
            return redirect('polls:thanks')
    else:
        form = ContactForm()
    return render(request, 'polls/contact.html', {'form': form})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    paginator=Paginator(latest_question_list,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'polls/index.html',{'page_obj':page_obj})

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question}) 

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))