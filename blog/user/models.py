# Create your models here.
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User


def upload_location_author(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Author(models.Model):
    # user = models.ForeignKey(User) IN DRINKER
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    avatar = models.ImageField(upload_to=upload_location_author,
                               null=True, blank=True,
                               height_field="height_field",
                               width_field="width_field",
                               )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    register_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})
    # def __str__(self):
    #     return self.email


def create_slug(instance, new_slug=None):
    slug = slugify(instance.first_name)
    if new_slug is not None:
        slug = new_slug
    qs = Author.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_author_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_author_receiver, sender=Author)

# def create_member(sender, instance, **kwargs):
#     member, new = Member.objects.get_or_create(user=instance)
# post_save.connect(create_member, User) in Drinker