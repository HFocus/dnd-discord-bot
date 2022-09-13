'''
Copyright (C) 2022 Keenan Buckley

This file is part of {PROJECT_NAME}.

{PROJECT_NAME} is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import discord
from discord.ext import commands


class Loot(commands.Cog):
    loot = discord.SlashCommandGroup("loot", "loot gathering and distribution")

    def __init__(self, bot : discord.Bot):
        self.bot = bot

    @loot.command(description="Splits a pile of coins into equal parts")
    async def split(self, ctx, parts: int, pp: int, gp: int, ep: int, sp: int, cp: int):
        """Splits a pile of coins into equal parts"""
        response = f'Splitting {pp} pp, {gp} gp, {ep} ep, {sp} sp, {cp} cp into {parts} parts, we get:\n'
        response += f'{int(pp/parts)} pp with {pp % parts} pp left over\n'
        response += f'{int(gp/parts)} gp with {gp % parts} gp left over\n'
        response += f'{int(ep/parts)} ep with {ep % parts} ep left over\n'
        response += f'{int(sp/parts)} sp with {sp % parts} sp left over\n'
        response += f'{int(cp/parts)} cp with {cp % parts} cp left over\n'
        await ctx.respond(response)


def setup(bot):
    bot.add_cog(Loot(bot))

def teardown(bot):
    bot.remove_cog('Loot')
