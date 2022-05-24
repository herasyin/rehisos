# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import discord
from discord.ext import commands
from discord import utils
import random
import config
import time
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = '.', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('ready 4 say hui1111')

# JOIN/LEAVE
@client.event
async def on_member_join(member):
    channel = client.get_channel(859024516906614784)
    hi = ['как же без тебя было скучно!', 'хай.', 'добро пожаловать!', 'ты блядь еще кто?', 'я ждал тебя и вот ты здесь.', 'я ждал тебя и вот ты здесь.', 'ну и ава у тебя, это лечится вообще?', 'мне кажется, мы подружимся.']
    await channel.send(f'{member.mention} ' + random.choice(hi))

@client.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    bye = ['откис еблан.', 'съебался в ужасе.', 'ну и пиздуй!', 'вышел в окно.', 'прощай, я не буду скучать.', 'прощай, я буду скучать.']
    await channel.send(f'{member} ' + random.choice(bye))

# CHAT
@client.event
async def on_message(message):
	await client.process_commands(message)
	msg = message.content.lower()
	pid = [u'пидор', u'педик', u'педрилла', 'pidor', u'пидорас', u'пидарас']
	for i in msg.split():
		if i in pid:
			await message.channel.send(u'осуждаю пидора, который это спизданул!')
			break
	nig = ['nigger', u'нигер', u'нига', u'ниггер', u'негр', 'nigga', 'niga', 'niger']
	for i in msg.split():
		if i in nig:
			her1 = [u'В машине сидят негp и мексиканец. Кто за рулём? Коп.', u'Негp и мексиканец падают с небоскрёба. Кто упадёт первым? Какая разница?', u'Как узнать, что у негpа недавно был секс? Его глаза всё ещё красные от перцового балончика.', u'Как называется негp на велосипеде? Вор.', u'Почему, когда какие-либо приборы не работают - по ним бьют? С рабами это срабатывало.', u'Негp и мексиканец падают с дерева. Кто упадёт на землюпервым? Мексиканец. Негp не долетит - ему помешает верёвка.', u'Что общего между кроссовками Nice и Ку-Клукс-Кланом? Они заставляют негpов быстро бегать.', u'Как сделать так что бы негp перестал тонуть? Надо просто убрать ногу с его головы.', u'Почему негpы так плохо пахнут? Чтобы слепые их тоже могли ненавидеть.', u'Какие три самых сложных года в жизни негра? Первый класс.', u'Почему негp, когда едет в машине, закрывает все окна? Он думает, что воняет снаружи.', u'Как снять негра с дерева? Перерезать веревку.']
			await message.channel.send(random.choice(her1))
			break
	heras = [u'джек лох', u'джек гей', u'джек какашка', u'джек еблан', u'herasyin лох', u'herasyin гей', u'herasyin еблан']
	if msg in heras:
		her2 = [u'согласен!', u'соглы', u'я тоже так считаю.']
		await message.channel.send(random.choice(her2))
	rehis = ['rehisos', u'рехисос', 'rehisos,', u'рехисос,']
	for i in msg.split():
		if i in rehis:
			her3 = [u'не поминай имя бога в суе, долбоеб.', u'че?', 'отебись, я сплю <:fuckyou:742675532600049704>', 'да - это я <:rehisos:742685931722506330>']
			await message.channel.send(random.choice(her3))
			break
	mapp = [u'проанализируй эти рисунки и найди место']
	if msg in mapp:
		await message.channel.send('сам проанализируй, мудила')
		time.sleep(2)
		await message.channel.send('шутка')
		time.sleep(2)
		await message.channel.send('начинаю анализ, ожидайте...')
		time.sleep(5)
		await message.channel.send('готово')
		time.sleep(1)
		await message.channel.send('это место на побережье к северу от Палето')
		time.sleep(2)
		await message.channel.send('так же я проанализировал все данные из открытых источников, анальный рисунок убийцы и трусы твоей мамки, в результате чего удалось выявить предпологаемые места захоронения жертв')
		time.sleep(3)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/888415881607131196/unknown.png')
		time.sleep(3)
		await message.channel.send('меня больше не трогать, я заебался <:fuckyou:742675532600049704>')

	majestic1 = [u'есть дополнительные материалы по джоку?']
	if msg in majestic1:
		await message.channel.send('спрашиваешь?')
		time.sleep(2)
		await message.channel.send('у меня есть все кроме вонючего и гниющего тела!')
		time.sleep(2)
		await message.channel.send('на нахуй!')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/890530867368300575/GTA_5_Jock_Cranley_Campaign_Trailer.mp4')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/890536920818528277/GTA_5_Sue_Murry_Campaign_Trailer.mp4')

	majestic2 = [u'покажи сайт и вырезку из газеты по этому делу']
	if msg in majestic2:
		await message.channel.send('покажи то')
		time.sleep(1)
		await message.channel.send('покажи cе')
		time.sleep(1)
		await message.channel.send('я венец твоериния человечества')
		time.sleep(2)
		await message.channel.send('а ты лезешь со своей хуйней...')
		time.sleep(2)
		await message.channel.send('https://media.discordapp.net/attachments/871746192743211018/890931893648887838/unknown.png')
		time.sleep(1)
		await message.channel.send('вот сайт')
		time.sleep(2)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/890684047838298152/unknown_1.png')
		time.sleep(1)
		await message.channel.send('вот газета')

	majestic3 = [u'есть записка которую увидел франклин?']
	if msg in majestic3:
		await message.channel.send('есть ли в тебе скрытое желание сосать хуй?')
		time.sleep(2)
		await message.channel.send('конечно есть!')
		time.sleep(2)
		await message.channel.send('https://media.discordapp.net/attachments/871746192743211018/890931094193594378/unknown.png')
		time.sleep(2)
		await message.channel.send('не благодари, отсосешь потом')
		time.sleep(1)
		await message.channel.send('<a:yees:801342763790499840>')

	majestic4 = [u'покажи письмо из дела по киностудии ричарда маджестика']
	if msg in majestic4:
		await message.channel.send('а ты мне что?')
		time.sleep(2)
		await message.channel.send('начинают заебывать твои просьбы')
		time.sleep(2)
		await message.channel.send('реально')
		time.sleep(2)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/890684043539124295/unknown_2.png')

	majestic5 = [u'переведи плиззз']
	if msg in majestic5:
		await message.channel.send('realy?')
		time.sleep(2)
		await message.channel.send('REALY???')
		time.sleep(2)
		await message.channel.send('dump motherfucker')
		time.sleep(2)
		await message.channel.send('Вайндвуд 14 августа 1949 год')
		time.sleep(2)
		await message.channel.send('Дорогой Дэвид, думаю ты уже знаешь, что я совершил несколько ошибок. Все мы совершили. Мы не совершенны. А я тот кто особенно сфокусировался на совершенстве, не совершенен больше остальных.')
		time.sleep(1)
		await message.channel.send('Я знаю, что ты знаешь всю эту историю или по крайней мере достаточную её часть. Я знаю что тебя тошнит от меня, но позволь задать вопрос. Разве у меня был выбор? Поиметь шлюху? Шлюху недостойную 3-х баксов сидящую за своей письменной машинкой и угрожающей мне? Это был лучший вариант из всех. Единственный возможный. Да я понимаю что это было отвратительный выбор, но это уже вопрос греха. Грех рождает грех. И мои грехи преумножились.')
		time.sleep(1)
		await message.channel.send('Я знаю о твоей осведомленности в деле с Айзеком. Чтож, это было пару лет назад и все приходило в норму. Никто не знал об этом. Только ты, я, адвокаты, Эйб Шварцман из Гранд Каньена. Все у кого есть свой алигорический скелет в шкафу. Айзек предал меня, возможно наихудшим образом, не из-за того дела с Морен. Правда в том что когда я познакомился с ней, она трахалась за хотдоги, чего мне было ожидать? Нет, Айзек предал меня самым дерьмовым способом, он не выложился полностью в фильме Закапать пса. Я предупреждал его, хотя знал, что он уже любезничал (флиртовал) с Эйбом. Он даже снял короткометражку для него. На моей кинопленке... Я выпил в тот день, а потом это случилось. Мы все сделали. Я похоронил его в шахте в горах. Потом позвонил Эйбу и предложил ему забыть об Айзеке. Эйб и сам совершил несколько ошибок включая тот дурдом с мойщиком посуды. Так что он заткнулся насколько я знаю.')
		await message.channel.send('Я надеюсь ты понимаешь насколько я ценю нашу дружбу и верю, что ничто не заставило бы тебя распускать обо мне дурные слухи. Дай мне побыть честным хотя бы на секунду. Я готов принимать сложные решения вновь и вновь для подтверждения, что для меня это важные отношения с тобой я бы хотел помочь тебе. Фредс купит у тебя 5% Ричард Маджестик за 450 тысяч кусков. Мы оба знаем, что это гораздо выше рыночной цены и это связывает нас вместе как братьев, коими мы и являемся. Ты талантливый человек, который должен заниматся тем, что у него получается лучше всего. Поменьше всей этой артистичной чепухи. Действие, только действие! Когда люди думают о Ричард Маджестик, они думают о шлюхах, районах и томиганах. Дай им то что они хотят. Мы претворяем мечты в жизнь. Это невероятная ответственность.')
		time.sleep(1)
		await message.channel.send('Твой друг Фред Квинси.')

	majestic6 = [u'есть что по фреду из записки?']
	if msg in majestic6:
		await message.channel.send('а вот тут странный момент...')
		time.sleep(2)
		await message.channel.send('кроме того что он владеет мультипликационной студией Freds')
		time.sleep(1)
		await message.channel.send('вообще ничего')
		time.sleep(2)
		await message.channel.send('будто за ним кто-то подчистил')
		time.sleep(2)
		await message.channel.send('но я нашел 4 случая вандализма сделанные одним подчерком')
		time.sleep(2)
		await message.channel.send('там явно упоминается фред связанный с киностудией')
		time.sleep(2)
		await message.channel.send('я отметил точки на карте')
		time.sleep(2)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/890923855999299594/map.png')
		time.sleep(2)
		await message.channel.send('приключение начинается прямо сейчас')
		time.sleep(2)
		await message.channel.send('ВПЕРЕД АНГЕЛЫ!')

	majestic7 = [u'в заброшенной шахте у скупщика рыбы трупы случайно не находили?']
	if msg in majestic7:
		await message.channel.send('случайно находили')
		time.sleep(2)
		await message.channel.send('был там один жмурик')
		time.sleep(1)
		await message.channel.send('ща высру его фотки')
		time.sleep(4)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/890686862396637194/Grand_Theft_Auto_V_Screenshot_2021.09.23_-_18.25.15.58.png')
		time.sleep(2)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/890686865731117056/Grand_Theft_Auto_V_Screenshot_2021.09.23_-_18.25.30.59.png')
		time.sleep(2)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/890686866943279184/Grand_Theft_Auto_V_Screenshot_2021.09.23_-_18.25.40.70.png')

	majestic8 = [u'че за хуйня у его ног?']
	if msg in majestic8:
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/890686871305326623/Grand_Theft_Auto_V_Screenshot_2021.09.23_-_18.28.01.77.png')
		time.sleep(2)
		await message.channel.send('эта?')

	majestic9 = [u'сделай что-бы видно было']
	if msg in majestic9:
		await message.channel.send('да ты заебешь')
		time.sleep(2)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/890686868683911229/Grand_Theft_Auto_V_Screenshot_2021.09.23_-_18.28.01.2.png')
		time.sleep(2)
		await message.channel.send('на')

	majestic9 = [u'спорим ты не найдешь труп секретаря которого они захуярили?']
	if msg in majestic9:
		await message.channel.send('ну ты сука и мразь...')
		time.sleep(2)
		await message.channel.send('Я')
		time.sleep(2)
		await message.channel.send('БЛЯТЬ')
		time.sleep(2)
		await message.channel.send('ПРАКТИЧЕСКИ БОГ!')
		time.sleep(4)
		await message.channel.send('нашел труп')
		time.sleep(2)
		await message.channel.send('пиздуйте за аквалангом')
		time.sleep(2)
		await message.channel.send('https://media.discordapp.net/attachments/871726192743211018/890963455606157322/Screenshot_3.png')
		time.sleep(2)
		await message.channel.send('он тут')
	masquarade1 = [u'ttjwl']
	if msg in masquarade1:
		await message.channel.send('**FOOD MARKET** на Sinner Street в Textile City')
		time.sleep(2)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928076723545841725/Grand_Theft_Auto_V_Screenshot_2022.01.04_-_23.19.52.75.png')
		time.sleep(2)
		await message.channel.send('к слову маркет закрыт после *кровавого четверга*')
		time.sleep(2)
		await message.channel.send('че за четверг я не ебу')
		time.sleep(4)
		await message.channel.send('в базах данных походу все подчистили')
		time.sleep(2)
		await message.channel.send('остались только заголовки в реесте под названием «кровавый четверг в фуд маркете»')
		time.sleep(2)
		await message.channel.send('если хочешь рассмотреть эту криповую вывеску получше, напиши свой рот наоборот')
		time.sleep(2)
		await message.channel.send('ой, то есть код, ну этот ttjwl')
	masquarade1dop = [u'lwjtt']
	if msg in masquarade1dop:
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928096344818737192/Grand_Theft_Auto_V_Screenshot_2022.01.05_-_03.54.16.72.png')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928096342612537354/Grand_Theft_Auto_V_Screenshot_2022.01.05_-_03.46.33.72.png')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928096342859984907/Grand_Theft_Auto_V_Screenshot_2022.01.05_-_03.48.28.27.png')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928096343459762236/Grand_Theft_Auto_V_Screenshot_2022.01.05_-_03.49.46.01.png')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928096343648534568/Grand_Theft_Auto_V_Screenshot_2022.01.05_-_03.50.25.84.png')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928096344147624066/Grand_Theft_Auto_V_Screenshot_2022.01.05_-_03.52.29.46.png')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928096344437035089/Grand_Theft_Auto_V_Screenshot_2022.01.05_-_03.53.19.75.png')
		time.sleep(2)
		await message.channel.send('у меня все!')
	masquarade2 = [u'i124q']
	if msg in masquarade2:
		await message.channel.send('**Homme Gina** на Eastbourne Way в Rockford Hills')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928076723990458428/Grand_Theft_Auto_V_Screenshot_2022.01.04_-_23.44.26.40.png')
		time.sleep(1)
		await message.channel.send('есть приколян про этот бренд, но сперва давай проверим твои познания в...')
		time.sleep(2)
		await message.channel.send('...биологии, да биологии!')
		time.sleep(2)
		await message.channel.send('посмотри на постер и покажи пальчиком где у дяди пися <:cur:913398850214055966>')
		time.sleep(4)
		await message.channel.send('я серьезно, тыкни пальцем прямо в монитор в то место где у него хуй, я жду!')
		time.sleep(6)
		await message.channel.send('умница! <:vsrat:743399038337941527> ')
		time.sleep(1)
		await message.channel.send('это реклама магазина мужской и женской одежды, забавно, что слово Homme в названии можно перевести с французского, как мужчина, тогда новый вариант названия Man Gina очень созвучен с гомосексуальным термином *manjina*, который обозначает мужские половые органы. хуйня прикол, я знаю.')
	masquarade3 = [u'dntfwm']
	if msg in masquarade3:
		await message.channel.send('**Anna Rex** на Eastbourne Way в Rockford Hills')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928076724342763540/Grand_Theft_Auto_V_Screenshot_2022.01.04_-_23.49.23.10.png')
		time.sleep(1)
		await message.channel.send('на втором этаже похоже вечеринка, хотя магазин закрыт')
		time.sleep(2)
		await message.channel.send('когда к окну кто-то подходит, напоминает окно из района красных фонарей в амстердаме')
		time.sleep(2)
		await message.channel.send('было бы у меня тело, я бы туда заглянул <:vsrat:743399038337941527>')
	masquarade4 = [u'shwmtm']
	if msg in masquarade4:
		await message.channel.send('Рекламный плакат **Anna Rex**')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928728107106598932/Grand_Theft_Auto_V_Screenshot_2022.01.06_-_02.17.15.49.png')
		time.sleep(1)
		await message.channel.send('анарексичная марионетка')
		time.sleep(2)
		await message.channel.send('маркетолог долбоеб')
		time.sleep(2)
		await message.channel.send('или нет?')
	masquarade5 = [u'kmpiwtd']
	if msg in masquarade5:
		await message.channel.send('**Val-de-Grâce** на Portola Drive в Rockford Hills')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928076725433286666/Grand_Theft_Auto_V_Screenshot_2022.01.05_-_00.31.31.25.png')
		time.sleep(1)
		await message.channel.send('без комментариев')
	masquarade5 = [u'lvlkyad']
	if msg in masquarade5:
		await message.channel.send('Рекламный плакат телешоу **Implant Outsource**')
		time.sleep(1)
		await message.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/928076725118726164/Grand_Theft_Auto_V_Screenshot_2022.01.04_-_23.56.01.26.png')
		time.sleep(1)
		await message.channel.send('сиськи из Индонезии, жопа из Сомали, знучит не так плохо')


# COMMANDS
@client.command()

async def help(ctx, amount = 1):
	await ctx.channel.purge(limit = amount)
	author = ctx.message.author
	await ctx.send(f'{author.mention} никто тебе не поможет!')
	print (author)

@client.command()
@commands.has_permissions(administrator = True)

async def clear(ctx, amount : int):
	await ctx.channel.purge(limit = amount + 1)

@client.command()

async def fibsearchmerleabrahams(ctx, amount = 1):
	emb = discord.Embed(colour = discord.Colour.from_rgb(233, 0, 38))
	author = ctx.message.author
	emb.set_author(name = '[FIB | FPB | №1419 | Jack Heras]', icon_url = ctx.author.avatar_url)
	emb.set_thumbnail(url = 'https://media.discordapp.net/attachments/871746192743211018/888067721466626058/NHAcV09.png')
	emb.add_field(name = 'MERLE ABRAHAMS', value='file#00083041', inline=False)
	emb.add_field(name = 'GENDER', value='male', inline=True)
	emb.add_field(name = 'HIGHT', value='5′ 8″', inline=True)
	emb.add_field(name = 'WEIGHT', value='148 lb', inline=True)
	emb.add_field(name = 'РАССЛЕДОВАНИЕ', value='Дело «Бесконечных убийств» с самого начала было сраным тупиком. Из рассказов местных, мы знали кто убийца, но кроме косвенных улик ничего не было. 48 часовой допрос подозреваемого ничего не дал и мы были вынуждены его отпустить. Во время слежки он подошёл к нашей машине и назвал мать агента Томаса «жирной пиздой», поэтому агент Томас нашел у него в заднем кармане 100 грамм отборного кокса и засадили уебка в федеральную тюрьму. Тела жертв так и небыли найдены.', inline=False)
	emb.add_field(name = 'АРЕСТ', value='Во время задержания трижды испражнился в патрульной машине, вонь стояла, просто пиздец. Постоянно говорил, что оставил в своей машине монеты для проезда и просил отвезти к месту где огонь извергнулся в бесконечность, что бы забрать их. Зарегистрированных т/с на его имя в базе не было.', inline=False)
	emb.add_field(name = 'СМЕРТЬ', value='Merle Abrahams скончался в федеральной тюрьме в декабре 2004, точное время и обстоятельства смери не известны.', inline=False)
	emb.set_image(url = 'https://cdn.discordapp.com/attachments/871746192743211018/888153234353586196/Grand_Theft_Auto_V_Screenshot_2021.09.16_-_20.37.16.12.png')
	emb.set_footer(text = 'FEDERAL INVESTIGATION BUREAU DATABASE')
	await ctx.channel.send('произвожу поиск по имени Merle Abrahams в базе данных')
	await ctx.channel.send('<a:loading:888451642645708800>')
	time.sleep(8)
	await ctx.channel.purge(limit = amount)
	await ctx.send(embed = emb)

@client.command()

async def federalprisonrequestvandalism(ctx, amount = 1):
	author = ctx.message.author
	await ctx.channel.send('запрашиваю в архивах SASPA информацию о случаях вандализма на территории федералной тюрьмы')
	await ctx.channel.send('<a:loading:888451642645708800>')
	time.sleep(13)
	await ctx.channel.purge(limit = amount)
	await ctx.channel.send('вообще-то заключенных пиздят за разрисовывание стен, но один случай в базе все-таки нашелся')
	time.sleep(3)
	await ctx.channel.send('https://cdn.discordapp.com/attachments/871746192743211018/888411812612157471/54860_GwU8305wrh_mh6r90.png')
	await ctx.channel.send('вот фото')

@client.command()

async def fibserachjockcranley(ctx, amount = 1):
	emb = discord.Embed(colour = discord.Colour.from_rgb(233, 0, 38))
	author = ctx.message.author
	emb.set_author(name = '[FIB | FPB | №1419 | Jack Heras]', icon_url = ctx.author.avatar_url)
	emb.set_thumbnail(url = 'https://media.discordapp.net/attachments/871746192743211018/890943607425605682/unknown.png')
	emb.add_field(name = 'JOCK CRANLEY', value='file#00213271', inline=False)
	emb.add_field(name = 'GENDER', value='male', inline=True)
	emb.add_field(name = 'HIGHT', value='5′ 9″', inline=True)
	emb.add_field(name = 'WEIGHT', value='149 lb', inline=True)
	emb.add_field(name = 'БИОГРАФИЯ', value='Претендент на звание губернатора штата, участвующий в предвыборной компании против Сью Маррей. У него есть рекламные ролики на телевидении, и на веб-сайте Jockcranley.com. Он обещает устранить налоги, продавая ненужные парковки и сократить бюджет на образование на 98%. Помимо этого является консерватором, а также теле- и кинозвездой.', inline=False)
	emb.add_field(name = 'ДОПОЛНИТЕЛЬНО', value='В городе Vice City на радиостанции Wave 103 рассказывал о том, что организация DEA "спасла меня от моего злейшего врага — меня самого". Имеется ввиду наркотическая зависимость Джока в тот период', inline=False)
	emb.set_footer(text = 'FEDERAL INVESTIGATION BUREAU DATABASE')
	await ctx.channel.send('произвожу поиск по имени Jock Cranley в базе данных')
	await ctx.channel.send('<a:loading:888451642645708800>')
	time.sleep(8)
	await ctx.channel.purge(limit = amount)
	await ctx.send(embed = emb)

@client.command()

async def fibserachleonorajohnson(ctx, amount = 1):
	emb = discord.Embed(colour = discord.Colour.from_rgb(233, 0, 38))
	author = ctx.message.author
	emb.set_author(name = '[FIB | FPB | №1419 | Jack Heras]', icon_url = ctx.author.avatar_url)
	emb.set_thumbnail(url = 'https://media.discordapp.net/attachments/871746192743211018/890926978369224764/unknown.png')
	emb.add_field(name = 'LEONORA JOHNSON', value='file#00001666', inline=False)
	emb.add_field(name = 'GENDER', value='female', inline=True)
	emb.add_field(name = 'HIGHT', value='5′ 1″', inline=True)
	emb.add_field(name = 'WEIGHT', value='135 lb', inline=True)
	emb.add_field(name = 'БИОГРАФИЯ', value='Леонора родилась 1952 году, в бедной семье. Позже для осуществления своей мечты стать актрисой, моделью или певицей поехала в Лос-Сантос. Позже начала сниматься в фильмах Соломона Ричардса и завела роман с Питером Дрейфусом. Но по неизвестной причине была убита Дрейфусом. Сам Питер был убит неким Франклином Клинтоном, после того как последний нашел письмо в котором Дрейфус признается в убийстве.', inline=False)
	emb.add_field(name = 'СМЕРТЬ', value='Питер Дрейфус отрезал ей стопы и кисти, разложил их по противоположным сторонам. Отрезал ей часть лица до неузнаваемости, отрезал ей часть бедра и написал «Ветчина».', inline=False)
	emb.set_image(url = 'https://media.discordapp.net/attachments/871746192743211018/890934242308145182/photodeath.png')
	emb.set_footer(text = 'FEDERAL INVESTIGATION BUREAU DATABASE')
	await ctx.channel.send('произвожу поиск по имени Leonora Johnson в базе данных')
	await ctx.channel.send('<a:loading:888451642645708800>')
	time.sleep(8)
	await ctx.channel.purge(limit = amount)
	await ctx.send(embed = emb)

# ERROR
@client.event
async def on_command_error(ctx, error):
	pass

@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.name}, сколько удалять то?')

	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.name}, хуя разогнался, не указывай мне что делать!')

#ROLE
@client.event
async def on_raw_reaction_add(payload):
	if payload.message_id == config.POST_ID:
		channel = client.get_channel(payload.channel_id) # получаем объект канала
		message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
		member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию

		try:
			emoji = str(payload.emoji) # эмоджик который выбрал юзер
			role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выбранной роли (если есть)
			if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
				await member.add_roles(role)
				print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
			else:
				await message.remove_reaction(payload.emoji, member)
				print('[ERROR] Too many roles for user {0.display_name}'.format(member))

		except KeyError as e:
			print('[ERROR] KeyError, no role found for ' + emoji)
		except Exception as e:
			print(repr(e))
			
@client.event 
async def on_raw_reaction_remove(payload):
	channel = client.get_channel(payload.channel_id) # получаем объект канала
	message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
	member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию

	try:
		emoji = str(payload.emoji) # эмоджик который выбрал юзер
		role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выбранной роли (если есть)

		await member.remove_roles(role)
		print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

	except KeyError as e:
		print('[ERROR] KeyError, no role found for ' + emoji)
	except Exception as e:
		print(repr(e))

client.run(config.TOKEN)