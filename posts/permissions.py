class BasePermission(object):
    """
    A base class from whitch all permission classes should inherit.
    """

    def has_permission(self,request,view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True


    def has_object_permission(self,request,view,obj):
        """
        Return `True` if permission is granted, `False` otherwise. 
        """
        return True








