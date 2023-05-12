from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']


# from django.contrib import admin
# from rest_framework.authtoken.admin import TokenAdmin

# # Set the `raw_id_fields` attribute of the `TokenAdmin` class to `['user']`.
# TokenAdmin.raw_id_fields = ['user']

# # Register the `Token` model with the Django admin site.
# admin.site.register(Token, TokenAdmin)
