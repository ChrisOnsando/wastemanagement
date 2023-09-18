from django.contrib import admin
from accounts.models import User, Driver, Customer

admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Customer)
