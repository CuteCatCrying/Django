from django.core.exceptions import ValidationError

def validate_author(value):
    author_input = value
    if author_input == 'Einstein':
        message = 'Maaf, ' + author_input + ' tidak bisa posting'
        raise ValidationError(message)