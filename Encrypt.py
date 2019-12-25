###############################
__date__ = "06-Nov-2019"
__author__ = "Neilmark Ochea"
__codename__ = "Ph.ClownX"
__Team__ = "FilTech Hackers Philippines @2016"
########### Import ###############
import os, sys, time, marshal, base64, zlib
########### Color ################
if sys.platform in ["linux","linux2"]:

    BK='\033[1;30m' # Bold+Black
    BR='\033[1;31m' # Bold+Red
    BG='\033[1;32m' # Bold+Green
    BY='\033[1;33m' # Bold+Yellow
    BB='\033[1;34m' # Bold+Blue
    BM='\033[1;35m' # Bold+Magenta
    BC='\033[1;36m' # Bold+Cyan
    BW='\033[1;37m' # Bold+White
    
else:

    BK=''
    BR=''
    BG=''
    BY=''
    BB=''
    BM=''
    BC=''
    BW=''

########### Banner #########
def banner():
	os.system('clear')
	print('')
	print(BG + "  ____ _  _ ____ ____ _   _ ___  ___")
	print(BG + "  |___ |\ | |    |__/  \_/  |__]  |")
	print(BG + "  |___ | \| |___ |  \   |   |     |" + BR + ".py")
	print('')
########### Main ##########
def main():
	banner()
	try:
		print(BY + '    Menu : \n') 
		print(BY + '   [' + BR + '01' + BY + ']' + BG + ' Marshal')
		print(BY + '   [' + BR + '02' + BY + ']' + BG + ' Base16')
		print(BY + '   [' + BR + '03' + BY + ']' + BG + ' Base32')
		print(BY + '   [' + BR + '04' + BY + ']' + BG + ' Base64')
		print(BY + '   [' + BR + '05' + BY + ']' + BG + ' Zlib,Base16')
		print(BY + '   [' + BR + '06' + BY + ']' + BG + ' Zlib,Base32')
		print(BY + '   [' + BR + '07' + BY + ']' + BG + ' Zlib,Base64')
		print(BY + '   [' + BR + '08' + BY + ']' + BG + ' Zlib,Base16,Marshal')
		print(BY + '   [' + BR + '09' + BY + ']' + BG + ' Zlib,Base32,Marshal')
		print(BY + '   [' + BR + '10' + BY + ']' + BG + ' Zlib,Base64,Marshal')
		print(BY + '   [' + BR + '11' + BY + ']' + BG + ' Obfuscate String')
		print(BY + '   [' + BR + '12' + BY + ']' + BG + ' Obfuscate String,Marshal\n')
		print(BY + '   [' + BR + '99' + BY + ']' + BG + ' Info')
		print(BY + '   [' + BR + '00' + BY + ']' + BR + ' Exit\n')
		ochea = raw_input(BR + 'Encrypt' + BY + ' >> ' + BG)
		if ochea in ['1','01']:
			mars()
		elif ochea in ['2','02']:
			bas16()
		elif ochea in ['3','03']:
			bas32()
		elif ochea in ['4','04']:
			bas64()
		elif ochea in ['5','05']:
			zbas16()
		elif ochea in ['6','06']:
			zbas32()
		elif ochea in ['7','07']:
			zbas64()
		elif ochea in ['8','08']:
			zb16mars()
		elif  ochea in ['9','09']:
			zb32mars()
		elif ochea in ['10']:
			zb64mars()
		elif ochea in ['11']:
			obstring()
		elif ochea in ['12']:
			obsmars()
		elif ochea in ['99']:
			info()
		elif ochea in ['0','00']:
			sys.exit()
		if ochea == '':
			main()
		else:
			banner()
			print(BR + "[" + BY + "-" + BR + "] " + BG + "command " + BR + ochea + BG + " not found")
			time.sleep(2)
			main()
	except (KeyboardInterrupt, EOFError):
		main()
	except IndexError:
		main()
########### Marshal ##########
def mars():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		print('')
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		fileopen = open(file).read()
		a = compile(fileopen, 'ochea', 'exec')
		m = marshal.dumps(a)
		s = repr(m)
		b = 'import marshal\nexec(marshal.loads(' + s + '))'
		c = file.replace('.py', '-Marshal.py')
		d = open('output/' + c , 'w')
		d.write(b)
		d.close()
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + c)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
########### Base16 ##########
def bas16():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		print('')
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		fileopen = open(file).read()
		a = base64.b16encode(fileopen)
		b = "import base64\nexec(base64.b16decode('" + a + "'))"
		c = file.replace('.py', '-Base16.py')
		d = open('output/' + c , 'w')
		d.write(b)
		d.close()
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + c)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
########### Base32 ##########
def bas32():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		print('')
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		fileopen = open(file).read()
		a = base64.b32encode(fileopen)
		b = "import base64\nexec(base64.b32decode('" + a + "'))"
		c = file.replace('.py', '-Base32.py')
		d = open('output/' + c , 'w')
		d.write(b)
		d.close()
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + c)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
########### Base64 ##########
def bas64():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		print('')
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		fileopen = open(file).read()
		a = base64.b64encode(fileopen)
		b = "import base64\nexec(base64.b64decode('" + a + "'))"
		c = file.replace('.py', '-Base64.py')
		d = open('output/' + c , 'w')
		d.write(b)
		d.close()
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + c)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
########### ZBase16 ##########
def zbas16():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		print('')
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		fileopen = open(file).read()
		c = zlib.compress(fileopen)
		d = base64.b16encode(c)
		e = 'import zlib,base64\nexec(zlib.decompress(base64.b16decode("' + d + '")))'
		f = file.replace('.py', '-ZBase16.py')
		g = open('output/' + f, 'w')
		g.write(e)
		g.close()
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + f)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
########### ZBase32 ##########
def zbas32():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		print('')
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		fileopen = open(file).read()
		c = zlib.compress(fileopen)
		d = base64.b32encode(c)
		e = 'import zlib,base64\nexec(zlib.decompress(base64.b32decode("' + d + '")))'
		f = file.replace('.py', '-ZBase32.py')
		g = open('output/' + f, 'w')
		g.write(e)
		g.close()
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + f)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
########### ZBase64 ##########
def zbas64():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		print('')
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		fileopen = open(file).read()
		c = zlib.compress(fileopen)
		d = base64.b64encode(c)
		e = 'import zlib,base64\nexec(zlib.decompress(base64.b64decode("' + d + '")))'
		f = file.replace('.py', '-ZBase64.py')
		g = open('output/' + f, 'w')
		g.write(e)
		g.close()
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + f)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
########### ZB16Marshal ##########
def zb16mars():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		print('')
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		fileopen = open(file).read()
		sa = compile(fileopen, 'ochea', 'exec')
		sb = marshal.dumps(sa)
		c = zlib.compress(sb)
		d = base64.b16encode(c)
		e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("' + str(d) + '"))))'
		f = file.replace('.py', '-ZB16Marshal.py')
		g = open('output/' + f, 'w')
		g.write(e)
		g.close()
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + f)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
########### ZB32Marshal ##########
def zb32mars():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		print('')
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		fileopen = open(file).read()
		sa = compile(fileopen, 'ochea', 'exec')
		sb = marshal.dumps(sa)
		c = zlib.compress(sb)
		d = base64.b32encode(c)
		e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("' + str(d) + '"))))'
		f = file.replace('.py', '-ZB32Marshal.py')
		g = open('output/' + f, 'w')
		g.write(e)
		g.close()
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + f)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
########### ZB64Marshal ##########
def zb64mars():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		print('')
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		fileopen = open(file).read()
		sa = compile(fileopen, 'ochea', 'exec')
		sb = marshal.dumps(sa)
		c = zlib.compress(sb)
		d = base64.b64encode(c)
		e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + str(d) + '"))))'
		f = file.replace('.py', '-ZB64Marshal.py')
		g = open('output/' + f, 'w')
		g.write(e)
		g.close()
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + f)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
########### Obfuscation String ##########
def obstring():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		string = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'String' + BY + ' : ' + BR)
		fileopen = open(file,'r')
		a = []
		for i in fileopen:
			a.append(ord(i))
		c = []
		for i in a:
			c.append(string.replace("'","").replace('"','')*i)
		e="""OBString={};exec("".join([chr(len(i)) for i in OBString]))""".format(c)
		f = file.replace('.py', '-OBString.py')
		g = open('output/' + f, 'w')
		g.write(e)
		g.close()
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + f)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
 ########### OBSMarshal##########
def obsmars():
	banner()
	try:
		os.mkdir('output')
	except OSError:
		pass
	try:
		file = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'Filename' + BY + ' : ' + BR)
		string = raw_input(BR + '[' + BY + '+' + BR + '] ' + BG + 'String' + BY + ' : ' + BR)
		fileopen = open(file,'r')
		a = []
		for i in fileopen:
			a.append(ord(i))
		c = []
		for i in a:
			c.append(string.replace("'","").replace('"','')*i)
		e="""OBString={};exec("".join([chr(len(i)) for i in OBString]))""".format(c)
		f =  file.replace(file, 'OBSM.py')
		g = open(f , 'w')
		g.write(e)
		g.close()
		h = open('OBSM.py').read()
		i = compile(h, 'ochea', 'exec')
		j = marshal.dumps(i)
		k = repr(j)
		l = 'import marshal\nexec(marshal.loads(' + k + '))'
		m = file.replace('.py', '-OBSMarshal.py')
		n = open('output/' + m , 'w')
		n.write(l)
		n.close()
		os.system('rm -rf ' + f)
		banner()
		print(BR + '[' + BY + '+' + BR + ']' + BG +' Encrypting ' + BW + '...')
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Sucessfully Encrypted')
		print(BR + '[' + BY + '+' + BR + ']' + BG + ' File saved : output/' + BR + m)
		raw_input(BG + '\nDone ' + BY + '>> ' + BR)
		main()
	except IndentationError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + '] ' + BG + file +' failed to Compiled')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except ImportError:
		banner()
		print(BR + '\n[' + BY + '+' + BR + ']' + BG +' Failed to Import')
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except IOError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' file not found'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
	except SyntaxError:
		banner()
		print BR + '\n[' + BY + '-' + BR + '] ' + BG + file + ' failed to Encrypt'
		raw_input(BR + '\nBack ' + BY + '>> ' + BR)
		main()
########### Info Menu ##########
def infome():
	print('')
	print(BR + '   Author' + BY + '   :   ' + BG + 'Neilmark Ochea')
	print(BR + '   Codename' + BY + ' :   ' + BG + 'Ph.ClownX')
	print(BR + '   Tools' + BY + '    :   ' + BG + 'Encrypt Python')
	print(BR + '   Github' + BY + '   :   ' + BG + 'www.github.com/0ch3a\n')
	print(BY + '  [' + BR + '00' + BY + ']' + BR+ ' Back\n')
########### Info Main ##########
def info():
  banner()
  infome()
  try:
	ochea = raw_input(BR + 'Encrypt' + BY +'/' + BR + 'Info ' + BY + '>> ' + BG)

	if ochea in ['0','00']:
		os.system('xdg-open https://github.com/0ch3a')
		main()
	if ochea == '':
		info()
	else:
		print(BR + "[" + BY + "-" + BR + "]" + BG + " command " + BR + ochea + BG + " not found")
		time.sleep(2)
		info()

  except KeyboardInterrupt:
	info()
  except IndexError:
	info()

if __name__=='__main__':
	main()