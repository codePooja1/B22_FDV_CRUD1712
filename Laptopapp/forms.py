from .models import Laptop
from django import forms


class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        labels = {'ram':'RAM in GB','company':'company name'}
        widgets = {'model_name': forms.TextInput(attrs={'placeholder':'eg:abc123'})}

        def clean_weight(self):
            all_cleaned_data = super().clean()

            r= all_cleaned_data['rom']
            if r<1:
                raise forms.ValidationError('Rom cant be less than 1')
            elif r % 2 == 1:
                raise forms.ValidationError('ROM always available in odd number')

            p = all_cleaned_data['ram']
            if p not in [2,4,6,8,16,24,64,256]:
                raise forms.ValidationError('msg')

            w = all_cleaned_data['weight']
            if w < 0:
                raise forms.ValidationError('weight cannot be negative')
            else:
                return w

