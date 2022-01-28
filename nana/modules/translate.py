from googletrans import Translator

from nana import app, Command
from pyrogram import Filters

trl = Translator()

__MODULE__ = "Translate"

# TODO: Setlang for translation

@app.on_message(Filters.user("self") & Filters.command(["tr"], Command))
async def translate(client, message):
	if message.reply_to_message and (message.reply_to_message.text or message.reply_to_message.caption):
		if len(message.text.split()) == 1:
			await message.edit("Usage: Reply to a message, then `tr <lang>`")
			return
		target = message.text.split()[1]
		text = message.reply_to_message.text or message.reply_to_message.caption
	else:
		if len(message.text.split()) <= 2:
			await message.edit("Usage: `tr <lang> <text>`")
			return
		target = message.text.split(None, 2)[1]
		text = message.text.split(None, 2)[2]

	detectlang = trl.detect(text)
	try:
		tekstr = trl.translate(text, dest=target)
	except ValueError as err:
		await message.edit("Error: `{}`".format(str(err)))
		return
	await message.edit("Translated from `{}` to `{}`:\n```{}```".format(detectlang.lang, target, tekstr.text))

