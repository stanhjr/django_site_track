from django import forms


class ContactForm(forms.Form):

    full_name = forms.CharField(label="Password confirmation",
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Enter your name'
                                    }
                                ))

    email = forms.CharField(label="email",
                            widget=forms.EmailInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter your email'
                                }
                            ))

    subject = forms.CharField(label="Password confirmation",
                              widget=forms.TextInput(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Enter your subject'
                                  }
                              ))

    text = forms.CharField(label="Password confirmation",
                           widget=forms.Textarea(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Write your message'
                               }
                           ))
