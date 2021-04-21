from django.shortcuts import render
from rest_framework import viewsets
from .models import Endpoint, Skill, Project, Resume, TextSection
from .serializers import EndpointsSerializer, SkillSerializer, ProjectSerializer, ResumeSerializer, TextSectionSerializer

# Create your views here.


class IndexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Endpoint.objects.all()
    serializer_class = EndpointsSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ResumeViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class TextSectionViewset(viewsets.ReadOnlyModelViewSet):
    queryset = TextSection.objects.all()
    serializer_class = TextSectionSerializer
