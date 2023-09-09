import time

import random

from pyrogram import Client, filters



CMD = ["/", "."]



@Client.on_message(filters.command("alive", CMD))

async def check_alive(_, message):

    await message.reply_text("Lᴜᴄᴋʟʏ I Aᴍ Aʟɪᴠᴇ :) Pʀᴇss 👉 /start \n\nPʀᴇss 👉 /help Fᴏʀ Hᴇʟᴩ ;)\n\n\nPʀᴇss 👉 /ping Tᴏ Cʜᴇᴄᴋ Mʏ Pɪɴɢ 😁")



@Client.on_message(filters.command("help", CMD))

async def help(_, message):

    await message.reply_text("Pʀᴇss 👉 /movies Fᴏʀ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Mᴏᴠɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\nPʀᴇss 👉 /series Fᴏʀ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Sᴇʀɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\n\nPʀᴇss 👉 /tutorial Fᴏʀ Tᴜᴛᴏʀɪᴀʟ Aʙᴏᴜᴛ Hᴏᴡ Tᴏ Gᴇᴛ Dɪʀᴇᴄᴛ Fɪʟᴇs Fʀᴏᴍ Mᴇ 🤗")



@Client.on_message(filters.command("credits", CMD))

async def help(_, message):

    await message.reply_text("Tʜɪs Is Cᴏᴅᴇᴅ Bʏ🧑‍💻 @Kishan484 \n\nTHANKS TO🛰️ VPS FOR DEPLOY LIVE🔴 \n\nTHES IS NOT A📡 Oᴩᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ Sᴏ 🎮Sᴜᴩᴩᴏʀᴛ\n\n 🌬️PRIVATE BOT IS BOT ONLY USE 🥷ADMIN")



@Client.on_message(filters.command("forward", CMD))

async def movie(_, message):

    await message.reply_text("🧌HOW TO START🔴 FORWARDING\n ADD THE 📌TARGET CHANNEL ID (-100ID) AND 🔄SHORTS CHANNEL COPY THE LAST MESSAGE LINK YA FORWARD ✅THE LAST MESSAGE ON BOT START FORWARDING🛰️\n\n THANK YOU ❤️")



@Client.on_message(filters.command("stats", CMD))

async def series(_, message):

    await message.reply_text("BOT STATUS 🔴 LIVE................\n\n SIGNAL 📡 RECEIVING FROM 🚀 VPS \n BOT 😮‍💨 SLEEPING 💤 TIME 30 S")



@Client.on_message(filters.command("broadcast", CMD))

async def tutorial(_, message):

    await message.reply_text("📡 BROADCAST FEATURE 🛰️ IS NOT ❌  ALLOWED BECAUSE THIS BOT 🧑‍💻 USE ONLY 👹ADMIN \n ♻️ ғʀᴇᴇ sᴛᴏʀᴀɢᴇ ... NO DATABASE 🗃️")



@Client.on_message(filters.command("ping", CMD))

async def ping(_, message):

    start_t = time.time()

    rm = await message.reply_text("...........")

    end_t = time.time()

    time_taken_s = (end_t - start_t) * 1000

    await rm.edit(f"Pɪɴɢ🔥!\n{time_taken_s:.3f} ms")
