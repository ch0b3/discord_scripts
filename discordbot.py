import discord

TOKEN = 'NzU0NTg5NzUyNzk5Mzk1ODUx.X128eA.Kdf7vIXUTwABJ9-o8UDHusgeh1E'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# コマンドに対応するリストデータを取得する関数を定義
def get_data(message):
    command = message.content
    data_table = {
        '/members': message.guild.members, # メンバーのリスト
        '/roles': message.guild.roles, # 役職のリスト
        '/text_channels': message.guild.text_channels, # テキストチャンネルのリスト
        '/voice_channels': message.guild.voice_channels, # ボイスチャンネルのリスト
        '/category_channels': message.guild.categories, # カテゴリチャンネルのリスト
    }
    return data_table.get(command, '無効なコマンドです')

# コマンドを読み取るハンドラ
@client.event
async def on_message(message):
	# メッセージ送信者がBotだった場合は無視する
	if message.author.bot:
		return
	data_list = get_data(message)
	# ログ出力
	print(data_list)
	for data in data_list:
		msg = f'id: {data.id}\nname: {data.name}'
		await message.channel.send(msg)

# リアクションを通知する
@client.event
async def on_raw_reaction_add(payload):
	channel = client.get_channel(payload.channel_id)
	message = await channel.fetch_message(payload.message_id)
	msg = f'{payload.member.name}さんがリアクションしました: {payload.emoji.name}\n{message.jump_url}'
	await channel.send(msg)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
