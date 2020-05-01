from django.contrib import admin
from django.utils.safestring import mark_safe

from home.models import Setting, Contact


class SettingAdmin(admin.ModelAdmin):
    list_display = ('title','company','logo_show',)
    readonly_fields = ('create_at','update_at','icon_show','logo_show',)

    fieldsets = [
        # tuple ile alanların aynı kolonda görünmesini sağlıyoruz..
        (None, { 'fields':('title','company','keywords',('description','welcome_message'),),}),
        ('Address', { 'fields' :('address', ('phone','fax'),),}),
        ('Email', {'fields' :('email',('smtpserver','smtpemail','smtppassword','smtpport'),),}),
        ('İcon', {'fields' :(('logo','logo_show'),('icon','icon_show'),),}),
        ('Social', {'fields' : ('facebook', 'instagram', 'twitter'), }),
        ('About', {'fields' : ('aboutus', 'contact', 'references'), }),
        ('Process Dates', {
            'classes' : ('collapse',),
            'fields' : ('create_at', 'update_at'),
        }),
    ]

    # Bu sayede Settings modeline tek kayıt ekleniyor.
    def has_add_permission(self, request) :
        MAX_OBJECTS = 1
        if self.model.objects.count() >= MAX_OBJECTS :
            return False
        return super().has_add_permission(request)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message','note','status')
    list_filter = ('status',)

            


admin.site.register(Setting, SettingAdmin)
admin.site.register(Contact, ContactAdmin)

