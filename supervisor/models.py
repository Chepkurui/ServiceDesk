from django.db import models

# Create your models here.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Department(models.Model):
    dpt_name = models.CharField(max_length=100)
    def __str__(self):
        return self.dpt_name

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Project(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    pjt_name = models.CharField(max_length=200)
    pjt_status = models.IntegerField(default=0)
    def __str__(self):
        return self.pjt_name
    def is_pending(self):
        return self.pjt_status <= 2

class Stage(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    stg_name = models.CharField(max_length=200)
    stg_order = models.IntegerField(default=0)
    def __str__(self):
        return self.stg_name

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Phase(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    phs_name = models.CharField(max_length=200)
    phs_status = models.IntegerField(default=0)
    def __str__(self):
        return self.phs_name

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Task(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    tsk_name = models.CharField(max_length=200)
    tsk_status = models.IntegerField(default=0)
    def __str__(self):
        return self.tsk_name

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Issue(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    iss_name = models.CharField(max_length=200)
    iss_status = models.IntegerField(default=0)
    def __str__(self):
        return self.iss_name