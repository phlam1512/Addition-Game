#!/usr/bin/env python
from Tkinter import *  

#main function
def alpha():
    global qno
    global cans
    qno=0
    corans=0
    attempts=0
    for qno in range(1, 11):
        #clears the window
        import os
        os.system('cls')
        
        #randomiser
        import random
        operator=['+','-']
        var1=random.randrange(1,11)
        var2=random.randrange(var1,11)
        var3=random.choice(operator)   
        import operator
        ops = {"+": operator.add,
               "-": operator.sub,
                 "*": operator.mul,
                 "/": operator.div}
        op_char = var3
        op_func = ops[op_char]
        
        #user interface
        print "Question", qno
        print "What is:"
        print var2, var3, var1
        result = op_func(var2, var1)
        while(input() != result):
            print "Try again!"
            attempts+=1
        print "Correct!"
        import time
        time.sleep(0.25)
        os.system('cls')
        print "Loading..."
        time.sleep(0.25)
        #statistics calculation
        if qno<10:
            qno+=1
            attempts+=1
            corans+=1
        else:
            attempts+=1
            corans+=1
        os.system('cls')
    
    #end game
    print "Number of questions:",qno
    print "Number of correct answers:",corans
    print "Number of attempts:",attempts
    
    class MyFirstGUI:
        def __init__(self, master):
            self.master = master
            master.title("End of Round")
    
            self.label = Label(master, text="Do you want to play again?")
            self.label.pack()
    
            self.greet_button = Button(master, text="Play Again", command=self.again)
            self.greet_button.pack()
    
            self.close_button = Button(master, text="Menu", command=self.menu)
            self.close_button.pack()
    
        def again(self):
            self.master.destroy()
            alpha()
        
        def menu(self):
            self.master.destroy()
            menu()

    root = Tk()
    my_gui = MyFirstGUI(root)
    w = 400 # width for the Tk root
    h = 200 # height for the Tk root
    
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    
    # set the dimensions of the screen 
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.mainloop()
#end of main function

def menu():
    class MenuGUI:
        def __init__(self, master):
            self.master = master
            master.title("Welcome")
    
            self.label = Label(master, text="Level Select")
            self.label.pack()
    
            self.greet_button = Button(master, text="Level 1: Addition & Subtraction up to 10", command=self.alpha)
            self.greet_button.pack()
    
            self.close_button = Button(master, text="Quit", command=self.quit)
            self.close_button.pack()
    
        def alpha(self):
            self.master.destroy()
            alpha()
        def quit(self):
            self.master.destory()
            quit()
            
    root = Tk()
    my_gui = MenuGUI(root)
    w = 400 # width for the Tk root
    h = 200 # height for the Tk root
    
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    
    # set the dimensions of the screen 
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.mainloop()
    root.attributes("-topmost", True)
    
menu()