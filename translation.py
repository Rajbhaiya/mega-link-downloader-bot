import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

class Translation(object):
    START_TEXT = f"""<b>Hello there,</b>
    
I am a <b>Mega Link Downloader</b> bot!

Just enter your mega.nz link and I will return the file/video to you!😇

💠 I can set custom captions and custom thumbnails too!

💠 I can download links which are bigger than 2GB too! 😍

Press /help for more details!"""
    
    DOWNLOAD_START = "<b>Downloading to my server now 📥</b> \n\n<code>Please wait uploading will start as soon as possible😇...</code>"
    UPLOAD_START = "Uploading to Telegram now 📤..."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS =  "Downloaded in <b>{}</b> seconds.\n\nUploaded in <b>{}</b> seconds.\n\n<b>Thanks For Using This Free Service</b>"
    SAVED_CUSTOM_THUMB_NAIL = "𝗖𝘂𝘀𝘁𝗼𝗺 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗜𝘀 𝗦𝗮𝘃𝗲𝗱. 𝗧𝗵𝗶𝘀 𝗜𝗺𝗮𝗴𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗨𝘀𝗲𝗱 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗡𝗲𝘅𝘁 𝗨𝗽𝗹𝗼𝗮𝗱𝘀 📁.\n\nIf you want to delete it send\n /deletethumbnail anytime!"
    DEL_ETED_CUSTOM_THUMB_NAIL = "𝗖𝘂𝘀𝘁𝗼𝗺 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗖𝗹𝗲𝗮𝗿𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ❌.\nYou will now get an auto generated thumbnail for your video uploads!"

    HELP_USER = f"""<b><u>🍁Hi I am a Mega Link Downloader Bot.. 🍁</u></b>
 
<u>How to use me:-</u>

<b>Just Send me a mega.nz file link!</b>

<b>Important:-</b> 

- Folder links are not supported.

- Your link should be valid(not expired or been removed) and should not be password protected or encrypted or private!

❇️ <b>If you want a custom thumbnail for your uploads send a photo before sending the mega link!

press /deletethumbnail if you want to delete saved thumbnail.


<b>Note</b> :- You can download links which are bigger than 2GB from me too! i will split files which are bigger thna 2GB"""
