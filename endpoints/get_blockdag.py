# encoding: utf-8

from server import spectred_client


async def get_blockdag():
    """
    Get some global Spectre BlockDAG information
    """
    resp = await spectred_client.request("getBlockDagInfoRequest")
    return resp["getBlockDagInfoResponse"]
