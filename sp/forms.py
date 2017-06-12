from django.forms import ModelForm
from django.forms.widgets import ClearableFileInput
from sp.models import Call, Profile


class MyClearableFileInput(ClearableFileInput):
     initial_text = 'Текущее'
     input_text = 'Изменить'
     clear_checkbox_label = 'Удалить'


class CallUpdateForm(ModelForm):
    class Meta:
        model = Call
        fields = ('type', 'city', 'name', 'description', 'card', 'tags')
        widgets = {
            'card': MyClearableFileInput(),
        }


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'city', 'birthday', 'education', 'gender', 'offers', 'search', 'e_mail', 'contacts']
