import discord
import json

ALPHA_TESTER_ROLE = discord.Object(id='499492657974870027')

with open('token.json') as f:
    token = json.load(f)['token']

with open('members.json') as f:
    alpha_members = frozenset(json.load(f))


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_member_join(self, member):
        if member.id in alpha_members:
            member.add_roles(ALPHA_TESTER_ROLE)


client = MyClient()
client.run(token)
