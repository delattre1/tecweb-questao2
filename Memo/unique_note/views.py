from .models import Note
from django.shortcuts import render, redirect
from datetime import datetime


def createNote(note):
    note_item = Note(note=note, pub_date=datetime.now())

    note_item.save()


def index(request):
    if request.method == 'POST':
        note = request.POST.get('note')
        createNote(note)

        return redirect('index')
    else:
        all_notes = Note.objects.order_by('pub_date')
        tamanho = len(all_notes)
        last_note = (all_notes[tamanho-1])

        return render(request, 'unique_note/index.html',
                      {'last_note': last_note})
