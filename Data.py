from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I'm a **πΏππππππ.ππ-ππππππππ π­ππ**
I can upload media to telegra.ph and give you back the link with ease. Try sending multiple media, and it still won't stop me.
I can also be used in groups !!

To see `Supported Media Types` tap the related button below.
Use the other buttons to know more about me and my usage.

By @ImRishmika
    """

    # Help Message
    HELP = """
**READ BELOW TO KNOW HOW TO USE ME.**

See `Supported Media Types` by clicking that related button below.

**How to use me here?**
Just send the media and leave rest on me. 

**How to use in group?**
Add to me the group.
Then reply to a media with /telegraph to get the telegra.ph link.
You can alternatively also use "t" or "tg" as commands and "!" as prefix to do the same.
That is,
!t   ,   !tg   ,   !telegraph 
/t   ,   /tg   ,   /telegraph
[If you add in your group, your group users won't need to join our channel.]

__Note__ : If the bot doesn't respond in the expected way, make the bot admin so that bot gets updates for sure. Telegram is weird.

More features in development. Keep track by joining @ImDark_Empire.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @ImRishmika

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @ImRishmika

Support : @Emo_bot_Support
    """

    SUPPORTED_MEDIA_TYPES = """
β¨ **SUPPORTED MEDIA TYPES** β¨

1) Image
2) Sticker
3) Gifs or Animation
4) Video
5) Video Note
6) Document (Video/Photo/Gif)

Note : Telegraph has a size limit of 5 MB.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("β¨ Bot Status and More Bots β¨", url="https://t.me/Emo_bot_Support")],
        [InlineKeyboardButton("βΎοΈ Supported Media Types βΎοΈ", callback_data="supported_media_types"),InlineKeyboardButton("Dev", url="https://t.me/@ImRishmika")],
        [InlineKeyboardButton("Close π", callback_data="close")],
        [InlineKeyboardButton(text="ποΈ Return Home ποΈ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("β¨ Bot Status and More Bots β¨", url="https://t.me/Emo_bot_Support")
        ],
        [InlineKeyboardButton("βΎοΈ Supported Media Types βΎοΈ", callback_data="supported_media_types"),InlineKeyboardButton("Dev", url="https://t.me/ImRishmika")],
        [
            InlineKeyboardButton("How to Use β", callback_data="help"),
            InlineKeyboardButton("π₯ About π₯", callback_data="about")
        ],
        [InlineKeyboardButton("Close π", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("β¨ Bot Status and More Bots β¨", url="https://t.me/Emo_bot_Support"),InlineKeyboardButton("Dev", url="https://t.me/ImRishmika")],
        [InlineKeyboardButton("Close π", callback_data="close")],
        [InlineKeyboardButton(text="ποΈ Return Home ποΈ", callback_data="home")]
    ]
