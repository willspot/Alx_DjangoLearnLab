from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

    def clean_query(self):
        # This method can be used for additional sanitization or validation of the query field
        query = self.cleaned_data.get('query')
        return query.strip() if query else query
