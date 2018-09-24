from tkinter import filedialog
from tkinter import *
from PIL import Image

# def show(x):
# 	for i in range(0,len(x)):
# 		print(x[i])

def resize():
	list_of_files=get_file_names()
	print(list_of_files)
	h=int(height_entry.get())
	w=int(width_entry.get())
	size=(h,w)
	name=str(output.get())
	i=Image.open(list_of_files[0])
	i.thumbnail(size)
	i.save('{}.jpg'.format(name))


def get_file_names():
	x=entry.get()
	#print(x)
	list_files=x.split(" ")
	#show(list_files)
	return list_files

def choose_file():
	top.filename =  filedialog.askopenfilenames(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))	
	entry.insert(0,top.filename)
	return

top=Tk()
top.title("Sa1f Image Resize Tool")

b = Button(top, text="Choose File", command=choose_file)
b.grid(column=0, row=0,padx=(5,10),pady=(5,5))

entry=Entry(top,bd=3)
entry.grid(column=1, row=0)

b2 = Button(top, text="print file name", command=get_file_names)
b2.grid(column=2, row=0)
l1=Label(top,text="Height")
l1.grid(column=0, row=1)

height_entry=Entry(top,bd=3)
height_entry.grid(column=1, row=1)

l2=Label(top,text="Width")
l2.grid(column=0, row=2,padx=(10,10))

width_entry=Entry(top,bd=3)
width_entry.grid(column=1, row=2)



l3=Label(top,text="Output File Name")
l3.grid(column=0, row=3,padx=(10,10))

output=Entry(top,bd=3)
output.grid(column=1, row=3)




b2 = Button(top, text="Resize!",command=resize)
b2.grid(column=2, row=4,padx=(5,10),pady=(5,5))



top.geometry("400x200")
top.mainloop()