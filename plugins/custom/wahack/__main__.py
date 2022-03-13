# by Alone

import asyncio

from userge import userge


@userge.on_cmd("wahack$", about={'header': "Hack Whatsapp of victim"})
async def wahack_func(message):
    user = await message.client.get_user_dict(message.from_user.id)
    heckerman = user['mention']
    animation_chars = [
        "```Connecting To Target Device \\```",
        "```Connecting To Target Device |```",
        "```Connecting To Target Device /```",
        "```Connecting To Target Device \\```",
        "```Connection Established ```",
        "```Target Selected```",
        "```Looking for msgstore.db.crypt12```",
        "```msgstore.db.crypt12 was found at sdcard/WhatsApp/Databases```",
        "```Uploading To Server... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Uploading To Server... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Uploading To Server... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Uploading To Server... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Uploading To Server... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒```",
        "```Uploading To Server... 52%\n█████████████▒▒▒▒▒▒▒▒▒```",
        "```Uploading To Server... 70%\n█████████████████▒▒▒▒▒```",
        "```Uploading To Server... 88%\n█████████████████████▒```",
        "```Uploaded To Server... 100%\n███████████████████████```",
        "```Decrypting Data... 1%\n▒██████████████████████```",
        "```Decrypting Data... 14%\n████▒██████████████████```",
        "```Decrypting Data... 30%\n████████▒██████████████```",
        "```Decrypting Data... 55%\n████████████▒██████████```",
        "```Decrypting Data... 72%\n████████████████▒██████```",
        "```Decrypting Data... 88%\n████████████████████▒██```",
        "```Decrypted Data... 100%\n███████████████████████```",
        "**Target's WhatsApp Database Was Successfully Copied And Decrypted :**Database Stored "
        "at `downloads/victim/WhatsApp-Chat.data.sql`",
    ]
    hecked = (f"**Your WhatsApp Account Is Hacked**\n\n```Pay 10000₹ To``` {heckerman}``` "
              "To Delete This Database```")
    max_ani = len(animation_chars)
    for i in range(max_ani):
        await asyncio.sleep(1)
        await message.edit(animation_chars[i % max_ani])
    await message.edit(hecked)
