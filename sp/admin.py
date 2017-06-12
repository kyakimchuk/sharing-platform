from django.contrib import admin
from sp.models import Call, Profile
# from django import forms
# from sp.forms import MyClearableFileInput


# class CallAdminForm(forms.ModelForm):
#     class Meta:
#         model = Call
#         fields = ('user_id', 'type', 'city', 'name', 'description', 'card', 'tags')
#         widgets = {
#             'card': MyClearableFileInput(),
#         }


class CallAdmin(admin.ModelAdmin):
    # form = CallAdminForm
    list_display = ('id', 'user_id', 'type', 'city', 'name', 'description', 'card', 'date_time')

admin.site.register(Call, CallAdmin)
admin.site.register(Profile)