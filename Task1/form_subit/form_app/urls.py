from django.urls import path
# from .views import form_submit,render_form
from. import views

urlpatterns = [
    path('',views.render_form, name='render_form'),
    path('submit-form/', views.form_submit, name='form_submit'),
    path('submit-form/', views.form_submit, name='form_submit'),
]
