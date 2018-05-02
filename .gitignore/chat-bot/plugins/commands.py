import logging

from plugin import Plugin
from utils import rich_response


log = logging.getLogger('discord')


class Commands(Plugin):

    fancy_name = 'Custom Commands'

    async def get_commands(self, server):
        storage = await self.get_storage(server)
        commands = sorted(await storage.smembers('commands'))
        cmds = []
        for command in commands:
            cmd = {
                'name': command
            }
            cmds.append(cmd)
        return cmds

    async def on_message(self, message):
        if message.author.bot:
            return
        if message.author.id == self.multigaming.user.id:
            return
        storage = await self.get_storage(message.server)
        commands = await storage.smembers('commands')
        for command in commands:
            if not message.content.startswith(command):
                continue

            splitted = message.content.split()
            if splitted[0] != command:
                continue

            args = splitted[1:]

            log.info('{}#{}@{} >> {}'.format(
                message.author.name,
                message.author.discriminator,
                message.server.name,
                message.clean_content
            ))
            response = await storage.get('command:{}'.format(command))
            response = rich_response(response, args=args, message=message)

            tags = {'cmd': 'custom'}
            self.multigaming.stats.incr('multigaming.command', tags=tags)

            await  self.multigaming.send_message(
                message.channel,
                response
            )
