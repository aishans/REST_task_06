from rest_framework.permissions import BasePermission
from datetime import date


class IsOwner(BasePermission):
    message = "You must be the owner of this booking in order to modify or cancel."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False
class IsPast(BasePermission):
	message= " cant modify booking that's unless its more than three days"

	def has_object_permission(self, request, view, obj):
		time_since_insertion = (obj.date- date.today()).days 
		if(time_since_insertion) >= 3: 
			return True
		else:
			return False