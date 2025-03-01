from django.contrib import admin
from inuamkulimaApp.models import ContactMessage, TrainingSession,ConsultationRequest,Product,Seller,LoanRequest


admin.site.register(TrainingSession)
admin.site.register(LoanRequest)
admin.site.register(ContactMessage)
admin.site.register(Seller)
admin.site.register(Product)



class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "consultation_type", "status", "consultation_date")
    list_filter = ("status", "consultation_type")
    actions = ["approve_requests", "deny_requests"]

    def approve_requests(self, request, queryset):
        queryset.update(status="approved")
    approve_requests.short_description = "Approve selected requests"

    def deny_requests(self, request, queryset):
        queryset.update(status="denied")
    deny_requests.short_description = "Deny selected requests"

admin.site.register(ConsultationRequest, ConsultationRequestAdmin)
