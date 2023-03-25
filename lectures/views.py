from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .models import Lecture
from . import serializers
from rest_framework import permissions
from categories.models import Category
from categories.serializers import CategorySerializer
from django.conf import settings
from users.models import User


#
class Lectures(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1

        # Get search query from query params
        try:
            search_query = request.query_params.get("search", "")
        except:
            search_query = ""

        # settings 로 보낼것.
        print(search_query)
        page_size = 30
        start = (page - 1) * page_size
        end = start + page_size
        lectures = Lecture.objects.filter(lectureTitle__icontains=search_query)
        total_num = lectures.count()
        lectures = lectures[start:end]
        print(total_num)
        serializer = serializers.LectureListSerializer(lectures, many=True)

        return Response({"data": serializer.data, "totalNum": total_num})

    def post(self, request):
        if request.user.isInstructor:
            serializer = serializers.LectureListSerializer(data=request.data)
            if serializer.is_valid():
                lecture = serializer.save()
                serializer = serializers.LectureListSerializer(lecture)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise ParseError()


class LecturesDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Lecture.objects.get(pk=pk)
        except Lecture.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        lecture = self.get_object(pk)
        serializer = serializers.LectureSerializer(lecture)
        return Response(serializer.data)

    def put(self, request, pk):
        lecture = self.get_object(pk)
        serializer = serializers.LectureListSerializer(
            lecture,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_lecture = serializer.save()
            return Response(
                serializers.LectureListSerializer(updated_lecture).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        room = self.get_object(pk)
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class SearchLectures(APIView):
    def get(self, request):
        # Filter by search words
        search_words = request.query_params.get("s", "")
        user = User.objects.get(name__icontains=search_words)
        if search_words:
            lectures = Lecture.objects.filter(
                lectureTitle__icontains=search_words
            ) or Lecture.objects.filter(lectureTitle__icontains=search_words)
        else:
            lectures = Lecture.objects.all()
        # Apply category filter if specified
        # Paginate results
        total_num = lectures.count()
        page_size = 30
        page = int(request.query_params.get("page", 1))
        start = (page - 1) * page_size
        end = start + page_size
        paged_lectures = lectures[start:end]
        # Serialize results
        serializer = serializers.LectureListSerializer(paged_lectures, many=True)
        return Response({"data": serializer.data, "totalNum": total_num})


# class OneCategory(APIView):
#     def get_CategoryObject(self, category1):
#         try:
#             category = Category.objects.get(classification=category1)
#             return Category.objects.filter(parent=category)
#         except Category.DoesNotExist:
#             raise NotFound

#     def get(self, request, category1):

#         categories = self.get_CategoryObject(category1)
#         union_query = None
#         for category in categories:
#             lectures = Lecture.objects.filter(categories=category)
#             print(lectures)
#             if union_query is None:
#                 union_query = lectures
#             else:
#                 union_query = union_query.union(lectures)
#         total_num = union_query.count()
#         page_size = 30
#         page = int(request.query_params.get("page", 1))
#         start = (page - 1) * page_size
#         end = start + page_size
#         paged_union_query = union_query[start:end]
#         # Serialize results
#         serializer = serializers.LectureListSerializer(paged_union_query, many=True)
#         return Response({"data": serializer.data, "totalNum": total_num})


class OneCategory(APIView):
    def get_CategoryObject(self, category1):
        try:
            category = Category.objects.get(classification=category1)
            return Category.objects.filter(parent=category)
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, category1):
        # Get child categories of specified category
        categories = self.get_CategoryObject(category1)
        # Get search query from query parameters
        search_query = request.query_params.get("search", "")
        # Get all lectures that belong to any of the child categories
        union_query = None
        for category in categories:
            lectures = Lecture.objects.filter(categories=category)
            # Filter the lectures based on search query
            if search_query:
                lectures = lectures.filter(lectureTitle__icontains=search_query)
            if union_query is None:
                union_query = lectures
            else:
                union_query = union_query.union(lectures)
        # Count the total number of lectures
        total_num = union_query.count()
        # Get page number from query parameters
        page = int(request.query_params.get("page", 1))
        # Set page size and calculate start and end indices
        page_size = 30
        start = (page - 1) * page_size
        end = start + page_size
        # Slice the data based on start and end indices
        paged_union_query = union_query[start:end]
        # Serialize results
        serializer = serializers.LectureListSerializer(paged_union_query, many=True)
        # Construct the response
        return Response({"data": serializer.data, "totalNum": total_num})


# class OneCategoryPage(APIView):
#     def get_CategoryObject(self, category1):
#         try:
#             category = Category.objects.get(classification=category1)
#             return Category.objects.filter(parent=category)
#         except Category.DoesNotExist:
#             raise NotFound

#     def get(self, request, category1, pages):
#         categories = self.get_CategoryObject(category1)
#         union_query = None
#         for category in categories:
#             lectures = Lecture.objects.filter(categories=category)
#             print(lectures)
#             if union_query is None:
#                 union_query = lectures
#             else:
#                 union_query = union_query.union(lectures)
#         total_num = union_query.count()
#         page_size = 30

#         start = (pages - 1) * page_size
#         end = start + page_size
#         paged_union_query = union_query[start:end]
#         # Serialize results
#         serializer = serializers.LectureListSerializer(paged_union_query, many=True)
#         return Response({"data": serializer.data, "totalNum": total_num})


class OneCategoryPage(APIView):
    def get_CategoryObject(self, category1):
        try:
            category = Category.objects.get(classification=category1)
            return Category.objects.filter(parent=category)
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, category1, pages):
        # Get child categories of specified category
        categories = self.get_CategoryObject(category1)
        # Get search query from query parameters
        search_query = request.query_params.get("search", "")
        # Get all lectures that belong to any of the child categories
        union_query = None
        for category in categories:
            lectures = Lecture.objects.filter(categories=category)
            # Filter the lectures based on search query
            if search_query:
                lectures = lectures.filter(lectureTitle__icontains=search_query)
            if union_query is None:
                union_query = lectures
            else:
                union_query = union_query.union(lectures)
        # Count the total number of lectures
        total_num = union_query.count()
        # Set page size and calculate start and end indices
        page_size = 30
        start = (pages - 1) * page_size
        end = start + page_size
        # Slice the data based on start and end indices
        paged_union_query = union_query[start:end]
        # Serialize results
        serializer = serializers.LectureListSerializer(paged_union_query, many=True)
        # Construct the response
        return Response({"data": serializer.data, "totalNum": total_num})


# class TwoCategory(APIView):
#     def get_CategoryObject(self, category2):
#         try:
#             return Category.objects.get(classification=category2)
#         except Category.DoesNotExist:
#             raise NotFound

#     def get(self, request, category1, category2):
#         category = self.get_CategoryObject(category2)
#         print(category)
#         lectures = Lecture.objects.filter(categories=category)
#         total_num = lectures.count()
#         page_size = 30
#         page = int(request.query_params.get("page", 1))
#         start = (page - 1) * page_size
#         end = start + page_size
#         paged_lectures = lectures[start:end]
#         # Serialize results
#         serializer = serializers.LectureListSerializer(paged_lectures, many=True)
#         return Response({"data": serializer.data, "totalNum": total_num})


# class TwoCategoryPage(APIView):
#     def get_CategoryObject(self, category2):
#         try:
#             return Category.objects.get(classification=category2)
#         except Category.DoesNotExist:
#             raise NotFound

#     def get(self, request, category1, category2, pages):
#         category = self.get_CategoryObject(category2)
#         print(category)
#         lectures = Lecture.objects.filter(categories=category)
#         total_num = lectures.count()
#         page_size = 30
#         # page = int(request.query_params.get("page", 1))
#         start = (pages - 1) * page_size
#         end = start + page_size
#         paged_lectures = lectures[start:end]
#         # Serialize results
#         serializer = serializers.LectureListSerializer(paged_lectures, many=True)
#         return Response({"data": serializer.data, "totalNum": total_num})


class TwoCategory(APIView):
    def get_CategoryObject(self, category2):
        try:
            return Category.objects.get(classification=category2)
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, category1, category2):
        # Get category object from database
        category = self.get_CategoryObject(category2)
        # Get search query from query parameters
        search_query = request.query_params.get("search", "")
        # Get lectures that belong to the specified category
        lectures = Lecture.objects.filter(categories=category)
        # Filter the lectures based on search query
        if search_query:
            lectures = lectures.filter(lectureTitle__icontains=search_query)
        # Count the total number of lectures
        total_num = lectures.count()
        # Set page size and calculate start and end indices
        page_size = 30
        page = int(request.query_params.get("page", 1))
        start = (page - 1) * page_size
        end = start + page_size
        # Slice the data based on start and end indices
        paged_lectures = lectures[start:end]
        # Serialize results
        serializer = serializers.LectureListSerializer(paged_lectures, many=True)
        # Construct the response
        return Response({"data": serializer.data, "totalNum": total_num})


class TwoCategoryPage(APIView):
    def get_CategoryObject(self, category2):
        try:
            return Category.objects.get(classification=category2)
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, category1, category2, pages):
        # Get category object from database
        category = self.get_CategoryObject(category2)
        # Get search query from query parameters
        search_query = request.query_params.get("search", "")
        # Get lectures that belong to the specified category
        lectures = Lecture.objects.filter(categories=category)
        # Filter the lectures based on search query
        if search_query:
            lectures = lectures.filter(lectureTitle__icontains=search_query)
        # Count the total number of lectures
        total_num = lectures.count()
        # Set page size and calculate start and end indices
        page_size = 30
        start = (pages - 1) * page_size
        end = start + page_size
        # Slice the data based on start and end indices
        paged_lectures = lectures[start:end]
        # Serialize results
        serializer = serializers.LectureListSerializer(paged_lectures, many=True)
        # Construct the response
        return Response({"data": serializer.data, "totalNum": total_num})


class InstructorName(APIView):
    def get(self, request, username):
        # print("username", username)
        try:
            user = User.objects.get(username=username)

            user_lecture = Lecture.objects.filter(instructor=user)
        except Lecture.DoesNotExist:
            raise NotFound
        serializer = serializers.LectureDetailSerializer(user_lecture, many=True)
        return Response(serializer.data)




class MainPage(APIView):
    def get(self, request):
        # Get all lectures
        lectures = Lecture.objects.all()
        # Get all categories
        categories = Category.objects.all()
        # Get all instructors
        instructors = User.objects.all()
        # Get all tags
        # tags = Tag.objects.all()
        # Serialize results
        serializer_lectures = serializers.LectureListSerializer(lectures, many=True)
        # serializer_categories = serializers.CategorySerializer(categories, many=True)
        # serializer_instructors = serializers.InstructorSerializer(instructors, many=True)
        # serializer_tags = serializers.TagSerializer(tags, many=True)
        # Construct the response
        return Response(
            {
                "lectures": serializer_lectures.data,
                # "categories": serializer_categories.data,
                # "instructors": serializer_instructors.data,
                # "tags": serializer_tags.data,
            }
        )