from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from alpha import models
from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from itertools import zip_longest

# Create your views here.

class loginform(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="密码",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )


def base(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # 验证用户
        try:
            user = models.UserInfo.objects.get(name=username, password=password)
        except models.UserInfo.DoesNotExist:
            # 用户不存在或密码不匹配
            user = None

        if user is not None:
            # 登录成功
            request.session["info"] = {'id': user.id, 'name': user.name}
            # login(request, user)
            return redirect('/base/home')
        else:
            # 登录失败
            messages.error(request, '用户名或密码错误')

    return render(request, 'base.html')


def datamanage(request):
    return render(request, 'datamanage.html')


def classes(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        models.TrainingPlan.objects.create(name=name)
        newtrainingplan = models.TrainingPlan.objects.filter(name=name).first()

        for categories in models.CourseCategory.objects.all():
            models.TrainingCategory.objects.create(
                category_id=categories.id,
                name=categories.name,
                parent=categories.parent_id,
                training_plan=newtrainingplan,
            )

        return redirect('/test1/')

    categories = models.CourseCategory.objects.all()
    courses = models.Course.objects.all()
    return render(request, 'classes.html', {"categories": categories, "courses": courses})


def map(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        training_id = models.TrainingPlan.objects.get(name=name).id
        class_1_1 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='1',
                                                        category_id__in=[77, 78, 79, 80, 81, 83, 84]).all()
        class_1_2 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='2',
                                                        category_id__in=[77, 78, 79, 80, 81, 83, 84]).all()
        class_1_3 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='3',
                                                        category_id__in=[77, 78, 79, 80, 81, 83, 84]).all()
        class_1_4 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='4',
                                                        category_id__in=[77, 78, 79, 80, 81, 83, 84]).all()
        class_1_5 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='5',
                                                        category_id__in=[77, 78, 79, 80, 81, 83, 84]).all()
        class_1_6 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='6',
                                                        category_id__in=[77, 78, 79, 80, 81, 83, 84]).all()
        class_2_1 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='1',
                                                        category_id__in=[86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
                                                                         105, 106, 107, 108]).all()
        class_2_2 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='2',
                                                        category_id__in=[86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
                                                                         105, 106, 107, 108]).all()
        class_2_3 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='3',
                                                        category_id__in=[86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
                                                                         105, 106, 107, 108]).all()
        class_2_4 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='4',
                                                        category_id__in=[86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
                                                                         105, 106, 107, 108]).all()
        class_2_5 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='5',
                                                        category_id__in=[86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
                                                                         105, 106, 107, 108]).all()
        class_2_6 = models.TrainingClass.objects.filter(training_plan_id=training_id, must=True, semester='6',
                                                        category_id__in=[86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
                                                                         105, 106, 107, 108]).all()
        id_list11 = list(class_1_1.values_list('course_id', flat=True))
        id_list12 = list(class_1_2.values_list('course_id', flat=True))
        id_list13 = list(class_1_3.values_list('course_id', flat=True))
        id_list14 = list(class_1_4.values_list('course_id', flat=True))
        id_list15 = list(class_1_5.values_list('course_id', flat=True))
        id_list16 = list(class_1_6.values_list('course_id', flat=True))
        id_list21 = list(class_2_1.values_list('course_id', flat=True))
        id_list22 = list(class_2_2.values_list('course_id', flat=True))
        id_list23 = list(class_2_3.values_list('course_id', flat=True))
        id_list24 = list(class_2_4.values_list('course_id', flat=True))
        id_list25 = list(class_2_5.values_list('course_id', flat=True))
        id_list26 = list(class_2_6.values_list('course_id', flat=True))
        course1_1 = models.Course.objects.filter(id__in=id_list11)
        course1_2 = models.Course.objects.filter(id__in=id_list12)
        course1_3 = models.Course.objects.filter(id__in=id_list13)
        course1_4 = models.Course.objects.filter(id__in=id_list14)
        course1_5 = models.Course.objects.filter(id__in=id_list15)
        course1_6 = models.Course.objects.filter(id__in=id_list16)
        course2_1 = models.Course.objects.filter(id__in=id_list21)
        course2_2 = models.Course.objects.filter(id__in=id_list22)
        course2_3 = models.Course.objects.filter(id__in=id_list23)
        course2_4 = models.Course.objects.filter(id__in=id_list24)
        course2_5 = models.Course.objects.filter(id__in=id_list25)
        course2_6 = models.Course.objects.filter(id__in=id_list26)
        # 获取每个查询集的记录数
        count1 = course1_1.count()
        count2 = course1_2.count()
        count3 = course1_3.count()
        count4 = course1_4.count()
        count5 = course1_5.count()
        count6 = course1_6.count()

        # 确定这些记录数中的最大值
        max_count1 = max(count1, count2, count3, count4, count5, count6)

        diff1 = max_count1  - count1
        course1_1 = list(course1_1) + [None] * diff1
        diff2 = max_count1  - count2
        course1_2 = list(course1_2) + [None] * diff2
        diff3 = max_count1  - count3
        course1_3 = list(course1_3) + [None] * diff3
        diff4 = max_count1  - count4
        course1_4 = list(course1_4) + [None] * diff4
        diff5 = max_count1  - count5
        course1_5 = list(course1_5) + [None] * diff5
        diff6 = max_count1  - count6
        course1_6 = list(course1_6) + [None] * diff6

        # 获取每个查询集的记录数
        count1 = course2_1.count()
        count2 = course2_2.count()
        count3 = course2_3.count()
        count4 = course2_4.count()
        count5 = course2_5.count()
        count6 = course2_6.count()

        # 确定这些记录数中的最大值
        max_count2 = max(count1, count2, count3, count4, count5, count6)

        diff1 = max_count2 - count1
        course2_1 = list(course2_1) + [None] * diff1
        diff2 = max_count2  - count2
        course2_2 = list(course2_2) + [None] * diff2
        diff3 = max_count2 - count3
        course2_3 = list(course2_3) + [None] * diff3
        diff4 = max_count2  - count4
        course2_4 = list(course2_4) + [None] * diff4
        diff5 = max_count2  - count5
        course2_5 = list(course2_5) + [None] * diff5
        diff6 = max_count2  - count6
        course2_6 = list(course2_6) + [None] * diff6

        #print(course1_3)
        return render(request, 'mapdisplay.html', {"class_1_1": course1_1, "class_1_2": course1_2, "class_1_3": course1_3, "class_1_4": course1_4,
                "class_1_5": course1_5, "class_1_6": course1_6, "class_2_1": course2_1, "class_2_2": course2_2,
                "class_2_3": course2_3, "class_2_4": course2_4, "class_2_5": course2_5, "class_2_6": course2_6,
                "max_count1": max_count1, "max_count2": max_count2,"cols":8,"name":name})
    return render(request, 'map.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(username, password, confirm_password)
        if password == confirm_password:
            # 创建新用户并保存到数据库
            models.UserInfo.objects.create(name=username, password=password)
            messages.success(request, '注册成功！')
            print('注册成功')
            return redirect('/base/')
        else:
            messages.error(request, '密码和确认密码不匹配')

    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')


def course(request):
    # 获取课程表所有信息，存储在course_list
    course_list = models.Course.objects.all()
    return render(request, 'coursedisplay.html', {"list": course_list})


def addcourse(request):
    if request.method == 'POST':
        print(request.POST.get('name'), request.POST.get('credit'), request.POST.get('semester'),
              request.POST.get('category_id'))
        name = request.POST.get('name')
        credit = request.POST.get('credit')
        semester = request.POST.get('semester')
        category_id = request.POST.get('category_id')
        coursecode = request.POST.get('coursecode')

        try:
            son = models.Course.objects.get(name=name, credits=credit, semester=semester, category_id=category_id,
                                            coursecode=coursecode)
        except models.Course.DoesNotExist:
            # 要添加的课程不存在
            son = None

        if son is not None:
            messages.error(request, '课程已存在，添加失败')

        if son is None:
            models.Course.objects.create(name=name, credits=credit, semester=semester, category_id=category_id,
                                         coursecode=coursecode)
            messages.success(request, '添加课程成功！')
    categories = models.CourseCategory.objects.all()
    return render(request, 'courseadd.html', {"categories": categories})


def deletecourse(request):
    if request.method == 'POST':
        print("收到POST")
        course_id = request.POST.get('course_id')
        course = models.Course.objects.get(id=course_id)
        course.delete()
        messages.success(request, '删除课程成功！')
        return redirect('/base/datamanage/course/delete/')  # 重定向到课程删除页面

    courses = models.Course.objects.all()
    # print(courses)
    return render(request, 'coursedelete.html', {"courses": courses})


def coursecategoty(request):
    # 获取课程类别表所有信息，存储在category_list
    category_list = models.CourseCategory.objects.all()
    print(category_list)
    return render(request, 'course_category_display.html', {"list": category_list})


def addcoursecategory(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        parent_id = request.POST.get('parent_id')
        try:
            father = models.CourseCategory.objects.get(id=parent_id)
        except models.CourseCategory.DoesNotExist:
            # 父类别不存在
            father = None

        try:
            son = models.CourseCategory.objects.get(name=name)
        except models.CourseCategory.DoesNotExist:
            # 子类别不存在
            son = None

        if son is not None:
            messages.error(request, '课程类别已存在，添加失败')
        if father is None:
            messages.error(request, '父节点不存在，添加失败')

        if father is not None and son is None:
            models.CourseCategory.objects.create(name=name, parent_id=father.id)
            messages.success(request, '添加课程类别成功！')
    categories = models.CourseCategory.objects.all()
    return render(request, 'course_category_add.html', {"categories": categories})


def deletecoursecategoty(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = models.CourseCategory.objects.get(id=category_id)
        category.delete()
        messages.success(request, '删除课程成功！')
        return redirect('/base/datamanage/coursecategory/delete/')  # 重定向到课程类别展示页面

    categories = models.CourseCategory.objects.all()
    # print(categories)
    return render(request, 'course_category_delete.html', {"categories": categories})


def tree(request):
    newtraining = models.TrainingPlan.objects.last()
    print(newtraining)
    trainingcategories = models.TrainingCategory.objects.filter(training_plan_id=newtraining.id).all()
    categories = models.CourseCategory.objects.all()
    courses = models.Course.objects.all()
    return render(request, 'tree.html', {'categories': categories, 'courses': courses, 'newtraining': newtraining})


def logout(request):
    print("注销")
    request.session.clear()

    return redirect('/base/')


from django.http import JsonResponse


def training_plan(request):
    categories = models.CourseCategory.objects.all()
    return render(request, 'training_plan.html', {'categories': categories})


def get_courses_by_category(request):
    newtraining = models.TrainingPlan.objects.last()
    trainingcategories = models.TrainingCategory.objects.filter(training_plan_id=newtraining.id).all()
    categories = models.CourseCategory.objects.all()
    courses = models.Course.objects.all()
    return render(request, 'course_table.html',
                  {'categories': categories, 'courses': courses, 'newtraining': newtraining})


def get(request):
    category_id = request.GET.get('category_id')
    # print(category_id)
    # 根据category_id查询相关课程数据
    courses = models.Course.objects.filter(category_id=category_id)
    # 将查询结果渲染到一个HTML模板中，或者以JSON格式返回
    # 以下是以JSON格式返回的示例
    data = {
        'courses': [{'id': course.id, 'name': course.name, 'category': course.category.name,
                     'semester': course.semester, 'coursecode': course.coursecode}
                    for course in courses]
    }
    # print(data)
    return JsonResponse(data)


@csrf_exempt
def add_selected_courses(request):
    # 必修课
    print("add_selected_courses")
    credits = 0
    if request.method == 'POST':
        selected_courses = request.POST.getlist('selected_courses[]')
        current_category_id = request.POST.get('category_id')
        details = request.POST.get('details')
        print(selected_courses, current_category_id)
        # 在数据库中创建选定的课程记录
        for course_id in selected_courses:
            print(course_id)
            models.TrainingClass.objects.create(course_id=course_id, category_id=models.CourseCategory.objects.filter(
                id=current_category_id).first(), semester=models.Course.objects.filter(id=course_id).first().semester,
                                                training_plan_id=models.TrainingPlan.objects.last().id, must=True)
            # 计算必修课总学分
            str = models.Course.objects.filter(id=course_id).first().credits
            credits = credits + int(float(str))

        # print(details)
        models.TrainingCategory.objects.filter(training_plan_id=models.TrainingPlan.objects.last().id,
                                               category_id=current_category_id).update(credits=credits)
        models.TrainingCategory.objects.filter(training_plan_id=models.TrainingPlan.objects.last().id,
                                               category_id=current_category_id).update(detail=details)
        return JsonResponse({'message': '课程添加成功'}, status=200)

    return JsonResponse({'message': '请求方法不允许'}, status=405)


@csrf_exempt
def add_elective_courses(request):
    # 选修课
    print("get in elective")
    if request.method == 'POST':
        flag = 1
        selected_courses = request.POST.getlist('selected_courses[]')

        # 最少学分直接得到
        credits = request.POST.get('minimum_credits')
        current_category_id = request.POST.get('category_id')
        details = request.POST.get('details')

        # 在数据库中创建选定的课程记录
        for course_id in selected_courses:
            print(course_id)
            models.TrainingClass.objects.create(course_id=course_id, category_id=models.CourseCategory.objects.filter(
                id=current_category_id).first(), semester=models.Course.objects.filter(id=course_id).first().semester,
                                                training_plan_id=models.TrainingPlan.objects.last().id, must=False)
        print(details)
        models.TrainingCategory.objects.filter(training_plan_id=models.TrainingPlan.objects.last().id,
                                               category_id=current_category_id).update(credits=credits)
        models.TrainingCategory.objects.filter(training_plan_id=models.TrainingPlan.objects.last().id,
                                               category_id=current_category_id).update(detail=details)

        return JsonResponse({'message': '课程添加成功'}, status=200)

    return JsonResponse({'message': '请求方法不允许'}, status=405)


@csrf_exempt
def Trainingplan_generate(request):
    if request.method == 'POST':
        leaf_nodes = request.POST.getlist('leaf_nodes[]')
    leaf_nodes = list(set(leaf_nodes))
    print(leaf_nodes)

    for leaf_node_id in leaf_nodes:
        print("leafnode1")
        leaf_node = models.TrainingCategory.objects.filter(category_id=leaf_node_id).last()
        this_node = models.TrainingCategory.objects.filter(category_id=leaf_node_id).last()
        parent_node_id = this_node.parent
        parent_node = models.TrainingCategory.objects.filter(category_id=parent_node_id).last()
        newcredit = parent_node.credits + this_node.credits
        models.TrainingCategory.objects.filter(category_id=parent_node_id).update(credits=newcredit)
        while parent_node != None:
            this_node = models.TrainingCategory.objects.filter(category_id=parent_node_id).last()
            parent_node_id = this_node.parent
            parent_node = models.TrainingCategory.objects.filter(category_id=parent_node_id).last()
            # print(this_node,parent_node)
            if parent_node:
                newcredit = parent_node.credits + leaf_node.credits
                models.TrainingCategory.objects.filter(category_id=parent_node_id).update(credits=newcredit)

    return redirect('/training_plan_display/')


def Trainingplan_show(request):
    training_plan = models.TrainingPlan.objects.last()
    training_classes = models.TrainingClass.objects.filter(training_plan_id=training_plan.id).all()
    training_categories = models.TrainingCategory.objects.filter(training_plan_id=training_plan.id, credits__gt=0)

    return render(request, 'training_plan_display1.html',
                  {"training_plan": training_plan, "training_classes": training_classes,
                   "training_categories": training_categories})


def build_category_tree(parent_id=None):
    # 获取顶级类别或子类别
    categories = models.TrainingCategory.objects.filter(parent=parent_id)
    category_tree = []
    for category in categories:
        # 递归构建子树
        children = build_category_tree(category.category_id)
        category_tree.append({
            'name': category.name,
            'children': children,
            'credits': category.credits,
            'detail': category.detail
        })
        # print('xxx')
    return category_tree


def training_plan_display1(request):
    if request.method == 'POST':
        models.CourseCategory_display.objects.all().delete()
        name = request.POST.get('name')
        print(name)
        id = models.TrainingPlan.objects.filter(name=name).first()
        print(id.id)
        print("成功查找")
        training_categories = models.TrainingCategory.objects.filter(
            training_plan_id=id,
            credits__gt=0).order_by('id').all()
        #print(training_categories)
        training_categories = training_categories.exclude(category_id=36)
        print(training_categories)
        root1 = training_categories.filter(category_id=37).first()
        root2 = training_categories.filter(category_id=73).first()
        root3 = training_categories.filter(category_id=158).first()
        root4 = training_categories.filter(category_id=163).first()
        rootlist = []
        rootlist.append(root1)
        rootlist.append(root2)
        rootlist.append(root3)
        rootlist.append(root4)
        level_1 = models.CourseCategory.objects.filter(level=1)
        level_2 = models.CourseCategory.objects.filter(level=2)
        level_3 = models.CourseCategory.objects.filter(level=3)
        level_4 = models.CourseCategory.objects.filter(level=4)
        level_5 = models.CourseCategory.objects.filter(level=5)
        #print(rootlist)
        for root in rootlist:
            if root != None:
                models.CourseCategory_display.objects.create(
                    category_id=root.category_id,
                    name=root.name,
                    credits=root.credits,
                    detail=root.detail,
                    training_plan_id=root.training_plan_id,
                    parent_id=None  # 根节点的parent_id通常为None
                )
                training_categories = training_categories.exclude(category_id=root.category_id)
                print("trainingcategories删除了", root.category_id)
        #print(training_categories)
        for child_cates in training_categories:
            print("加入了", child_cates.category_id)
            models.CourseCategory_display.objects.create(
                category_id=child_cates.category_id,
                name=child_cates.name,
                credits=child_cates.credits,
                detail=child_cates.detail,
                training_plan_id=child_cates.training_plan_id,
                parent=models.CourseCategory_display.objects.filter(category_id=child_cates.parent).first()
                # 子节点的parent_id为父节点的实例
            )
        return redirect('/training_plan_display/')

    models.CourseCategory_display.objects.all().delete()
    return render(request, 'training_plan_display1.html')


def training_plan_display(request):
    list = models.CourseCategory_display.objects.all()
    return render(request, 'training_plan_display.html', {"categories": list})


def stopmakingtrainingplan(request):
    newtraining = models.TrainingPlan.objects.last()
    newaddcategories = models.TrainingCategory.objects.filter(training_plan_id=newtraining.id).all()
    print("删除", newtraining)
    newtraining.delete()
    for temp in newaddcategories:
        print("删除", temp)
        temp.delete()

    return redirect('/base/home/')


def searchcourse(request):
    value = request.GET.get('q')

    if value:
        # 使用 Q 对象进行 OR 过滤
        queryset = models.Course.objects.filter(Q(name__icontains=value) | Q(coursecode__icontains=value))
    else:
        # 如果没有查询值，则返回所有课程
        queryset = models.Course.objects.all()

    return render(request, 'searchcourse.html', {"queryset": queryset})


class CourseEditModelForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ["name", "category", "coursecode", "credits", "semester"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def course_edit(request, nid):
    row_object = models.Course.objects.filter(id=nid).first()

    if request.method == "GET":
        form = CourseEditModelForm(instance=row_object)
        return render(request, 'courseedit.html', {"form": form})

    form = CourseEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'courseedit.html', {"form": form})


def searchcoursecategory(request):
    value = request.GET.get('q')

    if value:
        # 使用 Q 对象进行 OR 过滤
        queryset = models.CourseCategory.objects.filter(Q(name__icontains=value) | Q(id__icontains=value))
    else:
        # 如果没有查询值，则返回所有课程
        queryset = models.CourseCategory.objects.all()

    return render(request, 'searchcoursecategory.html', {"queryset": queryset})


class CourseCategoryEditModelForm(forms.ModelForm):
    class Meta:
        model = models.CourseCategory
        fields = ["name", "parent", ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def coursecategory_edit(request, pid):
    row_object = models.CourseCategory.objects.filter(id=pid).first()

    if request.method == "GET":
        form = CourseCategoryEditModelForm(instance=row_object)
        return render(request, 'coursecategoryedit.html', {"form": form})

    form = CourseCategoryEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('coursecategory_list')
    return render(request, 'coursecategoryedit.html', {"form": form})
