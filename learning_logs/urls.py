from django.conf.urls import url
from . import views 
urlpatterns = [
    #схемы url для learning_logs
               url(r'^$',views.index, name = 'index'),
               #страница со всеми темами
               url(r'^topics/$',views.topics, name = 'topics'),
               #текст отдельной темы
               url(r'^topics/(?P<topic_id>\d+)/$',views.topic, name = 'topic'),
               #страница для добав новой темы
               url(r'^new_topic/$',views.new_topic, name = 'new_topic'),
               #страница для добав новой записи
               url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry, name = 'new_entry'),
               #страница для редактирования записей
               url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry, name = 'edit_entry'),

               ]