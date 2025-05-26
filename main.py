import os
import asyncio
from contextual import AsyncContextualAI
from dotenv import load_dotenv
import sys
import pdb

load_dotenv()
# Import the AsyncContextualAI class from the contextual module
client = AsyncContextualAI(
    api_key=os.environ.get(
        "CONTEXTUAL_API_KEY"
    ),  # This is the default and can be omitted
)


async def main() -> None:
    pdb.set_trace()

    dbs = await client.datastores.list()

    usrs = await client.users.list()
    if not any(db.name == "pacp" for db in dbs):
        await client.datastores.create(
            name="pacp",
        )


asyncio.run(main())
