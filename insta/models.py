# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Image(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created')
	caption = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, blank=True)
	image = models.ImageField(upload_to='images/%Y/%m/%d')
	created = models.DateField(auto_now_add=True, db_index=True)
	users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

	class Meta:
		ordering = ('-created',)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.caption)
			super(Image, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('images:detail', args=[self.id, self.slug])