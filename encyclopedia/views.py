from django.http import request
from django.shortcuts import redirect, render

from . import util
from markdown2 import Markdown

MarkdownConverter = Markdown()

def index(request):
    if request.method == "POST":
        query = request.POST["q"]
        possible_entries = util.get_similar_entries(query)

        if type(possible_entries) == list:
            return render(request,"encyclopedia/search.html",{"entries": possible_entries})
    
        return redirect("entry_page",entry=possible_entries)

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

def search_entry(request,query):
    """
    searches for entry and if does not exist - substrings of search
    """
    possible_entries = util.get_similar_entries(query)

    if type(possible_entries) == list:
        return render(request,"encyclopedia/search.html",{"entries": possible_entries})
    
    return redirect("entry_page",entry=possible_entries)