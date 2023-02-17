from .config import config_t
from .logger import logger_t
import discord

class ticketer_t(discord.Client):
    """
    This class is main ticketer class. That store routines useable to 
    creating tickets, logging and connecting to discord.
    """

    def __init__(self, config, logger):
        """
        This function create new ticketer, from config and logger
        dependences. That veryfi that given objects is valid childs.
        :config: Config from config_t child
        :logger: Logger from logger_t child
        """

        if not issubclass(type(config), config_t):
            raise Exception("Given config is not valid config_t!")

        if not issubclass(type(logger), logger_t):
            raise Exception("Given logger is not valid logger_t")

        self.config = config
        self.logger = logger

        super(ticketer_t, self).__init__(intents = discord.Intents.all())
    

    def get_new_channel_name(self, name, channels):
        """
        This function return name for new channel, from given prefix, and
        channels list as list.
        :name: Name prefix
        :channels: Channels list
        """

        numbers = list([0])

        for element in channels:
            if element[0:len(name) + 1] == name + "-":
                try:
                    numbers.append(int(element[len(name) + 1:]))
                except:
                    pass

        numbers.sort()

        return name + "-" + str(int(numbers[-1]) + 1)
    

    async def on_ready(self):
        """
        This function report to logger when bot connect to discord.
        """
        
        self.logger.info("Ready to ticketing!")


    async def on_message(self, message):
        """
        This function is using to receiving and process messages from user.
        :message: Message container from user
        """

        if message.author == self.user:
            return

        command = self.config.get("command")
        
        if message.content[0:len(command)] == command:
            await self.create_new_ticket(
                message.channel, 
                message.guild, 
                message.author
            )


    async def create_new_ticket(self, channel, guild, author):
        """
        This function create new ticket in given channel from given guild and
        add to it person given as author.
        :channel: Channel to send info about
        :guild: Guild to create channel in
        :author: Author for add to created channel
        """

        channel_name = self.get_new_channel_name(
            self.config.get("channelname"), 
            [channel.name for channel in guild.text_channels]
        )

        support = discord.utils.get(
            guild.roles, 
            name = self.config.get("supportrole")
        )

        disable_read = discord.PermissionOverwrite(read_messages = False)
        enable_read = discord.PermissionOverwrite(read_messages = True)

        overwrites = {
            guild.default_role: disable_read,
            author: enable_read
        }

        if support is not None: 
            overwrites[support] = enable_read

        await guild.create_text_channel(channel_name, overwrites = overwrites)
        await channel.send(self.config.get("successfull") + channel_name)

        self.logger.info("Successfull create " + channel_name + " channel!")


    def run(self):
        """
        This function run bot from token given in config file.
        """

        token = self.config.get("discord-secret-token")
        super(ticketer_t, self).run(token)


