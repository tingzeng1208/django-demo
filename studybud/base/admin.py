from django.contrib import admin

# Register your models here.
# from . import models
# from .models import Room
from .models import Room, Topic, Message


admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
