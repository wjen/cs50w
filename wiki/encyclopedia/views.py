from django.shortcuts import render

from . import util
from markdown2 import Markdown

markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    page = util.get_entry(title)
    page_converted = markdowner.convert(page)
    return render(request, 'encyclopedia/entry.html', {
        "page" : page_converted, "title": title
    })
