from tkinter import *

def tinh():
    s = string14.get()
    # B1: Nhân đôi giá trị của những số ở vị trí lẻ (là các số ở vị trí 1, 3, 5,...,13),
    # trong đó số thứ 1 là số ngoài cùng phía bên phải của chuỗi số IMEI
    a = ''
    if len( s ) == 14:
        for j in range( 1, 8 ):
            aj = str( int( s[15 - 2 * j] ) * 2 )
            a = a + aj

        n = len( a )
        tong1 = 0
        for i in range( 0, n ):
            tong1 = tong1 + int( a[i] )

        # B2: Cộng dồn tất cả các chữ số riêng rẽ của các số thu được ở bước 1,
        # cùng với các số ở vị trí chẵn (là các số ở vị trí 2, 4, 6 ... 14) trong chuỗi số IMEI
        tong = int( s[12] ) + int( s[10] ) + int( s[8] ) + int( s[6] ) + int( s[4] ) + int( s[2] ) + int( s[0] ) + tong1
        if tong % 10 == 0:
            socuoi = 0
        else:
            socuoi = 10 - (tong % 10)
        string15.set(socuoi)
        string15full.set(s+str(socuoi))
    else:
       string15.set( "Số IMEI nhập vào không hợp lệ!!!" )



root = Tk()

string14= StringVar()
string15= StringVar()
string15full= StringVar()

root.title("Last digit of IMEI:")
root.resizable(height=TRUE, width=TRUE)
root.minsize(height=50,width=400)

Label(root, text="IMEI checked by Ken", fg= "red", font = ("tohama",16), justify= CENTER ).grid(row= 0, columnspan =2)
Label(root,text="Input 14 first digits of IMEI number: ", justify= RIGHT).grid(row=1, column = 0)
Entry(root, width =30, textvariable = string14).grid(row=1, column=1)
Label(root, text="Last digit of IMEI number: ", justify= RIGHT).grid(row = 2, column = 0)
Entry(root, width = 30, textvariable = string15).grid(row=2, column =1)

frameButton = Frame()
Button(frameButton, text= "Check", command = tinh).pack(side = LEFT)
Button(frameButton, text= "Exit", command = root.quit).pack(side = LEFT)
frameButton.grid(row = 3, columnspan=2)

Label(root, text="Right IMEI number: ", justify= RIGHT).grid(row = 4, column = 0)
Entry(root, width = 30, textvariable = string15full).grid(row=4, column =1)

def makecenter(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_width()
    x = (root.winfo_screenwidth()//2) - (width//2)
    y = (root.winfo_screenheight()//2) - (height//2)
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
makecenter(root)

root.mainloop()
#Sửa rồi nè


