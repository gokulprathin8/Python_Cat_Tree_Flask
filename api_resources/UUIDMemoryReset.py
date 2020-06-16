import uuid
from flask_restful import Resource

class UUIDMemoryReset(Resource):
    def aax(self):
        return str(uuid.uuid4())