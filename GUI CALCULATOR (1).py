import tkinter
from tkinter import scrolledtext
import keyboard

window=tkinter.Tk()
window.title("CALCULATOR")
window.geometry("800x600")
window.configure( bg="#181B1F")

  

#CREATING FUNCTIONS FOR BUTTONS
num_list2=[] #this is for display along with sign
state=False
op_list=["+","-","x","÷","="]
op_state=False
def entry():
    output=field.get()
    return output


def button_val(num):
    global state,op_state
    a=entry()

    if  state==True:
        field.delete(0,"end")
        field.insert("end",num)
        state=False
    else:
        a=entry()
        if len(a)<=10:
            field.insert("end",num)
            
        else:
            pass
    op_state=True
total=0
def add():
    global total,op_state
    global state
    last=laststep()
    if last=="=":
        a=float(entry())
        num_list2.clear()
        sym("+",a)
        total=a
    elif last=='-' or last=='÷' or last=='x':
        a=float(entry())
        num_list2.pop(-1)
        num_list2.append("+")
        b=concatenate_list_data(num_list2)
        list_label=tkinter.Label(entry_frame,width=5,text=f'{b}',fg="white", bg="#25282B")
        list_label.grid(row=0,column=0,sticky="nsew")


    else:
        if op_state==True:
            a=float(entry())
            sym('+',a)
            total=total+a
            field.delete(0,"end")
            field.insert("end",total)
        else:
            pass
    state=True
    op_state=False
    

    

def sub():
    
    global state
    global total,op_state,num_list2
    last = laststep()    
    if last == '=':
        
        a = float(entry())
        num_list2.clear()
        sym('-',a)
    elif last=='+' or last=='÷' or last=='x':
        a=float(entry())
        num_list2.pop(-1)
        num_list2.append("-")
        b=concatenate_list_data(num_list2)
        list_label=tkinter.Label(entry_frame,width=5,text=f'{b}',fg="white", bg="#25282B")
        list_label.grid(row=0,column=0,sticky="nsew")
    else:
        if op_state==True:
            a =int(entry())
            sym('-',a)
            if total<0 or total>0:
                total=total-a
                field.delete(0,"end")
                field.insert("end",total)
               
            else: 
                if len(num_list2)==2:
                    total=a-total
                    field.delete(0,"end")
                    field.insert("end",total)
                else:
                    total=total-a
                    field.delete(0,"end")
                    field.insert("end",total)
        else:
            pass


    state=True
    op_state=False

def mul():  #FUNCTION FOR MULTIPLICATION
    global state,op_state,total
    last=laststep()
    if last=="=":
        a=float(entry())
        num_list2.clear()
        sym("x",a)
        total=a
    elif last=='+' or last=='÷' or last=='-':
        a=float(entry())
        num_list2.pop(-1)
        num_list2.append("x")
        b=concatenate_list_data(num_list2)
        list_label=tkinter.Label(entry_frame,width=5,text=f'{b}',fg="white", bg="#25282B")
        list_label.grid(row=0,column=0,sticky="nsew")

    else:
        if op_state==True:
            if total==0:
                a=float(entry())
                sym("x",a)
                total=a
                field.delete(0,"end")
                field.insert("end",total)
            else:
                a=float(entry())
                sym("x",a)
                total=total*a
                field.delete(0,"end")
                field.insert("end",total)
        else:
            pass
    op_state=False
    state=True

def div():
    global state,op_state,total
    last=laststep()
    if last=="=":
        a=float(entry())
        num_list2.clear()
        sym("÷",a)
        total=a
    elif last=='+' or last=='-' or last=='x':
        a=float(entry())
        num_list2.pop(-1)
        num_list2.append("÷")
        b=concatenate_list_data(num_list2)
        list_label=tkinter.Label(entry_frame,width=5,text=f'{b}',fg="white", bg="#25282B")
        list_label.grid(row=0,column=0,sticky="nsew")

    else:
        if op_state==True:
            if total==0:
                a=float(entry())
                sym("÷",a)
                total=a    
                field.delete(0,"end")
                field.insert("end",round(total,2))
            else:
                a=float(entry())
                sym("÷",a)
                total=total/a
                field.delete(0,"end")
                field.insert("end",round(total,2))
        else:
            pass
    op_state=False
    state=True


def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result
    
def sym(ele,out):
    
    num_list2.append(out) 
    num_list2.append(ele)
    print ((num_list2))
    a=concatenate_list_data(num_list2)
    list_label=tkinter.Label(entry_frame,width=5,text=f'{a}',fg="white", bg="#25282B")
    list_label.grid(row=0,column=0,sticky="nsew")
    
    
  
# function to check what is the last operation

def laststep():
    global op_list,num_list2
    for i in reversed(range(len(num_list2))):
        if num_list2[i] in op_list:
            return num_list2[i]
            break

        else:
            pass
        

# fucntion to check what is the operation before = 
def before_eq():
    global op_list,num_list2
    return num_list2[-3]
    

def hist(): #this is equals function
    global num_list2,total,state
    last=laststep()
    a=float(entry())
    if last=="+":
        sym("=",a)
        total=total+a
        field.delete(0,"end")
        field.insert("end",total)
        history_list.configure(state="normal")
        history_list.insert("end",num_list2, 'justified')
        history_list.insert("end",'\n', 'justified')
        history_list.insert("end",total, 'justified')
        history_list.insert("end",'\n', 'justified')
        history_list.configure(state="disabled")
        state=True

    elif last=='-':
        sym("=",a)
        if total<0 or total>0:
            total=total-a
            field.delete(0,"end")
            field.insert("end",total)
            history_list.insert("end",num_list2, 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.insert("end",total, 'justified')
            history_list.insert("end",'\n', 'justified')
            state=True

    
        else:
            if len(num_list2)==2:
                total=a-total
                field.delete(0,"end")
                field.insert("end",total)
                history_list.configure(state="normal")
                history_list.insert("end",num_list2, 'justified')
                history_list.insert("end",'\n', 'justified')
                history_list.insert("end",total, 'justified')
                history_list.insert("end",'\n', 'justified')
                history_list.configure(state="disabled")
                state=True
            else:
                total=total-a
                field.delete(0,"end")
                field.insert("end",total)
                history_list.insert("end",num_list2, 'justified')
                history_list.insert("end",'\n', 'justified')
                history_list.insert("end",total, 'justified')
                history_list.insert("end",'\n', 'justified')
                state=True
    elif last=="x":
        sym("=",a)
        if total==0:
            total=a
            field.delete(0,"end")
            field.insert("end",total)
            history_list.insert("end",num_list2, 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.insert("end",total, 'justified')
            history_list.insert("end",'\n', 'justified')
            state=True
        else:
            total=total*a
            field.delete(0,"end")
            field.insert("end",total)
            history_list.configure(state="normal")
            history_list.insert("end",num_list2, 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.insert("end",total, 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.configure(state="disabled")
            state=True
    elif last=='÷':
        sym("=",a)
        if total==0:
            total=a    
            field.delete(0,"end")
            field.insert("end",round(total,2))
            history_list.configure(state="normal")
            history_list.insert("end",num_list2, 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.insert("end",round(total,2), 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.configure(state="disabled")
            state=True
        else:
            total=total/a
            field.delete(0,"end")
            field.insert("end",round(total,2))
            history_list.configure(state="normal")
            history_list.insert("end",num_list2, 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.insert("end",round(total,2), 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.configure(state="disabled")
            state=True
    else:
        pass

    #we will check if last operation was = or not
    # If last operation was = then we will check what operation was
    #before that 
    
    if last=="=":
        before=before_eq()
        if before=='+':
            num_list2=[total,"+",num_list2[-2],"="]

            a=concatenate_list_data(num_list2)
            list_label=tkinter.Label(entry_frame,width=5,text=f'{a}',fg="white", bg="#25282B")
            list_label.grid(row=0,column=0,sticky="nsew")

            total=total+num_list2[-2]
            field.delete(0,"end")
            field.insert("end",total)
            history_list.configure(state="normal")
            history_list.insert("end",num_list2, 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.insert("end",total, 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.configure(state="disabled")
            state=True
        if before == '-':
            num_list2 = [total,'-',num_list2[-2],'=']

            a=concatenate_list_data(num_list2)
            list_label=tkinter.Label(entry_frame,width=5,text=f'{a}',fg="white", bg="#25282B")
            list_label.grid(row=0,column=0,sticky="nsew")

            if total<0:
                total=total-num_list2[-2]
                field.delete(0,"end")
                field.insert("end",total)
                history_list.configure(state="normal")
                history_list.insert("end",num_list2, 'justified')
                history_list.insert("end",'\n', 'justified')
                history_list.insert("end",total, 'justified')
                history_list.insert("end",'\n', 'justified')
                history_list.configure(state="disabled")
                state=True
            elif total>0:
                total=total-num_list2[-2]
                field.delete(0,"end")
                field.insert("end",total)
                history_list.configure(state="normal")
                history_list.insert("end",num_list2, 'justified')
                history_list.insert("end",'\n', 'justified')
                history_list.insert("end",total, 'justified')
                history_list.insert("end",'\n', 'justified')
                history_list.configure(state="disabled")
                state=True
            elif total==0:
                total=total-num_list2[-2]
                field.delete(0,"end")
                field.insert("end",total)
                history_list.configure(state="normal")
                history_list.insert("end",num_list2, 'justified')
                history_list.insert("end",'\n', 'justified')
                history_list.insert("end",total, 'justified')
                history_list.insert("end",'\n', 'justified')
                history_list.configure(state="disabled")
                state=True
            else:
        
               pass
        if before=="x":
            num_list2=[total,"x",num_list2[-2],"="]
            a=concatenate_list_data(num_list2)
            list_label=tkinter.Label(entry_frame,width=5,text=f'{a}',fg="white", bg="#25282B")
            list_label.grid(row=0,column=0,sticky="nsew")
            
            total=total*num_list2[-2]
            field.delete(0,"end")
            field.insert("end",total)
            history_list.configure(state="normal")
            history_list.insert("end",num_list2, 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.insert("end",total, 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.configure(state="disabled")
            state=True
        if before=="÷":
            num_list2=[round(total,2),"÷",num_list2[-2],"="]
            a=concatenate_list_data(num_list2)
            list_label=tkinter.Label(entry_frame,width=5,text=f'{a}',fg="white", bg="#25282B")
            list_label.grid(row=0,column=0,sticky="nsew")
            
            total=total/num_list2[-2]
            field.delete(0,"end")
            field.insert("end",round(total,2))
            history_list.configure(state="normal")
            history_list.insert("end",num_list2, 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.insert("end",round(total,2), 'justified')
            history_list.insert("end",'\n', 'justified')
            history_list.configure(state="disabled")
            state=True

    else:
        pass

def c():
    global total,num_list2,state
    total=0
    num_list2.clear()
    field.delete(0,"end")
    field.insert("end",total)
    a=concatenate_list_data(num_list2)
    list_label=tkinter.Label(entry_frame,width=5,text=f'{a}',fg="white", bg="#25282B")
    list_label.grid(row=0,column=0,sticky="nsew")
    state=True

def ce():
    global total,num_list2,state
    total=0
    history_list.delete(1.0,"end")
    num_list2.clear()
    field.delete(0,"end")
    field.insert("end",total)
    a=concatenate_list_data(num_list2)
    list_label=tkinter.Label(entry_frame,width=5,text=f'{a}',fg="white", bg="#25282B")
    list_label.grid(row=0,column=0,sticky="nsew")
    state=True

def negate():
    global total,state
    
    if total==0:
        a=float(entry())
        total=0-a
        field.delete(0,"end")
        field.insert("end",total)
    else:
        total=0-total
        field.delete(0,"end")
        field.insert("end",total)
    state=True


def back():
    global state
    field.delete(0)
    state=True



#configuring row and columns of main window
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

#create left and right frames
left=tkinter.Frame(window,height=190,width=200)
right=tkinter.Frame(window,height=190,width=400,bg="black")
left.grid(row=0,column=0,sticky="NSEW")
right.grid(row=0,column=1,sticky="NS")

#configuring row and columns of left frame
left.rowconfigure(0,weight=1)
left.columnconfigure(0,weight=1)
left.rowconfigure(1,weight=5)

#creating frames for entry and button 
entry_frame=tkinter.Frame(left,height=200,width=5)
entry_frame.grid(row=0,column=0,sticky="NwsE")
button_frame=tkinter.Frame(left,height=200,width=5,bg="red")
button_frame.grid(row=1,column=0,sticky="nsew")

#configuring button frame rows and columns
button_frame.rowconfigure((0,1,2,3,4),weight=1)
button_frame.columnconfigure((0,1,2,3),weight=1)

#creating buttons in button_frame row=0
b_mod=tkinter.Button(button_frame,text="C",command=c,relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b_mod.grid(row=0,column=0,sticky="nsew")
b_square=tkinter.Button(button_frame,text="CE",command=ce,relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b_square.grid(row=0,column=1,sticky="nsew")
b_ac=tkinter.Button(button_frame,text="÷",command= div,relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b_ac.grid(row=0,column=2,sticky="nsew")
b_div=tkinter.Button(button_frame,text="«",command=back,relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b_div.grid(row=0,column=3,sticky="nsew")

#creating buttons in button_frame row=1
b7=tkinter.Button(button_frame,text="7",command= lambda : button_val(7),relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b7.grid(row=1,column=0,sticky="nsew")
b8=tkinter.Button(button_frame,text="8",command= lambda : button_val(8),relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b8.grid(row=1,column=1,sticky="nsew")
b9=tkinter.Button(button_frame,text="9",command= lambda : button_val(9),relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b9.grid(row=1,column=2,sticky="nsew")
b_mul=tkinter.Button(button_frame,text="x",command= mul,relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b_mul.grid(row=1,column=3,sticky="nsew")

#creating buttons in button_frame row=2
b4=tkinter.Button(button_frame,text="4",command= lambda : button_val(4),relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b4.grid(row=2,column=0,sticky="nsew")
b5=tkinter.Button(button_frame,text="5",command= lambda : button_val(5),relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b5.grid(row=2,column=1,sticky="nsew")
b6=tkinter.Button(button_frame,text="6",command= lambda : button_val(6),relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b6.grid(row=2,column=2,sticky="nsew")
b_min=tkinter.Button(button_frame,text="-",command= sub,relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b_min.grid(row=2,column=3,sticky="nsew")

#creating buttons in button_frame row=4
b00=tkinter.Button(button_frame,text="+/-",command= negate,relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b00.grid(row=4,column=0,sticky="nsew")
b0=tkinter.Button(button_frame,text="0",command= lambda : button_val(0),relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b0.grid(row=4,column=1,sticky="nsew")
bdot=tkinter.Button(button_frame,text=".",command= lambda : button_val("."),relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
bdot.grid(row=4,column=2,sticky="nsew")
b_equal=tkinter.Button(button_frame,text="=",command= hist,relief="flat",fg="white", bg="#b31b1b",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b_equal.grid(row=4,column=3,sticky="nsew")

#creating buttons in button_frame row=3
b1=tkinter.Button(button_frame,text="1",command= lambda : button_val(1),relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b1.grid(row=3,column=0,sticky="nsew")
b2=tkinter.Button(button_frame,text="2",command= lambda : button_val(2),relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b2.grid(row=3,column=1,sticky="nsew")
b3=tkinter.Button(button_frame,text="3",command= lambda : button_val(3),relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b3.grid(row=3,column=2,sticky="nsew")
b_plus=tkinter.Button(button_frame,text="+",command= add,relief="flat",fg="white", bg="#181B1F",font=("Microsoft Yi Baiti bold",15),activebackground="#666666")
b_plus.grid(row=3,column=3,sticky="nsew")

Warn=tkinter.Label(window,text="The creator of this calculator tried to make it similar to calculator in MICROSOFT WINDOWS 10. \n Creator: S A U R A B H  K H A R E ",fg="white", bg="#181B1F")
Warn.grid(row=1,columnspan=2)
#configuring row and column of entry_frame
entry_frame.rowconfigure(0,weight=2)
entry_frame.rowconfigure(1,weight=1)
entry_frame.columnconfigure(0,weight=1)

#creating entry box in entry_frame XXXXXXX 
field=tkinter.Entry(entry_frame,width=5,font=("Times new roman",30),fg="white", bg="#25282B",relief="flat",justify="right")
field.grid(row=1,column=0,sticky="nsew")


#entering blank label in left side
list_label=tkinter.Label(entry_frame,width=5,text=" ",fg="white", bg="#25282B")
list_label.grid(row=0,column=0,sticky="nsew")

    
    
#configuring row and column of right frame
right.rowconfigure(0,weight=1)
right.columnconfigure(0,weight=1)
right.rowconfigure(1,weight=5)

#dividing right frame into two parts 1> History 2>History shower
#creating history in rightframe
#right.grid(row=0,column=1,sticky="NS")
History=tkinter.Frame(right,height=200,width=400, bg="#25282B")
History.grid(row=0,column=0,sticky="NwsE")
History_frame=tkinter.Frame(right,height=280,width=5)
History_frame.grid(row=1,column=0,sticky="nsew")

#Creating history label in History and also configuring row and column of history frame
History.rowconfigure(0,weight=1)
History.columnconfigure(0,weight=1)
label=tkinter.Label(History,text="H I S T O R Y",font=("audrey",15),fg="white", bg="#25282B")
label.grid(row=0,column=0)

#creating listbox in History_frame
History_frame.rowconfigure(0,weight=1)
History_frame.columnconfigure(0,weight=1)
#history_list=tkinter.Listbox(History_frame,width=20,height=18,bg="#F0F0F0",relief="flat")

history_list = tkinter.scrolledtext.ScrolledText(History_frame, width = 30, height=12, bg="#25282B", fg="white",wrap="word",font=("times new roman",15),relief="flat")
history_list.tag_config('justified', justify="right")
#history_list.configure(justify="right")
history_list.grid(row=0,column=0,sticky="nse")

# This checks if entered value is integer or not
a=entry()
if a.isdigit():
    field.insert("end",a)
else:
    pass
#___________________________________________________________________
#on hover
def changeOnHover(button, colorOnHover, colorOnLeave): 
  
    # adjusting backgroung of the widget 
    # background on entering widget 
    button.bind("<Enter>", func=lambda e: button.config( 
        background=colorOnHover)) 
  
    # background color on leving widget 
    button.bind("<Leave>", func=lambda e: button.config( 
        background=colorOnLeave)) 

changeOnHover(b1, "#3b444b", "#181B1F")
changeOnHover(b_mod, "#3b444b", "#181B1F")
changeOnHover(b_square, "#3b444b", "#181B1F")
changeOnHover(b_ac, "#3b444b", "#181B1F")
changeOnHover(b_div, "#3b444b", "#181B1F")
changeOnHover(b7, "#3b444b", "#181B1F")
changeOnHover(b9, "#3b444b", "#181B1F")
changeOnHover(b_mul, "#3b444b", "#181B1F")
changeOnHover(b4, "#3b444b", "#181B1F")
changeOnHover(b5, "#3b444b", "#181B1F")
changeOnHover(b6, "#3b444b", "#181B1F")
changeOnHover(b_min, "#3b444b", "#181B1F")
changeOnHover(b00, "#3b444b", "#181B1F")
changeOnHover(b0, "#3b444b", "#181B1F")
changeOnHover(bdot, "#3b444b", "#181B1F")
changeOnHover(b_equal, "#3b444b", "#b31b1b")
changeOnHover(b2, "#3b444b", "#181B1F")
changeOnHover(b3, "#3b444b", "#181B1F")
changeOnHover(b_plus, "#3b444b", "#181B1F")
#____________________________________________________________________
#creating bind buttons
window.bind('<Return>',lambda event : hist())
window.bind('<BackSpace>',lambda event : back())
window.bind('<Escape>',lambda event : c())
window.bind('1',lambda event : button_val(1))
window.bind('2',lambda event : button_val(2))
window.bind('3',lambda event : button_val(3))
window.bind('4',lambda event : button_val(4))
window.bind('5',lambda event : button_val(5))
window.bind('6',lambda event : button_val(6))
window.bind('7',lambda event : button_val(7))
window.bind('8',lambda event : button_val(8))
window.bind('9',lambda event : button_val(9))
window.bind('0',lambda event : button_val(0))
window.bind('+',lambda event : add())
window.bind('-',lambda event : sub())
window.bind('*',lambda event : mul())
window.bind('/',lambda event : div())

#_____________________________________________________________________
#creating bind buttons to change bg

window.mainloop()

