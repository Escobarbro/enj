import asyncio
from pytgcalls import idle
import os
import sys
import random
import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
from bot import *
from pyromod import listen

async def main():
    await start_helalbot()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
