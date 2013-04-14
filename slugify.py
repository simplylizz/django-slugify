from django import conf
from django.utils import encoding

try:
    # Django 1.5 have some permutations.
    from django.utils import text as src_pkg
    from django.utils.text import slugify as dj_slugify
except ImportError:
    from django.template import defaultfilters as src_pkg
    from django.template.defaultfilters import slugify as dj_slugify

import unidecode


def slugify(value):
    value = encoding.smart_unicode(value)
    return dj_slugify(encoding.smart_unicode(unidecode.unidecode(value)))


if getattr(conf.settings, 'PATCH_SLUGIFY', True):
    if not getattr(src_pkg.slugify, 'patched', False):
        src_pkg.slugify = slugify
        src_pkg.slugify.patched = True
