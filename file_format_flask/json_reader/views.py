from flask import views
import json
import os


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
        with open(
            os.path.join(
                os.path.dirname(__file__),
                "resources",
                "sample.json",
            ),
            "r",
        ) as f:
            return json.load(f)
