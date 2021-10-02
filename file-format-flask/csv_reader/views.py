from flask import views
import os
from csv import reader


class CsvReaderAPI(views.MethodView):
    """CSV reader implementation of Flask MethodView class that is utilized
    by blueprint to implement common CSV reader routes.

    :param views: Inherits Flask MethodView
    :type views: Class object
    """

    def get(self):
        """Handles HTTP GET requests.

        :return: Output of CSV file.
        :rtype: dict
        """
        with open(
            os.path.join(
                os.path.dirname(__file__),
                "resources",
                "sample.csv",
            ),
            "r",
        ) as f:
            csv_data = []
            sample_reader = reader(f, delimiter=',')
            for row in sample_reader:
                csv_data.append(",".join(row))
            return {"data": csv_data}
