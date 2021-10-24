import bloxypy
import asyncio

group = bloxypy.Group(None)

async def Main():
  group_roles = group.get_group_roles(1) # this gets the roles of the group
  if group_roles:
    print("group roles found!")
    return True # return true if group i found/roles are found
  else:
    print("no group roles found!")
    return False # return false if the group doesnt exist

 asyncio.run(Main()) # run the function
