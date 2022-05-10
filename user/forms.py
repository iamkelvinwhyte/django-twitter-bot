
from django import forms

# creating a form
class TwitterFrom(forms.Form):
    SHIFT_OPTIONS = (
        ('csv', 'CSV'),
        ('json', 'JSON'),
        ('txt', 'TEXT'),
    )
    search = forms.CharField(label='Search',max_length = 200)
    doc_type = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=SHIFT_OPTIONS)