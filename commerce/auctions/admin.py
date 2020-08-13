from django.contrib import admin
from .models import User, Listing, Bid, Comment
# from .models import Listing
# python manage.py createsuperuser to create superuser

# Register your models here
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Comment)
