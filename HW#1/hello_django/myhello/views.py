#from django.http import HttpResponse

# Create your views here.
#def myIndex(request):
    #my_name = request.POST.get('name',"CGU")
    #return HttpResponse("Hello " + my_name)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
import logging

from .models import Post
from .models import Course

logger = logging.getLogger('django')

#@api_view(['GET'])
#class HelloApiView(APIView):
# def myhello_api(request):
#         my_name = request.GET.get('name' , None)
#         if my_name:
#             #retValue = {}
#             #retValue['data'] = "Hello" + my_name
#             return Response({"data": "Hello" + my_name}, status=status.HTTP_200_OK)
#         else:
#             return Response(
#                 {"res": "parameter: name is None"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

# def add_post(request):
#     title = request.GET.get('title', '')
#     content = request.GET.get('content', '')
#     photo = request.GET.get('photo', '')
#     location = request.GET.get('location', '')

#     new_post = Post()
#     new_post.title = title
#     new_post.content = content
#     new_post.photo = photo
#     new_post.location = location
#     new_post.save()
#     logger.debug(" ************** myhello_api: " + title)
#     if title:
#         return Response({"data": title + " insert!"}, status=status.HTTP_200_OK)
#     else:
#         return Response(
#             {"res": "parameter: name is None"},
#             status=status.HTTP_400_BAD_REQUEST
#         )
    
# @api_view(['GET'])
# def list_post(request):
#     posts = Post.objects.all().values()
#     return JsonResponse(list(posts), safe=False)
    # return Response({"data":
    #                  json.dumps(
    #                      list(posts),
    #                      sort_keys = True,
    #                      indent = 1,
    #                      cls = DjangoJSONEncoder)},
    #                      status=status.HTTP_200_OK)

#課程列表
@api_view(["GET"])
def course_list(request):
    courses = Course.objects.all().values("id","Department","CourseTitle","Instructor")
    return Response(list(courses),status=status.HTTP_200_OK)

#新增課程
@api_view(["POST"])
def add_course(request):
    data = request.data
    Department = data.get("Department")
    CourseTitle = data.get("CourseTitle")
    Instructor = data.get("Instructor")

    course = Course.objects.create(
        Department=Department,
        CourseTitle=CourseTitle,
        Instructor=Instructor
    )

    return Response(
        {"message": "課程新增成功","id": course.id},
        status=status.HTTP_201_CREATED
    )

#HW1另種寫法
# @api_view(['POST'])
# def add_course(request):
#     Department = request.data.get('Department', '')
#     CourseTitle = request.data.get('CourseTitle', '')
#     Instructor = request.data.get('Instructor', '')
    

#     if not Department or not CourseTitle or not Instructor:
#         return Response({"res": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

#     new_course = Course(Department=Department, CourseTitle=CourseTitle, Instructor=Instructor)
#     new_course.save()

#     return Response({"Course": CourseTitle + " inserted!"}, status=status.HTTP_201_CREATED)

# @api_view(['GET'])
# def course_list(request):
#     courses = Course.objects.all().values()
#     return Response({"data": list(courses)}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def course_list(request):
#     courses = Course.objects.all().values()
#     #return JsonResponse(list(courses), safe=False)
#     return Response({"data":
#                      json.dumps(
#                          list(courses),
#                          sort_keys = True,
#                          indent = 1,
#                          cls = DjangoJSONEncoder)},
#                          status=status.HTTP_200_OK)
