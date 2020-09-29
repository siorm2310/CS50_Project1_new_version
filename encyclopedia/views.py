from django.http import request
from django.shortcuts import redirect, render

from . import util
from markdown2 import Markdown
import random
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

def add_entry(request):
    if request.method == "POST":
        titles = util.list_entries()
        title = request.POST["title"]
        if title in titles:
            return render(request,"encyclopedia/error.html",{"error": 403})
        if title is None:
            return redirect("index")
        content = request.POST["content"]
        util.save_entry(title, content)
        return redirect("entry_page", entry=title)
    return render(request,"encyclopedia/new_entry.html")

def random_entry(request):
    entry = random.choice(util.list_entries())
    return redirect("entry_page", entry=entry)

def edit_entry(request,entry):
    entry_content = util.get_entry(entry)

    if request.method == "POST":
        util.save_entry(request.POST["title"],request.POST["content"])
        return redirect("entry_page", entry=entry)
    
    return render(request, "encyclopedia/edit_entry.html",{
            "entry": entry,
            "content":entry_content
        })