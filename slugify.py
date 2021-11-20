from django import conf
from django.utils import text as src_pkg
from django.utils.text import slugify as dj_slugify

import unidecode


def slugify(value, allow_unicode=False):
    if not allow_unicode:
        value = unidecode.unidecode(value)
    return dj_slugify(value=value, allow_unicode=allow_unicode)


if getattr(conf.settings, 'PATCH_SLUGIFY', True):
    if not getattr(src_pkg.slugify, 'patched', False):
        src_pkg.slugify = slugify
        src_pkg.slugify.patched = True
