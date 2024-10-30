from django.utils import timezone
import jdatetime


class PersianDateMixin:
    @property
    def persian_created(self):
        created = self.created or timezone.now()
        return jdatetime.datetime.fromgregorian(datetime=created).strftime('%Y/%m/%d %H:%M:%S')

    persian_created.fget.short_description = 'تاریخ ایجاد (هجری شمسی)'

    @property
    def persian_updated(self):
        updated = self.updated or timezone.now()
        return jdatetime.datetime.fromgregorian(datetime=updated).strftime('%Y/%m/%d %H:%M:%S')

    persian_updated.fget.short_description = 'تاریخ به‌روزرسانی (هجری شمسی)'
