from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cars'
urlpatterns = [
    path('cars/', views.CarListView.as_view(), name='cars'),
    path('person/', views.PersonListView.as_view(), name='person'),
    path('cars/<int:pk>', views.CarDetailView.as_view(), name='cars-detail'),
    path('cars/<slug>', views.PersonDetailView.as_view(), name='person-detail'),

]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)