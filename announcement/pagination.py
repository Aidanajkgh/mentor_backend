from rest_framework import pagination


class AnnounccementPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'per_page'