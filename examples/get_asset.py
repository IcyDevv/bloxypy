import bloxypy
import asyncio

client = bloxypy.Client(None)

async def Main():
    asset = client.get_asset(1) # put your id here
    if asset:
        print("Asset found!") # if asset is found it will print the asset id and return true
        print(asset.name, asset.id, asset.version, asset.description)
        return True
    else:
        print("Asset was not found or it has been deleted!") # if asset is not found it will print "asset not found" and return false
        return False

asyncio.run(Main()) # run the function
