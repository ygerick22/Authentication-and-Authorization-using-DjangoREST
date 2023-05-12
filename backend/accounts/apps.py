from django.apps import AppConfig

# Define the configuration for the accounts app.
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Use a BigAutoField as the default primary key field type for this app.
    name = 'accounts'  # Set the name of the app to 'accounts'.
