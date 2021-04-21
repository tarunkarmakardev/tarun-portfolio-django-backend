from django.db import models

# Skills


class Skill(models.Model):
    icon_html = models.CharField(
        'Icon HTML', max_length=100, blank=True, null=True)
    skill_name = models.CharField(
        'Skill Name', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.skill_name


# Projects

class Project(models.Model):
    title = models.CharField('Project Title', max_length=100)
    proj_url = models.URLField('Project URL', blank=True, null=True)
    github_url = models.URLField('Github URL', blank=True, null=True)
    image = models.ImageField('Project Image', upload_to='projects/')
    description = models.TextField('Description')

    def __str__(self):
        return self.title

# Resume


class Resume(models.Model):

    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    date = models.DateTimeField('Date Added', auto_now_add=True)

    def __str__(self):
        return str(self.date)

# Endpoints


class Endpoint(models.Model):
    title = models.CharField('Title', max_length=100)
    url = models.URLField('Path')

    def __str__(self):
        return self.title

# TextSections


class TextSection(models.Model):
    title = models.CharField('Title of page or section', max_length=100)
    detail = models.TextField('Text details')
