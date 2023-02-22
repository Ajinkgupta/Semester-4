import tkinter
 
root = tkinter.Tk()

 
myCanvas = tkinter.Canvas(root, bg="white", height=300, width=300)
 
dimension = 1, 1, 300, 300
part1 = myCanvas.create_arc(dimension, start=0, extent=140, fill="red")
part2 = myCanvas.create_arc(dimension, start=140, extent=220, fill="green")
 
myCanvas.pack()
root.mainloop()
