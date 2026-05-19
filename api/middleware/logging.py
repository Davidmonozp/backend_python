import logging

logger = logging.getLogger(__name__)

class LoggingAvanzadoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Capturar datos del usuario autenticado por JWT
        if request.user and request.user.is_authenticated:
            roles = [g.name for g in request.user.groups.all()]
            user_info = f"Usuario: {request.user.username} (Roles: {roles})"
        else:
            user_info = "Usuario: Anónimo"

        # Estructura solicitada en la prueba técnica
        log_message = f"MÉTODO: {request.method} | URI: {request.path} | STATUS: {response.status_code} | {user_info}"

        print(f"\n[LOG DE OPERACIÓN] {log_message}\n")

        return response