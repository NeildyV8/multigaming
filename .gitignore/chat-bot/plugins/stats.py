from plugin import Plugin
import asyncio
import logging
import discord
import aiohttp
import json
import os

logs = logging.getLogger('discord')

class Stats(Plugin):

    is_global = True

    async def carbon_stats(self):
        carbon_key = os.getenv('CARBONITEX_KEY')
        if not carbon_key:
            return

        url = 'https://www.carbonitex.net/discord/data/botdata.php?id={}'.format(
            self.multigaming.user.id
        )
        with aiohttp.ClientSession() as session:
            payload = {
                'key': carbon_key,
                'servercount': len(self.multigaming.servers)
            }
            headers = {'content-type': 'application/json'}
            async with session.post(url, headers=headers,
                                    data=json.dumps(payload)) as resp:
                pass

    async def on_server_join(self, server):
        await self.multigaming.stats.incr('multigaming.server_join')
        for member in server.members:

    async def on_channel_create(self, channel):
        await self.db.redis.sadd('multigaming:stats:channels', channel.id)

    async def on_message(self, message):
        await self.multigaming.stats.incr('multigaming.received_messages')
        if message.author.id == self.multigaming.user.id:
            await self.multigaming.stats.incr('multigaming.sent_messages')

    async def on_ready(self):
        """Initialize stats"""
        #await self.carbon_stats()

        # Total members
        members = set(self.multigaming.get_all_members())
        channels = set(self.multigaming.get_all_channels())
        servers = multigaming.servers
        for server in servers:
            await self.multigaming.stats.set('multigaming.servers', server.id)
        for channel in channels:
            await self.multigaming.stats.set('multigaming.channels', channel.id)
        for member in members:
            await self.multigaming.stats.set('multigaming.users', member.id)

