from django.db import models
from django.contrib.auth.models import User
from menus.models import Menu


class Profile(models.Model):
    """ User profile. Contains user configurations. """
    user = models.OneToOneField(User, editable=False)
    activeMenu = models.ForeignKey(Menu, related_name="activeWeek", null=True, blank=True)
    activeWeek = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.user.username + " profile"


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
