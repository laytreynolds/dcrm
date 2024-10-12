from django.contrib import admin
from .models import Order, Company, Comment, Campaign
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "status",
        "order_Number",
        "company",
        "order_First_Name",
        "order_Last_Name",
        "order_Mobile",
        "order_Created",
    ]


@admin.register(Company)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["company_Type", "company_Name", "company_Employees"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["owner", "order", "created", "body"]
    list_filter = ["owner", "created", "order"]
    search_fields = ["owner", "order", "body"]


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ["name", "target"]
    list_filter = ["name", "target"]
    search_fields = ["name", "target"]


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = "action_time"

    list_filter = ["user", "content_type", "action_flag"]

    search_fields = ["object_repr", "change_message"]

    list_display = [
        "action_time",
        "user",
        "content_type",
        "object_link",
        "action_flag",
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse(
                    "admin:%s_%s_change" % (ct.app_label, ct.model),
                    args=[obj.object_id],
                ),
                escape(obj.object_repr),
            )
        return mark_safe(link)

    object_link.admin_order_field = "object_repr"
    object_link.short_description = "object"
