import bloxypy
import asyncio

client = bloxypy.client(None)

async def Main():
  group_roles = client.get_group_roles(1) # this gets the roles of the group
  if group_roles:
    print("group roles found!")
    return True # return true if group i found/roles are found
  else:
    print("no group roles found!")
    return False # return false if the group doesnt exist

 asyncio.run(Main()) # run the function
