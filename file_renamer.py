import os, time
class Renamer():
	path = '';
	files = []
	def __init__(self,*args,**kargs):
		self.getPath()
		while(self.listFiles()==False):
			self.getPath()
		self.confirmPath()

		
	def	getPath(self):
		self.path = str(input('Digite o caminho dos arquivos a serem renomeados:'+"\n"))



	def listFiles(self):
		try:
			self.files = os.listdir(self.path)
		except OSError:
			print('Caminho inválido ou sem arquivos.')
			return False;
		return True;



	def confirmPath(self):
		print(self.files)
		resposta = str(input('Confirmar processamento dessa pasta? Todos os arquivos serão renomeados para sua data de criação. S/N ?'+"\n"))
		if(resposta == 's' or resposta == 'S'):
			print('renomeando...')
			with os.scandir(self.path) as it:
				for entry in it:
					if(not entry.name.startswith('.') and entry.is_file()):
						file = os.stat(entry.path)
						#print(file.st_mtime)
						year,month,day,hour,minute,second=time.localtime(file.st_mtime)[:-3]
						newname = "%04d.%02d.%02d.%02d.%02d.%02d"%(year,month,day,hour,minute,second)+os.path.splitext(entry.path)[1]
						print('Renomeando '+entry.path+' => '+self.path+'/'+newname)
						os.rename(entry.path, self.path+'/'+newname)


def main():
	Renamer()

main()




