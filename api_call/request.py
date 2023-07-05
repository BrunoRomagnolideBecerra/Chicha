import requests


def get_endpoint(name):
    endpoint_name = name.upper().replace(" ", "_")
    return getattr(Requests, endpoint_name)


class Requests:

    ENDPOINT_A = ""
    ENDPOINT_B = ""

    def get(self, endpoint_name, params=None, **kwargs):
        """Sends a GET request.
            :param endpoint_name: URL for the endpoint request.
            :param params: (optional) Dictionary, list of tuples or bytes to send
                in the query string for the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: Json response.
        """
        return requests.get(get_endpoint(endpoint_name), params, **kwargs).json()

    def post(self, endpoint_name, data=None, json=None, **kwargs):
        """Sends a POST request.
            :param endpoint_name: URL for the endpoint request.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param json: (optional) json data to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: Json response.
        """
        return requests.post(get_endpoint(endpoint_name), data, json, **kwargs).json()

    def put(self, endpoint_name, data=None, **kwargs):
        """Sends a PUT request.
            :param endpoint_name: URL for the endpoint request.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param json: (optional) json data to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: Json response.
        """
        return requests.put(get_endpoint(endpoint_name), data, **kwargs).json()

    def patch(self, endpoint_name, data=None, **kwargs):
        """Sends a PATCH request.
            :param endpoint_name: URL for the endpoint request.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param json: (optional) json data to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: Json response.
        """
        return requests.patch(get_endpoint(endpoint_name), data, **kwargs).json()

    def delete(self, endpoint_name, **kwargs):
        """Sends a DELETE request.
            :param endpoint_name: URL for the endpoint request.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: Json response.
        """
        return requests.delete(get_endpoint(endpoint_name), **kwargs).json()
