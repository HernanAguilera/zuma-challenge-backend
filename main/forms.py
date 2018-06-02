from django import forms
from .models import Number

__all__ = ('NumberForm', )

class NumberForm(forms.ModelForm):
    
    def clean(self):
        form_data = self.cleaned_data
        print('form_data', form_data)
        numbers = (form_data['number_1'], form_data['number_2'], form_data['number_3'], form_data['number_4'])
        numbers_set = set(numbers)
        if len(numbers) != len(numbers_set):
            raise forms.ValidationError('Todos los numeros deben ser diferentes', 'same_number')
        return form_data

    class Meta:
        model = Number
        fields = '__all__'
