from flask import views
import os
from pyarrow.orc import ORCFile


class OrcReaderAPI(views.MethodView):
    """ORC reader implementation of Flask MethodView class that is utilized
    by blueprint to implement common ORC reader routes.

    :param views: Inherits Flask MethodView
    :type views: Class object
    """

    def get(self):
        """Handles HTTP GET requests.

        :return: Output of ORC file.
        :rtype: dict
        """
        orc_data = []
        table = ORCFile(
            os.path.join(
                os.path.dirname(__file__),
                "resources",
                "sample.orc",
            )
        ).read()

        for batch in table.to_batches():
            bd = batch.to_pydict()
            [
                orc_data.append(
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

        return {"data": orc_data}
