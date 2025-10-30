import tkinter as tk
import random

TIPS = [
    '我想你了', '今天过得开心吗', '想和你见面', '顺顺利利',
    '早点休息', '天冷了，多穿衣服', '今天有想我吗'
]
COLORS = [
    'pink', 'skyblue', 'green', 'lavender', 'lightyellow',
    'plum', 'coral', 'bisque', 'lightblue', 'oldlace'
]

WIN_W, WIN_H = 300, 100

def popup(root):
    # 新建一个子窗口
    win = tk.Toplevel(root)
    win.title("宝宝")
    win.attributes("-topmost", True)   # 总在最前，可去掉
    # 计算随机位置（不越界）
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    x = random.randint(0, max(0, sw - WIN_W))
    y = random.randint(0, max(0, sh - WIN_H))
    win.geometry(f"{WIN_W}x{WIN_H}+{x}+{y}")

    tip = random.choice(TIPS)
    bg = random.choice(COLORS)

    tk.Label(
        win,
        text=tip,
        font=("微软雅黑", 14, "bold"),
        bg=bg,
        fg="black"
    ).pack(expand=True, fill="both")

    # 2.5 秒后自动关闭（仍在主线程）
    win.after(10000, win.destroy)

def schedule_next(root):
    popup(root)
    # 5 ~ 15 秒后再弹一次
    delay_ms = int(random.uniform(0.1, 0.5) * 1000)
    root.after(delay_ms, lambda: schedule_next(root))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()               # 隐藏主窗口，只显示弹窗
    schedule_next(root)           # 启动循环
    root.mainloop()
