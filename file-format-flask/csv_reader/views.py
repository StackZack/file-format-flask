from flask import views
import os
from csv import DictReader


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
            """Alternative to DictReader is the reader function.
            The reader function will return a list of strings instead.
            The rows could then be appended to the payload using built
            in join function.
            i.e. ",".join(row)
            """
            sample_reader = DictReader(f)
            for row in sample_reader:
                csv_data.append(row)
            return {"data": csv_data}
