from django import forms
from authy.models import Profile
from django.contrib.auth.models import User, Group

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'adress', 'city', 'plz', 'picture']

class StaffCreateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = User
        fields = ("username", "email", "groups")

    def save(self, commit=True):
        user = super(StaffCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_unusable_password()
        if commit:
            user.save()
            user.groups.set(self.cleaned_data["groups"])
        return user