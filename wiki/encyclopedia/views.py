from django.shortcuts import render
from django import forms
from . import util
from markdown2 import Markdown

markdowner = Markdown()

class Search(forms.Form):
    search_term = forms.CharField(label="Search Wiki", widget=forms.TextInput(attrs={'class' : 'myfieldclass', 'placeholder': 'Search'})) 

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), 'form': Search()
    })

def entry(request, title):
    entries = util.list_entries()
    entries_lower = [x.lower() for x in entries]
    if title.lower() in entries_lower:    
        print(title)
        page = util.get_entry(title)
        page_converted = markdowner.convert(page)
        return render(request, 'encyclopedia/entry.html', {
            "page" : page_converted, "title": title, 'form': Search()
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
                'page' : page_converted, "title" : search_term, 'form' : Search()
            })
        for entry in entries_lower: 
            if search_term_lower in entry:
                search_matches.append(entry)
        return render(request, 'encyclopedia/search.html', {
            'entries' : search_matches, 'form': Search()
        })
