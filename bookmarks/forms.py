from django import forms


class BookmarkForm(forms.Form):
    name = forms.CharField(label='Website Name', max_length=100)
    url = forms.URLField(label='Website url')
    notes = forms.CharField(label='Any Notes', required=False)
