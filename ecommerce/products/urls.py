from django.urls import path
from .views import DetailCategory,ListCustomer,ListProduct,DetailProduct,ListCategory
urlpatterns = [
    # path('',views.apiOverview),
    # path('/',views.apiOverviewproduct)
#     path('categories', ListCategory.as_view(), name='categories'),
#     path('categories/<str:pk>/', DetailCategory.as_view(), name='singlecategory'),
#     path('products/', ListProduct.as_view(), name='products'),
#     path('products/<str:pk>/', DetailProduct.as_view(), name='singleproduct'),
#     path('customer/', ListCustomer.as_view(), name='customer'),
]