from django.urls import path, include
from .views import SkillViewSet, IndexViewSet, ProjectViewSet, ResumeViewset, TextSectionViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('skill', SkillViewSet, basename='skill')
router.register('project', ProjectViewSet, basename='project')
router.register('resume', ResumeViewset, basename='resume')
router.register('textsection', TextSectionViewset, basename='text-section')


urlpatterns = [
    path('', IndexViewSet.as_view({'get': 'list'}), name='index'),
    path('api/', include(router.urls))
]
