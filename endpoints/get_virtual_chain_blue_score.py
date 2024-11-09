# encoding: utf-8

from server import spectred_client


async def get_virtual_selected_parent_blue_score():
    """
    Returns the blue score of virtual selected parent
    """
    resp = await spectred_client.request("getSinkBlueScoreRequest")
    return resp["getSinkBlueScoreResponse"]
