from tkinter import Tk, Label, Frame

from rx.subjects import Subject
from rx.concurrency import TkinterScheduler


def main():
    root = Tk()
    root.title("Rx for Python rocks")
    scheduler = TkinterScheduler(root)

    mousemove = Subject()

    frame = Frame(root, width=600, height=600)

    def move(event):
        mousemove.on_next(event)
    frame.bind("<Motion>", move)

    text = 'TIME FLIES LIKE AN ARROW'
    labels = [Label(frame, text=c) for c in text]

    def handle_label(i, label):
        label.config(dict(borderwidth=0, padx=0, pady=0))

        def on_next(ev):
            label.place(x=ev.x + i*12 + 15, y=ev.y)
        ys = mousemove.delay(i*100).subscribe_(on_next, scheduler=scheduler)

    for i, label in enumerate(labels):
        handle_label(i, label)

    frame.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
