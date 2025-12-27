import os
import random
import asyncio
from telethon import TelegramClient, errors
from datetime import datetime

# --- YOUR VARIABLES ---
API_ID = xd      
API_HASH = ''  
PHONE = ''
VIDEO_DIR = '/home/esef/Documents/messenger/messengaer/video_list'
TARGETS = [""] #usernames and phone numbers can be put here

async def main():
    async with TelegramClient('session_esef', API_ID, API_HASH) as client:
        await client.start(phone=PHONE)
        print("system running, checks time each minute and sends when the time is right")

        while True:
            now = datetime.now()
            
            #  at what hour and at what minute
            if now.hour == 8 and now.minute == 0:
                print(f"sending a video")
                
                videos = [f for f in os.listdir(VIDEO_DIR) if f.lower().endswith('.mp4')]
                if videos:
                    for target in TARGETS:
                        video_path = os.path.join(VIDEO_DIR, random.choice(videos))
                        await client.send_file(target, video_path, caption="Good morning! ☀️")
                        print(f"sent to {target}")
                
                # Wait 61 seconds so it doesn't send 10 times in the same minute
                await asyncio.sleep(61)
            
            # Wait 30 seconds before checking the time again
            await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(main())