# encoding: utf-8

from server import spectred_client


async def get_info():
    """
    Get some global Spectre BlockDAG information
    """
    resp = await spectred_client.request("getInfoRequest")
    return resp["getInfoResponse"]
