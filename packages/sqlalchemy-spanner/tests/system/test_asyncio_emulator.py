import asyncio
import pytest
import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

from sqlalchemy.testing.plugin.plugin_base import fixtures

class AsyncioEmulatorTest(fixtures.TestBase):
    @pytest.mark.asyncio
    async def test_async_execute_on_emulator(self):
        os.environ["SPANNER_EMULATOR_HOST"] = "localhost:9010"
        
        database_url = "spanner+spanner_asyncio:///projects/test-project/instances/test-instance/databases/test-database"
        engine = create_async_engine(database_url)
        
        async with engine.connect() as conn:
            res = await conn.execute(text("SELECT 1"))
            result = res.fetchone()
            assert result[0] == 1
            print("\nSuccessfully executed query on Spanner emulator!")
