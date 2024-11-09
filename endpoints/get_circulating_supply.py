# encoding: utf-8

from server import spectred_client


async def get_coinsupply():
    """
    Get $SPR coin supply information
    """
    resp = await spectred_client.request("getCoinSupplyRequest")
    return {
        "circulatingSupply": resp["getCoinSupplyResponse"]["circulatingSompi"],
        "totalSupply": resp["getCoinSupplyResponse"]["circulatingSompi"],
        "maxSupply": resp["getCoinSupplyResponse"]["maxSompi"],
    }


async def get_circulating_coins(in_billion: bool = False):
    """
    Get circulating amount of $SPR coin as numerical value
    """
    resp = await spectred_client.request("getCoinSupplyRequest")
    coins = str(float(resp["getCoinSupplyResponse"]["circulatingSompi"]) / 1e9)
    if in_billion:
        return str(round(float(coins) / 1e9, 2))
    else:
        return coins


async def get_total_coins():
    """
    Get total amount of $SPR coin as numerical value
    """
    resp = await spectred_client.request("getCoinSupplyRequest")
    return str(float(resp["getCoinSupplyResponse"]["circulatingSompi"]) / 1e8)
