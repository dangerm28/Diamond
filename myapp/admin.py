from django.contrib import admin
from .models import MyModel
import jdatetime


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'persian_created', 'persian_updated')

    def persian_created(self, obj):
        if obj.created:
            return jdatetime.datetime.fromgregorian(datetime=obj.created).strftime('%Y/%m/%d %H:%M:%S')
        return '-'
    persian_created.short_description = 'تاریخ ایجاد (هجری شمسی)'

    def persian_updated(self, obj):
        if obj.updated:
            return jdatetime.datetime.fromgregorian(datetime=obj.updated).strftime('%Y/%m/%d %H:%M:%S')
        return '-'
    persian_updated.short_description = 'تاریخ به‌روزرسانی (هجری شمسی)'
