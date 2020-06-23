from django.contrib import admin
from django.contrib.admin.models import DELETION
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import escape

# Disable Action 'Delete Selected'
admin.site.disable_action('delete_selected')


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in LogEntry._meta.fields]
    list_filter = ['content_type', 'action_flag']
    search_fields = ['object_repr', 'change_message']
    list_display = ['action_time', 'user',
                    'content_type', 'object_link',
                    'action_flag', 'change_message']
    ordering = ['-action_time']
    list_display_links = None

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' %
                        (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = 'object'

    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request) \
            .prefetch_related('content_type')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
