import connexion
import six

from imaginairy import imagine, imagine_image_files, ImaginePrompt, WeightedPrompt, LazyLoadingImage
from swagger_server.models.image_info import ImageInfo  # noqa: E501
from swagger_server.models.temperature_summary import TemperatureSummary  # noqa: E501
from swagger_server import util


def generate_image(body=None):  # noqa: E501
    """generate_image

    Generates image from imaginAIry # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = ImageInfo.from_dict(connexion.request.get_json())  # noqa: E501

    f = open("garage.jpg", 'rb')
    cont = f.read()
    f.close()

    return cont


def image_summary():  # noqa: E501
    """image_summary

     # noqa: E501


    :rtype: TemperatureSummary
    """
    return 'do some magic!'
