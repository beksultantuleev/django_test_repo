from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name',
                  'description', 'price',
                  'image' )

        widgets = {}
        for fields_name in fields:
            if fields_name == 'image':
                widgets[fields_name] = forms.FileInput(attrs={'class': INPUT_CLASSES})
            elif fields_name == 'category':
                widgets[fields_name] = forms.Select(attrs={'class': INPUT_CLASSES})
            elif fields_name == 'description':
                widgets[fields_name] = forms.Textarea(attrs={'class': INPUT_CLASSES})
            else:
                widgets[fields_name] = forms.TextInput(attrs={'class': INPUT_CLASSES})

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('is_sold', 'name',
                  'description', 'price',
                  'image' )

        widgets = {}
        for fields_name in fields:
            if fields_name == 'image':
                widgets[fields_name] = forms.FileInput(attrs={'class': INPUT_CLASSES})
            elif fields_name == 'is_sold':
                pass
                # widgets[fields_name] = forms.Select(attrs={'class': INPUT_CLASSES})
            elif fields_name == 'description':
                widgets[fields_name] = forms.Textarea(attrs={'class': INPUT_CLASSES})
            else:
                widgets[fields_name] = forms.TextInput(attrs={'class': INPUT_CLASSES})