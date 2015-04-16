from django.contrib import admin
from .models import UserData
from .actions import export_as_csv_action

class UserDataAdmin(admin.ModelAdmin):
    """Admin page for UserData"""
    list_display = [
        'id', 'list_price', 'extra_price', 'discount', 'deposit_amount',
        'px_amount', 'term', 'monthly_budget', 'road_tax', 'hp', 'hp_term',
        'hp_loan_rate', 'pcp', 'pcp_term', 'pcp_loan_rate',
        'pcp_ballon_value', 'lease', 'lease_term', 'lease_extra',
        'lease_initial_payment', 'lease_monthly_payment',
        'lease_predicted_mileage', 'lease_included_mileage',
        'lease_excess_mile_price', 'loan', 'loan_term',
        'loan_loan_rate', 'loan_loan_at_end', 'ip_addr',
        'city', 'country', 'create_time', 'show_browser',
    ]
    actions = [export_as_csv_action('CSV Export',
        fields=list_display[:-1].append('browser_type')),]

    def show_browser(self, obj):
        return obj.user_agent.browser.family
    show_browser.short_description = 'Browser'

    def has_add_permission(self, request):
        return False

    def __init__(self, *args, **kwargs):
        super(UserDataAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )

# Register your models here.
admin.site.register(UserData, UserDataAdmin)