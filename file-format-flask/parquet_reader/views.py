from flask import views
import os
from pyarrow.parquet import ParquetFile


class ParquetReaderAPI(views.MethodView):
    """Parquet reader implementation of Flask MethodView class that is utilized
    by blueprint to implement common Parquet reader routes.

    :param views: Inherits Flask MethodView
    :type views: Class object
    """

    def get(self):
        """Handles HTTP GET requests.

        :return: Output of Parquet file.
        :rtype: dict
        """
        parquet_data = []
        table = ParquetFile(
            os.path.join(
                os.path.dirname(__file__),
                "resources",
                "sample.parquet",
            )
        ).read()

        for batch in table.to_batches():
            bd = batch.to_pydict()
            [
                parquet_data.append(
                    {
                        "id": person_id,
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                    }
                )
                for person_id, first_name, last_name, email in zip(
                    bd["id"], bd["first_name"], bd["last_name"], bd["email"]
                )
            ]

        return {"data": parquet_data}
