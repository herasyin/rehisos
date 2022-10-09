# storage of creepy ship and useful func 🝄
# сopyleft: ⌨ 2022 >>-her--> all rights not reserved

import os
import random

HERA_ID = 726267858283266160
JACK_ID = 424926267532640257
POST_ID = 802766660099768321
CHAT_ID = 859024516906614784
LOGS_ID = 963216065490481232

ROLES = {
	'<:eye:742677301157953559>': 741356737373667458 #observer
}

CODE = '```' # discord formating

CRYPT = '6hZtEeD8krYF)A:Xoai4WjNOS2H^sgCP%5zydRQlf07npxuqVTUJmc91v#K3LG!bw$MBI'


#░░░░░░   ░░░░░░   ░░░░░░  ░░   ░░ ░░░░░░░ ░░░░░░  ░░    ░░
#▒▒   ▒▒ ▒▒    ▒▒ ▒▒    ▒▒ ▒▒  ▒▒  ▒▒      ▒▒   ▒▒  ▒▒  ▒▒
#▒▒▒▒▒▒  ▒▒    ▒▒ ▒▒    ▒▒ ▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒    ▒▒▒▒
#▓▓   ▓▓ ▓▓    ▓▓ ▓▓    ▓▓ ▓▓  ▓▓  ▓▓      ▓▓   ▓▓    ▓▓
#██   ██  ██████   ██████  ██   ██ ███████ ██   ██    ██


def paint() -> 'image frames':
	with open(os.path.join('texted', 'ascii.txt'), encoding='utf-8') as pic_file:
		picture = pic_file.readlines()
	# BUILD FRAMES FIRST PIXEL INDEXES i:i_
	# ┌START🡫┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
		i = [n for n in range(1, 724, 25)]
		i_= [0 for _ in range(29)]
	# └702:0┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
	# ┌🡪┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
		for _ in range(5): i.append(725);
		for n in range(0, 41, 10): i_.append(n);
	# └726:40┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
	# ┌🡨┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
		for _ in range(2): i.append(725);
		for n in range(32, 23, -8): i_.append(n);
	# └726:24┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
	# ┌🡮┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
		for n in range(725, 750, 8): i.append(n);
		for n in range(16, 23, 2): i_.append(n);
	# └750:22┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
	# ┌🡯┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈𐓏
		for n in range(754, 760, 5): i.append(n);
		for n in range(12, 1, -10): i_.append(n);
	# └760:2┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
	# ┌🡪┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈𐓏
		for _ in range(4): i.append(759);
		for n in range(15, 61, 15): i_.append(n);
	# └760:61┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
	# ┌🡯┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈𐓏
		for n in range(766, 802, 7): i.append(n);
		for n in range(55, 26, -5): i_.append(n);
	# └END┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
		frames = []
		bord = '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n'
		bord_= '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'
		for s, r in zip(i, i_):
			frames.append('{0}{1}{3}{2}{0}'.format(CODE, bord, bord_,
				''.join('{:┃^32}\n'.format(line[r:r+30]) for line in picture[s:s+23])))
		return frames


def describe(value, title='', names=None) -> str:
	custom_columns = ['Fi†','Se†','Tre','Fo†','Fi‡','Si†',
					  'Se‡','Ei†','Ni†','Te†','El†','Twe']
	custom_rows = ['†5†k', '†4†k', '†3†k', '†2†k', '†1†k']
	block = ['█', '▄']
	value = [int(val) for val in (value[:12] if len(value) > 12 else value)]
	names = names[:12] if names is not None and len(names) > 12 else names
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
	if max(value) > 10000:
		current_rows = [x//1000 for x in current_rows]
	current_rows = map(lambda x: str(x).rjust(4, " "), current_rows)
	with open(os.path.join('texted', 'grafic.txt'), encoding='utf-8') as grafic:
		this_grafic = [line[:grafic_length] for line in grafic.readlines()]
		this_grafic[18] = f'{this_grafic[18]}────⮞' if len(values) < 13 else this_grafic[18]
		for i, row in enumerate(current_rows):
			this_grafic = [line.replace(custom_rows[i], row) for line in this_grafic]
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


def decoder(pack_, name) -> str:
	potion = down(ord('🝄')+ord('✝'))//ord(name[-1])
	sklep, pack = pack_[:len(CRYPT)], pack_[len(CRYPT):]
	sklep += pack_[:cack_+1]
	pack = pack.translate(str.maketrans(sklep, CRYPT))
	pack = ''.join(chr(ord(pack[x])+ord(potion)-ord(name[1])) for x inrange(len(pack)))
	return pack

def crypter(pack, name) -> str:
	potion = down(ord('🝄')+ord('✝'))//ord(name[-1])
	sklep = [x for x in CRYPT]; random.shuffle(sklep); sklep = ''.join(sklep);
	pack = ''.join(chr(ord(pack[x])-ord(potion)+ord(name[1])) for x in range(len(pack)))
	pack = pack.translate(str.maketrans(CRYPT, sklep))
	pack_ = sklep + pack
	return pack_

def down(ring) -> int:
	pyramid = [[x+i for x in range(i)] for i in range(1, ring)]
	def tentaculum(level, index):
		while level < len(pyramid)-1:
			return max(
			pyramid[level][index] + tentaculum(level+1, index),
			pyramid[level][index] + tentaculum(level+1, index+1)
			)
		return pyramid[level][index]
	return tentaculum(0, 0)

def generator(lenght=8) -> str:
    builder = lambda lenght: ''.join([random.choice(CRYPT) for x in range(int(lenght))])
    password = builder(lenght)
    while not any(x.isnumeric() for x in password) or \
          not any(x.islower () for x in password) or \
          not any(x.isupper() for x in password):
        password = builder(lenght)
    return password


#░░       ░░░░░░   ░░░░░░   ░░░░░░  ░░░░░░░ ░░░░░░
#▒▒      ▒▒    ▒▒ ▒▒       ▒▒       ▒▒      ▒▒   ▒▒
#▒▒      ▒▒    ▒▒ ▒▒   ▒▒▒ ▒▒   ▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒▒
#▓▓      ▓▓    ▓▓ ▓▓    ▓▓ ▓▓    ▓▓ ▓▓      ▓▓   ▓▓
#███████  ██████   ██████   ██████  ███████ ██   ██


async def logit(type_: str, client=None, channel_id=None, member=None, author=None, cursor=None, action=None, command=None, e=None):
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
