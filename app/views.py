from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # or wherever you want to go after login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'app/login.html')
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        login(request, user)  # log in after register
        return redirect('home')  # change this to your homepage url name

    return render(request, 'app/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'app/home.html', {'questions': questions})

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'app/ask.html', {'form': form})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = AnswerForm()
    return render(request, 'app/question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return HttpResponseRedirect(reverse('question_detail', args=[answer.question.id]))
