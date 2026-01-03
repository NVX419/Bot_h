# 11. Warn - تحذير عضو
@tree.command(name="warn", description="تحذير عضو")
@app_commands.describe(user="العضو", reason="سبب التحذير")
async def warn(interaction: discord.Interaction, user: discord.Member, reason: str = "لا سبب"):
    if interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message(f"تم تحذير {user.mention} بسبب: {reason}")
    else:
        await interaction.response.send_message("ليس لديك صلاحية!")

# 12. Poll - استطلاع رأي
@tree.command(name="poll", description="إنشاء استطلاع رأي")
@app_commands.describe(question="السؤال")
async def poll(interaction: discord.Interaction, question: str):
    embed = discord.Embed(title="استطلاع رأي", description=question)
    message = await interaction.response.send_message(embed=embed)
    await message.add_reaction("👍")
    await message.add_reaction("👎")

# 13. Remind - تذكير
@tree.command(name="remind", description="تذكير بعد وقت معين")
@app_commands.describe(time="الوقت بالدقائق", message="الرسالة")
async def remind(interaction: discord.Interaction, time: int, message: str):
    await interaction.response.send_message(f"سأذكرك بعد {time} دقيقة.")
    await asyncio.sleep(time * 60)
    await interaction.followup.send(f"تذكير: {message}")

# 14. Quote - اقتباس رسالة
@tree.command(name="quote", description="اقتباس رسالة")
@app_commands.describe(message_id="معرف الرسالة")
async def quote(interaction: discord.Interaction, message_id: str):
    try:
        msg = await interaction.channel.fetch_message(int(message_id))
        await interaction.response.send_message(f"> {msg.content}\n- {msg.author.mention}")
    except:
        await interaction.response.send_message("رسالة غير موجودة!")

# 15. Joke - نكتة
@tree.command(name="joke", description="نكتة عشوائية")
async def joke(interaction: discord.Interaction):
    jokes = ["لماذا الدجاجة عبرت الطريق؟ لتصل إلى الجانب الآخر!", "نكتة أخرى هنا."]
    await interaction.response.send_message(random.choice(jokes))

# 16. Meme - ميم
@tree.command(name="meme", description="ميم عشوائي")
async def meme(interaction: discord.Interaction):
    # يمكن ربط API مثل Reddit
    await interaction.response.send_message("ميم: [صورة ميم] (أضف API للصور)")

# 17. Dice - رمي نرد
@tree.command(name="dice", description="رمي نرد")
async def dice(interaction: discord.Interaction):
    result = random.randint(1, 6)
    await interaction.response.send_message(f"النتيجة: {result}")

# 18. Coinflip - رمي عملة
@tree.command(name="coinflip", description="رمي عملة")
async def coinflip(interaction: discord.Interaction):
    result = random.choice(["رأس", "ذيل"])
    await interaction.response.send_message(f"النتيجة: {result}")

# 19. User_info - معلومات عن عضو
@tree.command(name="user_info", description="معلومات عن عضو")
@app_commands.describe(user="العضو")
async def user_info(interaction: discord.Interaction, user: discord.Member = None):
    user = user or interaction.user
    embed = discord.Embed(title=f"معلومات عن {user.name}", description=f"انضم في: {user.joined_at}")
    await interaction.response.send_message(embed=embed)

# 20. Server_stats - إحصائيات الخادم
@tree.command(name="server_stats", description="إحصائيات الخادم")
async def server_stats(interaction: discord.Interaction):
    guild = interaction.guild
    embed = discord.Embed(title="إحصائيات الخادم", description=f"أعضاء: {guild.member_count}\nقنوات: {len(guild.channels)}")
    await interaction.response.send_message(embed=embed)

# 21. Avatar - عرض الصورة الرمزية
@tree.command(name="avatar", description="عرض الصورة الرمزية")
@app_commands.describe(user="العضو")
async def avatar(interaction: discord.Interaction, user: discord.Member = None):
    user = user or interaction.user
    await interaction.response.send_message(user.avatar.url if user.avatar else "لا توجد صورة")

# 22. Uptime - وقت التشغيل
@tree.command(name="uptime", description="وقت تشغيل البوت")
async def uptime(interaction: discord.Interaction):
    uptime = discord.utils.utcnow() - client.start_time
    await interaction.response.send_message(f"وقت التشغيل: {uptime}")

# 23. Translate - ترجمة
@tree.command(name="translate", description="ترجمة نص")
@app_commands.describe(text="النص", lang="اللغة (مثل 'ar' أو 'en')")
async def translate(interaction: discord.Interaction, text: str, lang: str):
    # يمكن ربط Google Translate API
    await interaction.response.send_message(f"ترجمة إلى {lang}: [ترجمة] (أضف API)")

# 24. Calc - حاسبة
@tree.command(name="calc", description="حساب بسيط")
@app_commands.describe(expression="التعبير (مثل 2+2)")
async def calc(interaction: discord.Interaction, expression: str):
    try:
        result = eval(expression)
        await interaction.response.send_message(f"النتيجة: {result}")
    except:
        await interaction.response.send_message("تعبير غير صحيح!")

# 25. Search - بحث
@tree.command(name="search", description="بحث عن موضوع")
@app_commands.describe(query="الاستعلام")
async def search(interaction: discord.Interaction, query: str):
    # يمكن ربط Google Search API
    await interaction.response.send_message(f"نتائج البحث عن '{query}': [روابط] (أضف API)")

# 26. Invite - دعوة البوت
@tree.command(name="invite", description="رابط دعوة البوت")
async def invite(interaction: discord.Interaction):
    await interaction.response.send_message("رابط الدعوة: [أضف رابط البوت]")

# 27. Feedback - ملاحظات
@tree.command(name="feedback", description="إرسال ملاحظات")
@app_commands.describe(message="الملاحظة")
async def feedback(interaction: discord.Interaction, message: str):
    # يمكن حفظها في قاعدة بيانات
    await interaction.response.send_message("شكراً لملاحظتك!")

# 28. Lock - قفل قناة
@tree.command(name="lock", description="قفل القناة")
async def lock(interaction: discord.Interaction):
    if interaction.user.guild_permissions.manage_channels:
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
        await interaction.response.send_message("تم قفل القناة.")
    else:
        await interaction.response.send_message("ليس لديك صلاحية!")

# 29. Unlock - فتح قناة
@tree.command(name="unlock", description="فتح القناة")
async def unlock(interaction: discord.Interaction):
    if interaction.user.guild_permissions.manage_channels:
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=True)
        await interaction.response.send_message("تم فتح القناة.")
    else:
        await interaction.response.send_message("ليس لديك صلاحية!")

# 30. Add_role - إضافة دور
@tree.command(name="add_role", description="إضافة دور لعضو")
@app_commands.describe(user="العضو", role="الدور")
async def add_role(interaction: discord.Interaction, user: discord.Member, role: discord.Role):
    if interaction.user.guild_permissions.manage_roles:
        await user.add_roles(role)
        await interaction.response.send_message(f"تم إضافة {role.name}.")
    else:
        await interaction.response.send_message("ليس لديك صلاحية!")

# 31. Remove_role - إزالة دور
@tree.command(name="remove_role", description="إزالة دور من عضو")
@app_commands.describe(user="العضو", role="الدور")
async def remove_role(interaction: discord.Interaction, user: discord.Member, role: discord.Role):
    if interaction.user.guild_permissions.manage_roles:
        await user.remove_roles(role)
        await interaction.response.send_message(f"تم إزالة {role.name}.")
    else:
        await interaction.response.send_message("ليس لديك صلاحية!")

# 32. Vote - تصويت
@tree.command(name="vote", description="تصويت على شيء")
@app_commands.describe(option="الخيار")
async def vote(interaction: discord.Interaction, option: str):
    await interaction.response.send_message(f"تم التصويت على: {option}")

# 33. Music - تشغيل موسيقى (بسيط)
@tree.command(name="music", description="تشغيل موسيقى")
@app_commands.describe(song="اسم الأغنية")
async def music(interaction: discord.Interaction, song: str):
    # يمكن ربط YouTube API أو Lavalink
    await interaction.response.send_message(f"تشغيل: {song} (أضف مكتبة للموسيقى)")

# 34. Random - رقم عشوائي
@tree.command(name="random", description="رقم عشوائي")
@app_commands.describe(min="الحد الأدنى", max="الحد الأقصى")
async def random_num(interaction: discord.Interaction, min: int = 1, max: int = 100):
    result = random.randint(min, max)
    await interaction.response.send_message(f"رقم عشوائي: {result}")

# 35. Time - الوقت الحالي
@tree.command(name="time", description="الوقت الحالي")
async def time_now(interaction: discord.Interaction):
    now = discord.utils.utcnow()
    await interaction.response.send_message(f"الوقت: {now}")

# 36. Emoji - إضافة إيموجي
@tree.command(name="emoji", description="إضافة إيموجي")
@app_commands.describe(emoji="الإيموجي")
async def emoji_add(interaction: discord.Interaction, emoji: str):
    await interaction.response.send_message(f"إيموجي: {emoji}")

# 37. Level - مستوى العضو (بسيط)
@tree.command(name="level", description="مستوى العضو")
@app_commands.describe(user="العضو")
async def level(interaction: discord.Interaction, user: discord.Member = None):
    user = user or interaction.user
    # يمكن ربط قاعدة بيانات للمستويات
    await interaction.response.send_message(f"مستوى {user.name}: 1 (أضف نظام مستويات)")

# 38. Report - تقرير
@tree.command(name="report", description="تقرير عن عضو")
@app_commands.describe(user="العضو", reason="السبب")
async def report(interaction: discord.Interaction, user: discord.Member, reason: str):
    # يمكن إرسال إلى قناة محددة
    await interaction.response.send_message(f"تم التقرير عن {user.mention}.")

# 39. Giveaway - سحب جوائز
@tree.command(name="giveaway", description="سحب جائزة")
@app_commands.describe(prize="الجائزة", time="الوقت بالدقائق")
async def giveaway(interaction: discord.Interaction, prize: str, time: int):
    await interaction.response.send_message(f"سحب {prize} بعد {time} دقيقة.")
    await asyncio.sleep(time * 60)
    # اختيار فائز عشوائي (أضف منطق)

# 40. Shutdown - إيقاف البوت (للمالك فقط)
@tree.command(name="shutdown", description="إيقاف البوت")
async def shutdown(interaction: discord.Interaction):
    if interaction.user.id == YOUR_USER_ID:  # استبدل بمعرفك
        await interaction.response.send_message("إيقاف البوت...")
        await client.close()
    else:
        await interaction.response.send_message("ليس لديك صلاحية!")
