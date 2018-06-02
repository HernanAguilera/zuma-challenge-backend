from django import template

register = template.Library()


@register.filter(name='bootstrap_class')
def boostrap_class(field, args=""):
    inputs = ('TextInput', 'NumberInput', 'EmailInput', 'URLInput', 'PasswordInput', 'DateInput', 'DateTimeInput', 'TimeInput', 'Textarea', 'Select', 'SelectMultiple')
    if get_type(field) in inputs:
        return field.as_widget(attrs={"class":"form-control " + args })
    return field.as_widget(attrs={'class': args})

def get_type(field):
    return field.field.widget.__class__.__name__