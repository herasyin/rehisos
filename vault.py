# storage of creepy ship and useful func 🝄
# сopyleft: ⌨ 2022 >>-her--> all rights not reserved

import os

HERA_ID = 726267858283266160
POST_ID = 802766660099768321
CHAT_ID = 859024516906614784
LOGS_ID = 963216065490481232

ROLES = {
	'<:eye:742677301157953559>': 741356737373667458 #observer
}

EXCROLES = ()
MAX_ROLES_PER_USER = 666

BOLD = '**'; SPOILER = '||'; CODE = '```'; UNDERLINE = '__'; STRIKE = '~~' # discord formating
ICON = [
	'<:vsrat:743399038337941527>',				#  0
	'<:rehisos:742685931722506330>',			#  1
	'<:cur:913398850214055966>',				#  2
	'<:fuckyou:742675532600049704>',			#  3
	'<:worker:791586102825582602>',				#  4
	'<:pressF:786230431561023529>',				#  5
	'<:tv1:742677301581447258>',				#  6
	'<:tea:847101198308999208>',				#  7
	'<:directory_fatal:974283553229639730>',	# -7
	'<:directory_error:974283553212878919>',	# -6
	'<:directory_warning:974283553170927636>',	# -5
	'<:directory_info:974283553275797515>',		# -4
	'<:directory_member:974276303308075038>',	# -3
	'<:directory_closed:847085141326299146>',	# -2
	'<a:loading:933335927659561070>'			# -1
]


HELPMESSAGE = f'{ICON[1]} **REHISOS USER MANUAL**\n\n\
` ██▀███  ▓█████  ██░ ██  ██▓  ██████  ▒█████    ██████ `\n\
`▓██ ▒ ██▒▓█   ▀ ▓██░ ██▒▓██▒▒██    ▒ ▒██▒  ██▒▒██    ▒ `\n\
`▓██ ░▄█ ▒▒███   ▒██▀▀██░▒██▒░ ▓██▄   ▒██░  ██▒░ ▓██▄   `\n\
`▒██▀▀█▄  ▒▓█  ▄ ░▓█ ░██ ░██░  ▒   ██▒▒██   ██░  ▒   ██▒`\n\
`░██▓ ▒██▒░▒████▒░▓█▒░██▓░██░▒██████▒▒░ ████▓▒░▒██████▒▒`\n\
`░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░`\n\
`  ░▒ ░ ▒░ ░ ░  ░ ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░`\n\
`  ░░   ░    ░    ░  ░░ ░ ▒ ░░  ░  ░  ░ ░ ░ ▒  ░  ░  ░  `\n\
`   ░        ░  ░ ░  ░  ░ ░        ░      ░ ░        ░  `\n\
`▀█████████████████████████████████████████████████████▀`\n\
`      ▀███▀                                            `\n\
`        █▒                ▀  █▀▀▄ █▀▀ ▄▀▀▄             `\n\
`        █▒   ▄███████▓▒░  █▀ █  █ █▀  █  █ ░▒▓████████▄`\n\
`        ▓░   ██          ▀▀▀ ▀  ▀ ▀    ▀▀            ██`\n\
`        ▒    ██   .help      ⚲   список команд       ██`\n\
`        ░    ██   .bones     ⚲   кинуть кости        ██`\n\
`             ██   .whoami    ⚲   кто ты по жизни?    ██`\n\
`        ░    ██   .moonday   ⚲   лунный день         ██`\n\
`        ░    ██   .today     ⚲   по григорианскому   ██`\n\
`        ░    ██   .data      ⚲   неее                ██`\n\
`        ░    ██   .grafic    ⚲   постоить график     ██`\n\
`        ▒    ██   .weather   ⚲   погода сейчас       ██`\n\
`       ░▓░   ██                                      ██`\n\
`       ▓█▓   ██ ▀ ▀▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀▀ ▀ ██`\n\
`        ▀    ██   .ғɪʙsᴇᴀʀᴄʜᴍᴇʀʟᴇᴀʙʀᴀʜᴀᴍs   ??????   ██`\n\
`             ██                                      ██`\n\
`             ▀████████████▓▒░ ░▒▓█████████████████████▀`\n'

HELPSQL = f'{ICON[6]} **SQL MANUAL**\n\n\
**CREATE** ~~IF NOT EXIST~~ **TABLE** ||table_name|| (||column_name|| ||column_datatype||, ...)\n\
**DROP** ~~IF EXIST~~ **TABLE** ||table_name||\n\n\
**SELECT** ||column_name||, ... **FROM** ||table_name||  **WHERE** ||column_name|| = ||value||\n\
**INSERT INTO** ||table_name|| (||column_name||, ...) **VALUES** (||value||, ...)\n\
**UPDATE** ||table_name|| **SET** ||column_name|| = ||new_value|| **WHERE** ||column_name|| = ||value||\n\n\
**ALTER** ||table_name|| **RENAME** ~~COLUMN~~ ||column_name|| **TO** ||new_column_name||\n\
**ALTER** ||table_name|| **ADD** ~~COLUMN~~ ||column_name||\n\
**ALTER** ||table_name|| **DROP** ~~COLUMN~~ ||column_name||\n\n\
{CODE}fix\n\
🝄 DATATYPE   🝄 TYPES ALLOWED IN THAT COLUMN\n\
🝙 INTEGER    🝙 INTEGER, REAL, TEXT, BLOB\n\
🝙 REAL       🝙 REAL, TEXT, BLOB\n\
🝙 TEXT       🝙 TEXT, BLOB\n\
🝙 BLOB       🝙 INTEGER, REAL, TEXT, BLOB\n\
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n\
INTEGER: /INT /INTEGER /TINYINT /SMALLINT /MEDIUMINT /BIGINT /UNSIGNED BIG INT /INT2 /INT8\n\
TEXT: /CHARACTER(20) /VARCHAR(255) /VARYING CHARACTER(255) /NCHAR(55) /NATIVE CHARACTER(70) /NVARCHAR(100) /TEXT /CLOB\n\
BLOB: /BLOB /no datatype specified\n\
REAL: /REAL /DOUBLE /DOUBLE PRECISION /FLOAT\n\
NUMERIC: /NUMERIC /DECIMAL(10,5) /BOOLEAN /DATE /DATETIME\n\
{CODE}\n\
DOCUMENTATION: ||https://www.postgresql.org/docs/current/index.html||\n\
ДОКУМЕНТАЦИЯ: ||https://postgrespro.ru/docs/postgresql/14/index||\n\
HEROKU MANGING DB: ||https://devcenter.heroku.com/articles/managing-heroku-postgres-using-cli||\n'

FILES_URL = ['https://cdn.discordapp.com/attachments/871746192743211018/', '/Grand_Theft_Auto_V_Screenshot_20']

TYPEMESS = [
	"hui▌\n␀",
	"hui\n␀",
	"hui▌\n␀",
	"hui\n␀",
	"hui▌\n␀",
	"hu▌\n␡",
	"h▌\n␡",
	"hi▌\n␡",
	"hi\n␀",
	"hi\n␛",
	"~~hi~~\n␛"
]

HI = [
	'как же без тебя было скучно!',
	'хай.',
	'добро пожаловать!',
	'ты блядь еще кто?',
	'я ждал тебя и вот ты здесь.',
	'ну и ава у тебя, это лечится вообще?',
	'мне кажется, мы подружимся.'
]

BYE = [
	'откис еблан.',
	'съебался в ужасе.',
	'ну и пиздуй!',
	'вышел в окно.',
	'прощай, я не буду скучать.',
	'прощай, я буду скучать.'
]

RACISTS_JOCKES = [
	'В машине сидят негp и мексиканец. Кто за рулём? Коп.',
	'Негp и мексиканец падают с небоскрёба. Кто упадёт первым? Какая разница?',
	'Как узнать, что у негpа недавно был секс? Его глаза всё ещё красные от перцового балончика.',
	'Как называется негp на велосипеде? Вор.',
	'Почему, когда какие-либо приборы не работают - по ним бьют? С рабами это срабатывало.',
	'Негp и мексиканец падают с дерева. Кто упадёт на землюпервым? Мексиканец. Негp не долетит - ему помешает верёвка.',
	'Что общего между кроссовками Nice и Ку-Клукс-Кланом? Они заставляют негpов быстро бегать.',
	'Как сделать так что бы негp перестал тонуть? Надо просто убрать ногу с его головы.',
	'Почему негpы так плохо пахнут? Чтобы слепые их тоже могли ненавидеть.',
	'Какие три самых сложных года в жизни негра? Первый класс.',
	'Почему негp, когда едет в машине, закрывает все окна? Он думает, что воняет снаружи.',
	'Как снять негра с дерева? Перерезать веревку.'
]

LABEL = {
	'CONTR': ['␀', '␁', '␂', '␃', '␄', '␅', '␆', '␇', '␈', '␉', '␊', '␋', '␌', '␍', '␎', '␏', '␐', '␑', '␒', '␓', '␔', '␕', '␖', '␗', '␘', '␙', '␚', '␛', '␜', '␝', '␞', '␟', '␠', '␡'],
	'RAIN': ['🜲', '🜁', '🜘', '🝄', '🝙', '⸙', '⸸', '⸕', 'ⵠ', 'ⵐ', 'ⵁ', 'ⵉ', 'キ', '𐓏', 'ꥥ', '꠹', 'ꬖ', 'ꔶ', '꘩', '꘨', '꘧', '꘦', '꘥', '꘤', '꘣', '꘢', '꘠', '෴'],
	'RUNES': ['ᚠ', 'ᚡ', 'ᚢ', 'ᚣ', 'ᚤ', 'ᚥ', 'ᚦ', 'ᚧ', 'ᚨ', 'ᚩ', 'ᚪ', 'ᚫ', 'ᚬ', 'ᚭ', 'ᚮ', 'ᚯ', 'ᚰ', 'ᚱ', 'ᚲ', 'ᚳ', 'ᚴ', 'ᚵ', 'ᚶ', 'ᚷ', 'ᚸ', 'ᚹ', 'ᚺ', 'ᚻ', 'ᚼ', 'ᚽ', 'ᚾ', 'ᚿ', 'ᛀ', 'ᛁ', 'ᛂ', 'ᛃ', 'ᛄ', 'ᛅ', 'ᛆ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛊ', 'ᛋ', 'ᛌ', 'ᛍ', 'ᛎ', 'ᛏ', 'ᛐ', 'ᛑ', 'ᛒ', 'ᛓ', 'ᛔ', 'ᛕ', 'ᛖ', 'ᛗ', 'ᛘ', 'ᛙ', 'ᛚ', 'ᛛ', 'ᛜ', 'ᛝ', 'ᛞ', 'ᛟ', 'ᛠ', 'ᛡ','ᛢ', 'ᛣ', 'ᛤ', 'ᛥ', 'ᛦ', 'ᛧ', 'ᛨ', 'ᛩ', 'ᛪ'],
	'rome': ['ⅰ','ⅱ','ⅲ','ⅳ','ⅴ','ⅵ','ⅶ','ⅷ','ⅸ','ⅹ','ⅺ','ⅻ','ⅼ','ⅽ','ⅾ','ⅿ'],
	'ROME': ['Ⅰ','Ⅱ','Ⅲ','Ⅳ','Ⅴ','Ⅵ','Ⅶ','Ⅷ','Ⅸ','Ⅹ','Ⅺ','Ⅻ','Ⅼ','Ⅽ','Ⅾ','Ⅿ']
}

crypt = '6hZtEeD8krYF)A:Xoai4WjNOS2H^sgCP%5zydRQlf07npxuqVTUJmc91v#K3LG!bw$MBI'


#░░░░░░   ░░░░░░   ░░░░░░  ░░   ░░ ░░░░░░░ ░░░░░░  ░░    ░░ 
#▒▒   ▒▒ ▒▒    ▒▒ ▒▒    ▒▒ ▒▒  ▒▒  ▒▒      ▒▒   ▒▒  ▒▒  ▒▒  
#▒▒▒▒▒▒  ▒▒    ▒▒ ▒▒    ▒▒ ▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒    ▒▒▒▒   
#▓▓   ▓▓ ▓▓    ▓▓ ▓▓    ▓▓ ▓▓  ▓▓  ▓▓      ▓▓   ▓▓    ▓▓    
#██   ██  ██████   ██████  ██   ██ ███████ ██   ██    ██    


async def paint(channel, pic_: str, time):
	with open(os.path.join('texted', 'ascii.txt'), encoding='utf-8') as pic_file:
		picture = pic_file.readlines()
		cat_ = {
			# 0: начало рисунка
			# 1: конец первого слайда
			# 2: начало второго слайда
			# 3: конец рисунка минус количество строк в слайде
			# 4: шаг слайдов
			# 5: количество строк в слайде
			'nude': [616, 632, 620, 681, 4, 16],
			'warr': [1, 21, 24, 597, 22, 19]
		}
		await channel.send(f'{CODE}{"".join(picture[cat_[pic_][0]:cat_[pic_][1]])}{CODE}')
		message = channel.last_message
		for i in range(cat_[pic_][2], cat_[pic_][3], cat_[pic_][4]):
			time.sleep(0.9)
			await message.edit(content=f'{CODE}{"".join(picture[i:i+cat_[pic_][5]])}{CODE}')
		await message.delete(delay=1.0)


def describe(value: tuple, title='', names=None) -> str: 
	custom_columns = ['Fi†','Se†','Tre','Fo†','Fi‡','Si†','Se‡','Ei†','Ni†','Te†','El†','Twe']
	custom_rows = ['†5†k', '†4†k', '†3†k', '†2†k', '†1†k']
	block = ['█', '▄']
	value = [int(val) for val in (value[:12] if len(value) > 12 else value)]
	names = [name for name in names[:12]] if names is not None and len(names) > 12 else names
	values = [val*1000 for val in value]
	max_value = max(values)
	bit = max_value//30
	grafic_length = len(values)*6 + 7
	current_rows = [
		max_value//1000,
		max_value//5*4//1000,
		max_value//5*3//1000,
		max_value//5*2//1000,
		max_value//5//1000
	]
	current_rows = list(map(lambda x: (str(x//1000)+'k').rjust(4, " "), current_rows)) if max(value) > 10000 else \
	               list(map(lambda x: str(x).rjust(4, " "), current_rows))
	with open(os.path.join('texted', 'grafic.txt'), encoding='utf-8') as grafic:
		this_grafic = [line[:grafic_length] for line in grafic.readlines()]
		this_grafic[18] = f'{this_grafic[18]}────⮞' if len(values) < 13 else this_grafic[18]
		for i, row in enumerate(current_rows):
			this_grafic = [line.replace(custom_rows[i], current_rows[i]) for line in this_grafic]
		if names is not None:
			for i, name in enumerate(names):
				mane = name.rjust(3, "†") if len(name) < 3 else name[:3]
				this_grafic[20] = this_grafic[20].replace(custom_columns[i], mane.upper())
		for index, value_ in enumerate(values):
			value_bit = (value_-bit)/(bit*2)
			value_height = -4 - int(value_bit + 0.25)
			value_residue = (value_-bit)//(bit/1000) - int(value_bit+0.25)*2000
			for i in range(-4, value_height, -1):
				this_grafic[i] = this_grafic[i].replace(f'█{index:X}█', block[0]*3)
			if value_residue > 999:
				this_grafic[value_height] = this_grafic[value_height].replace(f'█{index:X}█', block[1]*3)
			this_grafic = [line.replace(f'█{index:X}█', '   ') for line in this_grafic]
		printer = ''.join([f'{line}\n' for line in this_grafic])
		grafic_ = f'{CODE}{title}{printer}{CODE}'
		return grafic_


def formater(records, icon='', description=None) -> str:
	linage = [description]
	for data in records:
		linage.append(list(data))
	for i in range(len(linage[0])):
		size = max((len(str(x[i])) for x in linage)) + 2
		for i_ in range(len(linage)):
			linage[i_][i] = str(linage[i_][i]).ljust(size, " ")
	package = f'  ┌ {"┌ ".join(linage[0])}  \n'
	for data in linage[1:]:
		package += f'  ┊ {"┊ ".join([str(x) for x in data])}  \n'
	package = f'{CODE}fix\n{icon}\n{package}\n🡷{CODE}'
	return package


def decoder(pack_, key) -> str:
	ring = int(''.join(x for x in key if x.isnumeric()))
	if down(key, ring)//10-ring:
		sklep, pack, cack_ = '', '', -1
		for i, x in enumerate(key[:len(pack_)-69]):
			sklep = sklep + pack_[~crypt.find(x)-len(pack):cack_]
			pack = pack + pack_[cack_] 
			cack_ = ~crypt.find(x)-len(pack)
		sklep += pack_[:cack_+1]
		pack = pack.translate(str.maketrans(sklep, crypt))
		pack = ''.join(chr(ord(pack[x])+ord(key[-2])-ord(key[-1])) for x in range(len(pack)))
	else:
		pack = f'{ICON[3]} нахуйпошёл'
	return pack

def crypter(random, pack, key) -> str:
	sklep = [x for x in crypt]; random.shuffle(sklep); sklep = ''.join(sklep);
	pack = ''.join(chr(ord(pack[x])-ord(key[-2])+ord(key[-1])) for x in range(len(pack)))
	pack = pack.translate(str.maketrans(crypt, sklep))
	pack_, cack_ = '', 0
	for i, x in enumerate(pack):
		pack_ = sklep[cack_:crypt.find(key[i])] + x + pack_
		cack_ = crypt.find(key[i])
	pack_ = sklep[cack_:] + pack_
	return pack_

def down(key, ring) -> int:
	pyramid = [[x+i for x in range(i)] for i in range(1, ring)]
	def tentaculum(level, index):
		while level < len(pyramid)-1:
			return max(
			pyramid[level][index] + tentaculum(level+1, index),
			pyramid[level][index] + tentaculum(level+1, index+1)
			)
		return pyramid[level][index]
	return tentaculum(0, 0)

def generator(random, length=8):
	password = ''.join([random.choice(crypt) for x in range(int(length))])
	return password


#░░       ░░░░░░   ░░░░░░   ░░░░░░  ░░░░░░░ ░░░░░░  
#▒▒      ▒▒    ▒▒ ▒▒       ▒▒       ▒▒      ▒▒   ▒▒ 
#▒▒      ▒▒    ▒▒ ▒▒   ▒▒▒ ▒▒   ▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒▒  
#▓▓      ▓▓    ▓▓ ▓▓    ▓▓ ▓▓    ▓▓ ▓▓      ▓▓   ▓▓ 
#███████  ██████   ██████   ██████  ███████ ██   ██ 


async def logit(type_: str, client=None, channel_id=None, member=None, author=None, cursor=None, action=None, command=None, e=None):
	title = {
		'MEMBER': f'{ICON[-3]} 🡶**┊MEMBER**',	
		'DAFUCK': f'{ICON[-6]} 🡶**┊{action} ERR⛶R:**\n',
		'ERROR_': f'{ICON[+0]} 🡶**┊ERR⛶R:**\n',
		'ACTION': {
		'INSERT': f'{ICON[-4]} 🡶**┊{action}:**\n',
		'UPDATE': f'{ICON[-4]} 🡶**┊{action}:**\n',
		'CREATE': f'{ICON[-5]} 🡶**┊{action}:**\n',
		 'ALTER': f'{ICON[-5]} 🡶**┊{action}:**\n',
		  'DROP': f'{ICON[-5]} 🡶**┊{action}:**\n'
		}
	}
	message_ = title[type_][action] if type_ == 'ACTION' else title[type_]
	if member: message_ = f'{message_} **||{member.name}||**\n';
	if author: message_ = f'{message_} error commander {author} fucked up';
	if channel_id: message_ = f'{message_} in <#{channel_id}>';
	message_ = f'{message_}:\n' if author or channel_id else f'{message_}'
	if type_ == 'MEMBER': message_ = f'{message_} big brother wrote it all down:\n' if not cursor else \
	                                 f'{message_} back to the server and already in base:\n';
	if cursor:
		cursor.execute('SELECT register, mention, discord_id, name, score \
						FROM members WHERE discord_id = {};'.format(member.id))
		user_info = cursor.fetchall()
		message_ = f'{message_}{CODE}{" ﹕ ".join(str(x) for x in user_info[0])}{CODE}\n'
	if command:
		message_ = f'{message_}{CODE}{action} {command}{CODE}\n'
	if e:
		message_ = f'{message_}{CODE}{e}{CODE}'
	await client.get_channel(LOGS_ID).send(message_)
