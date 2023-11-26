from django.contrib import admin
from django.urls import path
import authentication.views, presents.views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.identification_page, name='identification'),
    path('home/<int:member_id>', presents.views.home, name='home'),
    path('shoppinglist/<int:member_id>', presents.views.shopping_list, name='shopping-list'),
    path('presentdetail/<int:present_id>', presents.views.present_detail, name='present-detail'),
    path('deletepresent/<int:present_id>/<int:member_id>', presents.views.delete_present, name='delete-present'),
    path('purchasepresent/<int:present_id>/<int:member_id>', presents.views.purchase_present, name='purchase-present'),
    path('deletepurchase/<int:present_id>/<int:member_id>', presents.views.delete_purchase, name='delete-purchase'),
]
