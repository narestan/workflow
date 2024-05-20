from django import forms
from .models import CategoryItem, Item

class CategoryItemForm(forms.ModelForm):
    class Meta:
        model = CategoryItem
        fields = ['name', 'description']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item', 'description', 'is_available', 'unit', 'code', 'category']
        widgets = {
            'category': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].required = True