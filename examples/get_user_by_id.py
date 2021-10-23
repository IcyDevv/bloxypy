import bloxapi
import asyncio

client = bloxapi.Client(None)

async def main():
    user_object = await client.get_user_by_id(1) # This returns the user object.
    if user_object: # Checking if this user exists.
        print('This user exists!')
        print(user_object.name, user_object.id, user_object.status, user_object.about) 

asyncio.run(main())