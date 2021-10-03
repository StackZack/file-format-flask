from flask import views
import os
from avro.datafile import DataFileReader
from avro.io import DatumReader


class AvroReaderAPI(views.MethodView):
    """Avro reader implementation of Flask MethodView class that is utilized
    by blueprint to implement common Avro reader routes.

    :param views: Inherits Flask MethodView
    :type views: Class object
    """

    def get(self):
        """Handles HTTP GET requests.

        :return: Output of Avro file.
        :rtype: dict
        """
        with DataFileReader(
            open(
                os.path.join(
                    os.path.dirname(__file__),
                    "resources",
                    "output.avro",
                ),
                "rb",
            ),
            DatumReader(),
        ) as f:
            avro_data = []
            for row in f:
                avro_data.append(row)
            return {"data": avro_data}
