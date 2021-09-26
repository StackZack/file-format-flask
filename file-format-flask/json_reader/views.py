from flask import views


class JsonReaderAPI(views.MethodView):
    def get(self):
        test = {
            "test": "test message",
        }
        return test
