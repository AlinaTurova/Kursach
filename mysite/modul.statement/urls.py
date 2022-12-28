from django.urls import path
from .views import StatementCreate, StatementDetail, StatementRetrieve, StatementUpdate, StatementDelete

app_name = 'statement'


urlpatterns = [
    path('', StatementCreate.as_view(), name='statementCreate'),
    path('retrieves/', KursRetrieve.as_view(), name='statementRetrieve'),
    path('<int:pk>', KursDetail.as_view(), name='statementDetail'),
    path('<int:pk>/update/', KursUpdate.as_view(), name='statementUpdate'),
    path('<int:pk>/delete/', KursDelete.as_view(), name='statementDelete'),
]
