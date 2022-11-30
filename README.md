# bloxy.py

![](https://img.shields.io/github/stars/IcyDevv/bloxypy) ![](https://img.shields.io/github/forks/IcyDevv/bloxypy) ![](https://img.shields.io/github/license/IcyDevv/bloxypy) ![](https://img.shields.io/github/issues/IcyDevv/bloxypy)

A simple Python API Wrapper for roblox!

# ⚠️ ATTENTION , PLEASE READ! ⚠️
## Message from 30/11/2022 or 11/30/2022

## To any Roblox's developers using bloxy.py in a python related roblox projects. This message is for people still using bloxy.py in late 2022. In February of 2023 (Exact date wll be specified soon.) Bloxypy will end support and will no longer be apart of github as it will go private. The reason for this change is the code is messy and outdated and alot of the functions have tons of bugs making it almost impossible to use. The project has been inactive for almost 9 mouths and to any users, I aplogize for this. I will release some more update until about January when the day comes that it will end support completely. A new, improved, revamped version of bloxypy will release in the beginning of 2023. Imformation about that will be release soon. For now this is a warning and disclaimer for any devforum users on roblox interested and impressed with the project.

### Key Features

- Covers a large majority of the ROBLOX API.
- Modern Pythonic API using `async` and `await`.
- Easy and super simple to use.

### Installing

**Python 3.6.0 or higher is required**
```py
# Upgrade pip
# If 'python' does not work try 'py'
$ python -m pip install --upgrade pip

# Install the Module
$ pip install git+https://github.com/IcyDevv/bloxypy.git
```

### Basic Example

```py
import bloxpy
import asyncio

client = bloxypy.Client(None)

async def main():
    user_object = await client.get_user_by_id(1) # This returns the user object.
    if user_object: # Checking if this user exists.
        print('This user exists!')
        print(user_object.name, user_object.id, user_object.status, user_object.about) 

asyncio.run(main())
```

More examples can be found in the examples directory.
