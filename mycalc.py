from tkinter import *

window = None
show_result = ''
act_result = ''
display_label = None

def press_num(num):
    global act_result
    global show_result
    show_result += num
    act_result += num
    display_label['text'] = show_result

def press_alu(alu):
    global act_result
    global show_result

    if alu == '8':
        show_result += '×'
    elif alu == '/':
        show_result += '÷'
    elif alu == 'ㆍ':
        show_result += '.'
    else:
        show_result += alu

    act_result += alu
    display_label['text'] = show_result

def press_result():
    global act_result
    global show_result
    try:
        act_result = str(eval(act_result))
        if len(act_result) > 15:
            act_result = act_result[:15]
        display_label['text'] = act_result
        show_result = ''
        act_result = ''

    except:
        display_label['text'] = 'ERROR'
        act_result = ''
        show_result = ''

def press_c():
    global act_result
    global show_result
    display_label['text'] = '0'
    act_result = ''
    show_result = ''

def press_erase():
    global act_result
    global show_result

    act_result = act_result[:len(act_result)-1]
    show_result = show_result[:len(show_result)-1]

    if show_result == '':
        display_label['text'] = '0'
    else:
        display_label['text'] = show_result

def press_percent():
    global act_result
    global show_result

    act_result += ' * 0.01'
    show_result += ' × 0.01'

    display_label['text'] = show_result

def press_pow():
    global act_result
    global show_result

    act_result += ' ** 2'
    show_result += ' ^ 2'

    display_label['text'] = show_result

def setupGUI():
    global window
    global display_label
    global show_result
    global act_result

    window = Tk()
    window.title('Calculator')
    window.resizable(False, False)

    display_label = Label(window, text = '', relief = SUNKEN, anchor = 'e', width = 15, font = 'Arial 20')
    display_label.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

    btn1 = Button(window, text = '1', font = 'Arial15', width = 5, height = 2, command = lambda: press_num('1'), bg = 'orange')
    btn2 = Button(window, text='2', font='Arial15', width=5, height=2, command=lambda: press_num('2'), bg = 'orange')
    btn3 = Button(window, text='3', font='Arial15', width=5, height=2, command=lambda: press_num('3'), bg = 'orange')
    btn4 = Button(window, text='4', font='Arial15', width=5, height=2, command=lambda: press_num('4'), bg = 'orange')
    btn5 = Button(window, text='5', font='Arial15', width=5, height=2, command=lambda: press_num('5'), bg = 'orange')
    btn6 = Button(window, text='6', font='Arial15', width=5, height=2, command=lambda: press_num('6'), bg = 'orange')
    btn7 = Button(window, text='7', font='Arial15', width=5, height=2, command=lambda: press_num('7'), bg = 'orange')
    btn8 = Button(window, text='8', font='Arial15', width=5, height=2, command=lambda: press_num('8'), bg = 'orange')
    btn9 = Button(window, text='9', font='Arial15', width=5, height=2, command=lambda: press_num('9'), bg = 'orange')
    btn0 = Button(window, text='0', font='Arial15', width=5, height=2, command=lambda: press_num('0'), bg = 'orange')

    btn_p = Button(window, text='+', font = 'Arial15', width = 5, height = 2, command = lambda: press_alu('+'), bg = 'skyblue')
    btn_s = Button(window, text='-', font='Arial15', width=5, height=2, command=lambda: press_alu('-'), bg = 'skyblue')
    btn_m = Button(window, text='×', font='Arial15', width=5, height=2, command=lambda: press_alu('*'), bg = 'skyblue')
    btn_d = Button(window, text='÷', font='Arial15', width=5, height=2, command=lambda: press_alu('/'), bg = 'skyblue')
    btn_point = Button(window, text = 'ㆍ', font = 'Arial15', width = 5, height = 2, command = lambda: press_alu('.'), bg = 'orange')

    btn_res = Button(window, text = '=', font = 'Arial15', width = 5, height = 2, command = press_result, bg = 'orange')

    btn_C = Button(window, text = 'C', font = 'Arial15', width = 5, height = 1, command = press_c, fg = 'red', bg = 'skyblue')
    btn_E = Button(window, text = '＜', font = 'Arial15', width = 5, height = 1, command = press_erase, bg = 'skyblue')
    btn_per = Button(window, text = '％', font = 'Arial15', width = 5, height = 1, command = press_percent, bg = 'skyblue')
    btn_pow = Button(window, text = 'X²', font = 'Arial15', width = 5, height = 1, command = press_pow, bg = 'skyblue')

    btn_C.grid(row = 1, column = 0)
    btn_E.grid(row = 1, column = 1)
    btn_per.grid(row = 1, column = 2)
    btn_pow.grid(row = 1, column = 3)
    btn1.grid(row = 2, column = 0)
    btn2.grid(row=2, column = 1)
    btn3.grid(row = 2, column = 2)
    btn_p.grid(row = 2, column = 3)
    btn4.grid(row = 3, column = 0)
    btn5.grid(row = 3, column = 1)
    btn6.grid(row = 3, column = 2)
    btn_s.grid(row = 3, column = 3)
    btn7.grid(row = 4, column = 0)
    btn8.grid(row = 4, column = 1)
    btn9.grid(row = 4, column = 2)
    btn_m.grid(row = 4, column = 3)
    btn_point.grid(row = 5, column = 0)
    btn0.grid(row = 5, column = 1)
    btn_res.grid(row = 5, column = 2)
    btn_d.grid(row = 5, column = 3)

setupGUI()
window.mainloop()