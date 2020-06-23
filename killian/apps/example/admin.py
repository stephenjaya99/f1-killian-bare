from django.contrib import admin

from killian.libs.loading import get_model

Example = get_model('example', 'Example')


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Example._meta.fields]
    actions = None

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True
