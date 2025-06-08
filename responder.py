from telethon import TelegramClient, events

# Reemplaza con los datos reales que obtuviste en https://my.telegram.org
api_id = 28694061
api_hash = 'e5566a19f422c6ec909aba1f04db1829'

client = TelegramClient('userbot', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    # Lista de palabras o frases clave para identificar mensajes no deseados
    mensajes_indeseados = [
        'criptomoneda',
        'criptomonedas'
        'inversión',
        'ponzi',
        'hola',
        'expansion'
        'cómo estás',
        'como estas',
        'buenas',
        'saludos'
    ]

    mensaje_lower = event.raw_text.lower().strip()

    # Verifica si el mensaje completo coincide con algún mensaje corto sospechoso
    if mensaje_lower in ['hola', 'buenas', 'saludos', 'cómo estás', 'como estas']:
        await event.reply("Hola. No estoy disponible para conversaciones nuevas. Por favor, abstente de ofrecer inversiones o criptomonedas.")
        return

    # Verifica si contiene alguna palabra clave
    if any(palabra in mensaje_lower for palabra in mensajes_indeseados):
        await event.reply("Hola. No estoy interesado en ofertas relacionadas con inversiones o criptomonedas. Gracias.")
        return

async def main():
    print("Userbot activo...")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()