from rest_framework import permissions

class MyUserCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # if(
        #     request.method in permissions.SAFE_METHODS
        # ):
        #     return True
        return (
            request.user.is_authenticated and request.user.is_superuser
        )

        # se eu precisar autorizar alguma rota get pra um usuário normal é só eu não inserir essas restrições pra ele ou criar outro custom permission
        