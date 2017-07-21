class FileOwners:
	@staticmethod
	def group_by_owners(files):
		c={}
		for a,b in files.items():
			o=None
			if c.get(b)==None:
				o=[]
				o.append(a)
				c[b]=o
				print("first",o)
				print("first",c)
			else:
				o=[]
				o.extend(c[b])
				o.append(a)
				c[b]=o
				print(a)
				print("second",o)
				print("second",c)
		return c


files = {
	'Input.txt': 'Randy',
	'Code.py': 'Stan',
	'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))