from django.http import request
from django.shortcuts import render

from . import util
from markdown2 import Markdown

MarkdownConverter = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request,entry):
    try:
        content = MarkdownConverter.convert(util.get_entry(entry)) 
        return render(request, "encyclopedia/entry.html",{
            "Entry_name": entry,
            "content":content
        })
    except TypeError:
        return render(request,"encyclopedia/error.html",{"error": 404})