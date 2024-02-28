from django.contrib import admin
from .models import Account, EmailVerification

admin.site.register(Account)

@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'experation')
    fields = ('code', 'user', 'experation', 'created_at')
    readonly_fields = ('created_at',)
