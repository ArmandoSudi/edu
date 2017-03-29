from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from onlineedu import views

urlpatterns = [
    url(r'^universities/$', views.UniversityList.as_view(), name='university-list'),
    url(r'^departments/$', views.DepartmentList.as_view(), name='department-list'),
    url(r'^courses/$', views.CourseList.as_view(), name='course-list'),
    url(r'^students/$', views.StudentList.as_view(), name='student-list'),
    url(r'^books/$', views.BookList.as_view(), name='book-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
