from django.db import models
from mptt.models import MPTTModel,TreeForeignKey

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class CourseCategory(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255, null= True)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, null = True)
    coursecode = models.CharField(max_length=30,blank=False,default=None,null= True) #课程编码
    credits = models.CharField(max_length=5, blank=False, default=None,null= True)  # 学分
    semester = models.CharField(max_length=20, blank=True, null=True)  # 开课学期

    def __str__(self):
        return self.name


class TrainingPlan(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TrainingClass(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    must = models.BooleanField(null=True)
    training_plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(CourseCategory,on_delete=models.CASCADE,null=True)
    semester = models.CharField(max_length=20, blank=True, null=True)  # 开课学期

    def __str__(self):
        return f'{self.training_plan} - {self.course}'


class TrainingCategory(models.Model):
    category_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    parent = models.IntegerField(null=True, blank=True)
    training_plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, null=True)
    credits = models.IntegerField(default=0)
    detail = models.TextField(null = True)

    def __str__(self):
        return self.name

    def get_children(self):
        """
        返回所有直接子分类。
        """
        return TrainingCategory.objects.filter(parent=self.category_id)

class CourseCategory_display(MPTTModel):
    category_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    training_plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, null=True)
    credits = models.IntegerField(default=0)
    detail = models.TextField(null=True)
    def __str__(self):
        return self.name
