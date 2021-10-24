import bloxypy
import asyncio

client = bloxypy.client(None)

async def Main():
  group_roles = client.get_group_roles(1) # this gets the roles of the group


  if group_roles:
    print("group roles found!")
    return True
  else:
    print("no group roles found!")
    return False 



 asyncio.run(Main())   
