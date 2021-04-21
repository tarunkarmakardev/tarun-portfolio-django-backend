from rest_framework import serializers
from .models import Endpoint, Skill, Project, Resume, TextSection


class EndpointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class TextSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextSection
        fields = '__all__'
