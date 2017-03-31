from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from onlineedu import views

urlpatterns = [
    url(r'^universities/$', views.UniversityList.as_view(), name='university-list'),
    url(r'^universities/(?P<pk>[0-9]+)/$', views.UniversityDetail.as_view(), name='university-detail'),
    url(r'^departments/$', views.DepartmentList.as_view(), name='department-list'),
    url(r'^departments/(?P<pk>[0-9]+)/$', views.DepartmentDetail.as_view(), name='department-detail'),
    url(r'^courses/$', views.CourseList.as_view(), name='course-list'),
    url(r'^courses/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view(), name='course-detail'),
    url(r'^coursematerials/$', views.CourseMaterialList.as_view(), name='coursematerial-list'),
    url(r'^coursematerials/(?P<pk>[0-9]+)/$', views.CourseMaterialDetail.as_view(), name='coursematerial-detail'),
    url(r'^videourls/$', views.VideoURLList.as_view(), name='videourl-list'),
    url(r'^videourls/(?P<pk>[0-9]+)/$', views.VideoURLDetail.as_view(), name='videourl-detail'),
    url(r'^books/$', views.BookList.as_view(), name='book-list'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name='book-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
