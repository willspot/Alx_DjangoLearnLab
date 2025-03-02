from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.strip()  # Clean leading/trailing spaces

    def clean_email(self):
        email = self.cleaned_data['email']
        # Custom email validation (example)
        return email.lower()  # Normalize email to lowercase

    def clean_message(self):
        message = self.cleaned_data['message']
        return message.strip()  # Clean leading/trailing spaces


class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

    def clean_query(self):
        # This method can be used for additional sanitization or validation of the query field
        query = self.cleaned_data.get('query')
        return query.strip() if query else query
