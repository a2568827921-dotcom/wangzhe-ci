import tkinter as tk
import random

root = tk.Tk()

root.attributes("-fullscreen", True)
root.configure(bg="black")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()

canvas = tk.Canvas(
    root,
    width=w,
    height=h,
    bg="black",
    highlightthickness=0
)

canvas.pack()


texts = []

running = True


colors = [
    "#ff0000",
    "#ff5555",
    "#ffffff",
    "#00ff00"
]


# 初始渲染
for i in range(3):

    x = random.randint(0,w)
    y = random.randint(0,h)

    t = canvas.create_text(
        x,y,
        text="王喆",
        fill="red",
        font=("PingFang SC",80,"bold")
    )

    texts.append(t)



def spread():

    if not running:
        return


    new=[]

    for t in texts[:]:

        pos = canvas.coords(t)

        if pos:

            x,y=pos

            for i in range(2):

                nx=x+random.randint(-220,220)
                ny=y+random.randint(-220,220)

                nx=max(0,min(w,nx))
                ny=max(0,min(h,ny))


                obj=canvas.create_text(
                    nx,
                    ny,
                    text="王喆",
                    fill=random.choice(colors),
                    font=(
                        "PingFang SC",
                        random.randint(30,90),
                        "bold"
                    )
                )

                new.append(obj)


    texts.extend(new)


    if len(texts)>600:
        canvas.delete(texts.pop(0))


    root.after(300,spread)



spread()



# 密码退出

def ask_password(event=None):

    global running

    win=tk.Toplevel(root)

    win.title("系统警告")
    win.geometry("300x150")

    tk.Label(
        win,
        text="请输入清除密码",
        font=("PingFang SC",16)
    ).pack(pady=10)


    entry=tk.Entry(
        win,
        show="*"
    )

    entry.pack()


    def check():

        global running

        if entry.get()=="666":

            running=False

            win.destroy()

            clear_animation()


    tk.Button(
        win,
        text="确认",
        command=check
    ).pack(pady=10)



def clear_animation():

    canvas.delete("all")


    msg=canvas.create_text(
        w/2,
        h/2,
        text="王喆病毒正在清除...",
        fill="white",
        font=(
            "PingFang SC",
            60,
            "bold"
        )
    )


    def finish():

        canvas.itemconfig(
            msg,
            text="✓  系统恢复正常\n\n感谢体验王喆病毒"
        )

        root.after(
            2500,
            root.destroy
        )


    root.after(
        2000,
        finish
    )



root.bind(
    "<Escape>",
    ask_password
)


root.mainloop()
