from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 50

    def get_page_num(self) -> int:
        try:
            return int(self.request.GET.get("page", 1))
        except ValueError as e:
            raise ValidationError({"page": "Page number must be an integer"}) from e

    def get_paginated_response(self, data):
        current_page = self.get_page_num()
        return Response(
            {
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "current_page": current_page,
                "first_page": 1,
                "last_page": self.page.paginator.num_pages,
                "results": data,
            }
        )