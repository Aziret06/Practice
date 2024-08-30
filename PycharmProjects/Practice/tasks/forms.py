from django import forms
from tasks.models import Task, Category



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=50,
        min_length=1,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search',
                'class': 'form-control',
            }))
    category = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
