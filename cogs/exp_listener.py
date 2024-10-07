from disnake.ext import commands
import asyncio
import os


ENABLED = True


class ExpListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_voice_activity = {}
        self.voice_xp_enabled = False

        # Add a task to the bot's event loop
        self.bot.loop.create_task(self.setup())

        print("ExpListener cog loaded")

    async def setup(self):
        """
        Wait until the bot is ready, then get all the voice channels in the
        active guild. For every member in the voice channel, add them to the
        user_voice_activity dictionary
        """
        await self.bot.wait_until_ready()

        guild_id = os.getenv("BOT_GUID_ID")
        if guild_id is None:
            print("BOT_GUID_ID is not set")
            return
        else:
            self.active_guild = self.bot.get_guild(int(guild_id))

        for channel in self.active_guild.voice_channels:
            # For every member in the voice channel
            for member_id in channel.voice_states:
                if not (
                    channel.voice_states[member_id].self_mute
                    or channel.voice_states[member_id].self_deaf
                ):
                    print(f"{member_id} is in {channel}")
                    self.user_voice_activity.setdefault(channel.id, set()).add(
                        member_id
                    )

    async def voice_xp(self):
        """
        Give XP to all users in voice channels every 5 minutes
        """
        self.voice_xp_enabled = True
        while self.voice_xp_enabled:
            # If set is empty, and finish loop
            if self.user_voice_activity == {}:
                print("Nobody is in a voice channel now")
                self.voice_xp_enabled = False
                continue
            else:
                # TODO: Give XP to all users in voice channels
                pass
            await asyncio.sleep(300)

    @commands.Cog.listener()
    async def on_message(self, ctx):
        """
        If a user sends a message, add XP to the user in the database
        """
        if ctx.author.id != self.bot.user.id:
            # TODO: Give XP to user
            pass

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        """
        If a user joins a voice channel and is not muted or deafened,
        add them to the user_voice_activity dictionary
        """
        if before.channel is not None:
            try:
                self.user_voice_activity[before.channel.id].discard(member.id)
                if self.user_voice_activity[before.channel.id] == set():
                    self.user_voice_activity.pop(before.channel.id)
            except Exception:
                pass

        if after.channel is not None:
            if after.self_mute or after.self_deaf or after.mute or after.deaf:
                return
            self.user_voice_activity.setdefault(after.channel.id, set()).add(member.id)
            if not self.voice_xp_enabled:
                await self.voice_xp()
            print(self.user_voice_activity)


def setup(bot):
    if ENABLED:
        bot.add_cog(ExpListener(bot))


def teardown(bot):
    bot.remove_cog("exp_listener")
    print("removing cog")
