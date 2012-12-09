from django import conf
from django.template import defaultfilters
from django.template.defaultfilters import slugify as dj_slugify
from django.utils import encoding
import unidecode


def slugify(value):
    value = encoding.smart_unicode(value)
    return dj_slugify(unidecode.unidecode(value))


if getattr(conf.settings, 'PATCH_SLUGIFY', True):
    if not getattr(defaultfilters.slugify, 'patched', False):
        defaultfilters.slugify = slugify
        defaultfilters.slugify.patched = True
