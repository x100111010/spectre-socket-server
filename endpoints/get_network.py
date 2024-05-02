# encoding: utf-8

from server import spectred_client


async def get_network():
    """
    Get some global spectre network information
    """
    resp = await spectred_client.request("getBlockDagInfoRequest")
    return resp["getBlockDagInfoResponse"]
