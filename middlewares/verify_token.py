from fastapi import Request, Response
from fastapi.routing import APIRoute

from utils.jwt import validate_token


# TODO: Arreglar el jwt
class VerifyTokenRoute(APIRoute):
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def verify_token_middleware(request: Request, response: Response):
            token = request.headers["Authorization"].split(" ")[1]
            validation_response = validate_token(token, False)

            if validation_response == None:
                response.headers["x-uid"] = "sebasthepro"
                return await original_route_handler(request)
            else:
                return validation_response

        return verify_token_middleware
