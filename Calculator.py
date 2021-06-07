from tkinter import *

expression =""

def MainWindow():
	root = Tk()
	root.title("My Calculator")
	return root

def MenuBar(root):
	menu = Menu(root)										# create widget menu bar	
	menu.add_command(label="Quit", command=root.destroy)	# menubar Quit to close root
	root.config(menu=menu)									# add manu to root
	return menu

def Display(root):
	Label(root).grid(column=0, row=2)						# create free label
	display = Entry(root, width=50, bg="yellow", fg="black")
	display.grid(column=0, row=1, columnspan=4)				# (0,1) with 5 colmuns need	
	return display

def Collect(keypress):										# save value
	global expression
	expression += keypress									# add value	
	print(expression)
	return expression

def Insert(display, keypress):								
	display.insert(END, keypress)							# insert value display

def ClearDisplay(display, mode):
	global expression
	if mode == "DEL":
		expression = expression[0:len(display.get())-1]		# delete last value
		display.delete(len(display.get())-1, END)			# delete last value display
		print(expression)
	elif mode == "DELALL":
		expression = ""										# clear value
		display.delete(0, END)								# clear value display
		print(expression)

def Event(display, keypress):
	if keypress == "C":
		ClearDisplay(display, "DELALL")		# delete all
	elif keypress == "DEL":
		ClearDisplay(display, "DEL")		# delete last
	elif keypress == ".":
		Insert(display, keypress)
	elif keypress == "(":
		Insert(display, keypress)
	elif keypress == ")":
		Insert(display, keypress)				
	elif keypress == "+":
		Insert(display, keypress)
		Collect(keypress)
	elif keypress == "-":
		Insert(display, keypress)
		Collect(keypress)
	elif keypress == "X":
		Insert(display, keypress)
		Collect("*")
	elif keypress == "%":
		Insert(display, keypress)
		Collect("/")
	elif keypress == "=":
		global expression
		try:
			result = eval(expression)		# eval = calculator function
			print(result)
			ClearDisplay(display, "DELALL")	# delete all
			Insert(display, str(result))	# display result
		except:
			ClearDisplay(display, "DELALL") # delete all
			Insert(display, "ERROR")		# display error massage
	else:
		Insert(display, keypress)			# insert
		Collect(keypress)					# collect

def CalButton(root, display):

	Button(root, text="C", width=10, fg="Red", command=lambda: Event(display, "C")).grid(column=3, row=3)		# lambda to hold a event
	Button(root, text="DEL", width=10, fg="Red", command=lambda: Event(display, "DEL")).grid(column=2, row=3)

	Button(root, text="1", width=10, fg="blue", command=lambda: Event(display, "1")).grid(column=0, row=4)
	Button(root, text="2", width=10, fg="blue", command=lambda: Event(display, "2")).grid(column=1, row=4)
	Button(root, text="3", width=10, fg="blue", command=lambda: Event(display, "3")).grid(column=2, row=4)
	Button(root, text="4", width=10, fg="blue", command=lambda: Event(display, "4")).grid(column=0, row=5)
	Button(root, text="5", width=10, fg="blue", command=lambda: Event(display, "5")).grid(column=1, row=5)
	Button(root, text="6", width=10, fg="blue", command=lambda: Event(display, "6")).grid(column=2, row=5)
	Button(root, text="7", width=10, fg="blue", command=lambda: Event(display, "7")).grid(column=0, row=6)
	Button(root, text="8", width=10, fg="blue", command=lambda: Event(display, "8")).grid(column=1, row=6)
	Button(root, text="9", width=10, fg="blue", command=lambda: Event(display, "9")).grid(column=2, row=6)
	Button(root, text="0", width=10, fg="blue", command=lambda: Event(display, "10")).grid(column=1, row=7)

	Button(root, text=".", width=10, fg="black", command=lambda: Event(display, ".")).grid(column=0, row=7)
	Button(root, text="(", width=10, fg="black", command=lambda: Event(display, "(")).grid(column=0, row=8)	
	Button(root, text=")", width=10, fg="black", command=lambda: Event(display, ")")).grid(column=1, row=8)	

	Button(root, text="X", width=10, fg="black", command=lambda: Event(display, "X")).grid(column=3, row=4)
	Button(root, text="%", width=10, fg="black", command=lambda: Event(display, "%")).grid(column=3, row=5)
	Button(root, text="-", width=10, fg="black", command=lambda: Event(display, "-")).grid(column=3, row=6)	
	Button(root, text="+", width=10, fg="black", command=lambda: Event(display, "+")).grid(column=3, row=7)

	Button(root, text="=", width=22, bg="black", fg="white", command=lambda: Event(display, "=")).grid(column=2, row=8, columnspan=2)	# width 12 with 2 colmuns need


def calculator():
	root = MainWindow()			# create root, title
	menu = MenuBar(root)		# create widget menu bar
	display = Display(root)		# create display
	CalButton(root, display)	# create all buttons
	root.mainloop()

calculator()