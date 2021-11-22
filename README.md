Patch for Django's slugify function.

Adds transliteration of locale-specific symbols into ASCII. Uses unidecode package.

https://code.djangoproject.com/ticket/8391 - related issue.

# Usage

1. Install it:
```
-e git+https://github.com/simplylizz/django-slugify.git#egg=slugify
```
2. Add it to the `INSTALLED_APPS` in your `settings.py`:
```
INSTALLED_APPS = [
    ...
    'slugify',
]
```
3. Set `PATCH_SLUGIFY = True` in your `settings.py` if you want to monkey-patch
   default slugify function and make it working with unicode symbols automatically.
4. Enjoy your URLs. ^__^
