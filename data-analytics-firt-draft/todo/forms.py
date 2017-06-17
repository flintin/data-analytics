from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.db.models import DateField, DateTimeField
from django.forms import SelectDateWidget, TextInput, Textarea, DateTimeInput,NumberInput,DateInput, DateField,FileInput
from todo.models import ToDo, Book 


class TodoForm(forms.ModelForm):

    tododate = forms.DateTimeField(widget=SelectDateWidget())

    class Meta:

        model = ToDo
        fields = ["title", "content", "tododate"]

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Add ToDo'})
        self.fields['content'].widget = Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Description'})

class Addbook(forms.ModelForm):

    publish = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Book
        fields = ["bookname", "price", "rating", "Author", "Publisher","publish"]

    def __init__(self, *args, **kwargs):
        super(Addbook, self).__init__(*args, **kwargs)
        self.fields['bookname'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Add A Book Title'})
        #self.fields['price'].widget = NumberInput()

        self.fields['price'] = forms.DecimalField(max_digits=7, decimal_places=2)

        self.fields['rating'] = forms.DecimalField(max_digits=3, decimal_places=1)

        self.fields['Author'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Author'})

        self.fields['Publisher'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Publisher'})

        #self.fields['publish'].widget = forms.DateInput()

        self.fields['Picture']= forms.ImageField()