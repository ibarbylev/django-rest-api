from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from polls.models import Poll, Choice


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    choices = Choice.objects.filter(poll__question=poll.question)
    list_choices = [c.choice_text for c in choices]
    data = {"results": {
        "question": poll.question,
        "choices": list_choices,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)


def choices_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()
    choices = Choice.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question", "choices__choice_text", "pub_date"))}
    return JsonResponse(data)


def choices_detail(request, pk):
    choice = get_object_or_404(Choice, pk=pk)
    data = {"results": {
        "question": choice.poll.question,
        "choice_text": choice.choice_text
    }}
    return JsonResponse(data)
