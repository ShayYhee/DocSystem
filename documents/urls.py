from django.urls import path
from .views import create_document, document_list, home, send_approved_email, autocomplete_sales_rep

urlpatterns = [
    path("create/", create_document, name="create_document"),
    path("list/", document_list, name="document_list"),
    path("", home, name="home"),
    path('autocomplete/sales-rep/', autocomplete_sales_rep, name='autocomplete_sales_rep'),
    # path("send-email/<int:document_id>/", send_approved_email, name="send_approval_email"),
]
