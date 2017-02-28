from __future__ import absolute_import, unicode_literals

from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.wagtailcore.models import Orderable, Page, Site
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel


class HomePage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('related_content', panels=[
            FieldPanel('title'),
            FieldPanel('sites', widget=forms.CheckboxSelectMultiple)
        ], label="Related content")
    ]


class HomePageInline(Orderable, models.Model):
    page = ParentalKey(HomePage, related_name='related_content')
    title = models.CharField(max_length=255)
    sites = models.ManyToManyField(Site)
    # sites = ParentalManyToManyField(Site)
