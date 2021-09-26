from flask import views


class JsonReaderAPI(views.MethodView):
    """JSON reader implementation of Flask MethodView class that is utilized
    by blueprint to implement common JSON reader routes.

    :param views: Inherits Flask MethodView
    :type views: Class object
    """

    def get(self):
        """Handles HTTP GET requests.

        :return: Output of JSON file.
        :rtype: dict
        """
        test = {
            "test": "test message",
        }
        return test
