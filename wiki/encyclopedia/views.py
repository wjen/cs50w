from django.shortcuts import render
from django import forms
from . import util
from markdown2 import Markdown
import random

markdowner = Markdown()


class Search(forms.Form):
    search_term = forms.CharField(label="Search Wiki", widget=forms.TextInput(
        attrs={'class': 'search__input', 'placeholder': 'Search'}))


class Post(forms.Form):
    title = forms.CharField(label="Title")
    textarea = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Write markdown'}))


class Edit(forms.Form):
    textarea = forms.CharField(widget=forms.Textarea(), label='')


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), 'form': Search()
    })


def show(request, title):
    entries = util.list_entries()
    entries_lower = [x.lower() for x in entries]
    if title.lower() in entries_lower:
        print(title)
        page = util.get_entry(title)
        page_converted = markdowner.convert(page)
        return render(request, 'encyclopedia/entry.html', {
            "page": page_converted, "title": title, 'form': Search()
        })
    else:
        return render(request, 'encyclopedia/error.html', {
            "title": 'error'
        })


def search(request):
    search_matches = []
    entries = util.list_entries()
    entries_lower = [x.lower() for x in entries]
    # needs is_valid() to get cleaned_data
    form = Search(request.GET)
    if form.is_valid():
        search_term = form.cleaned_data["search_term"]
        search_term_lower = search_term.lower()
        if search_term_lower in entries_lower:
            page = util.get_entry(search_term)
            page_converted = markdowner.convert(page)
            return render(request, 'encyclopedia/entry.html', {
                'page': page_converted, "title": search_term, 'form': Search()
            })
        for entry in entries_lower:
            if search_term_lower in entry:
                search_matches.append(entry)
        return render(request, 'encyclopedia/search.html', {
            'entries': search_matches, 'form': Search()
        })
    # server validation return form with error
    else:
        return render(request, 'encyclopedia/search.html', {
            'entries': search_matches, 'form': form
        })


def create(request):
    if request.method == "POST":
        form = Post(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text_area = form.cleaned_data['textarea']
            util.save_entry(title, text_area)
            page = util.get_entry(title)
            page_converted = markdowner.convert(page)
            return render(request, 'encyclopedia/entry.html', {
                'form': Search(), 'page': page_converted, 'title': title
            })
        else:
            return render(request, 'encyclopedia/create.html', {
                'form': Search(), 'post': Post()
            })

    return render(request, 'encyclopedia/create.html', {
        'form': Search(), 'post': Post()
    })


def edit(request, title):
    if request.method == 'GET':
        page = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {"form": Search(), "edit": Edit(initial={'textarea': page}), 'title': title})
    else:
        form = Edit(request.POST)
        if form.is_valid():
            body = form.cleaned_data['textarea']
            util.save_entry(title, body)
            page = util.get_entry(title)
            page_converted = markdowner.convert(page)
            return render(request, "encyclopedia/entry.html", {"form": Search(), 'title': title, "page": page})


def randomPage(request):
    if request.method == 'GET':
        entries = util.list_entries()
        num = random.randint(0, len(entries) - 1)
        page_random = entries[num]
        page = util.get_entry(page_random)
        page_converted = markdowner.convert(page)

        context = {
            'form': Search(),
            'page': page_converted,
            'title': page_random
        }

        return render(request, "encyclopedia/entry.html", context)
