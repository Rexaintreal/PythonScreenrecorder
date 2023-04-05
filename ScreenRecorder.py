import tkinter
import customtkinter
import pyautogui
import numpy
import cv2
import sys

class Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)




class Application(customtkinter.CTk):

    def start_recording(self):
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        fps = 60
        out = cv2.VideoWriter('output.mp4', fourcc, fps, (self.ScreenSize))
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Live", 480, 270)
        while self.Config:
            img = pyautogui.screenshot()
            frame = numpy.array(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            out.write(frame)
            cv2.imshow('Live', frame)
            if cv2.waitKey(1) == ord('q'):
                break

        out.release()
        cv2.destroyAllWindow()

    def stop_recording(self):
        sys.exit()

    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.title("ScreenRecorder")
        self.minsize(width=640, height=480)
        self.maxsize(width=640, height=480)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = Frame(master=self, )
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.lable = customtkinter.CTkLabel(master=self,
                                             text="ScreenRecorder",
                                             width=120,
                                             height=25,
                                             text_color="White",
                                             font=("", 30),
                                             corner_radius=8)
        self.lable.place(relx=0.50, rely=0.15, anchor=tkinter.CENTER)
        self.Record = customtkinter.CTkButton(master=self,
                                              width=120,
                                              height=32,
                                              border_width=0,
                                              corner_radius=8,
                                              font=("",24),
                                              text="Start Recording",
                                              command=self.start_recording
                                              )

        self.Record.place(relx=0.50, rely=0.47, anchor=tkinter.CENTER)
        self.Stop = customtkinter.CTkButton(master=self,
                                              width=120,
                                              height=32,
                                              border_width=0,
                                              corner_radius=8,
                                              font=("", 24),
                                              text="Stop Recording",
                                              command=self.stop_recording)

        self.Stop.place(relx=0.50, rely=0.60, anchor=tkinter.CENTER)
        self.ScreenSize=tuple(pyautogui.size())
        self.Config=True




application = Application()

application.mainloop()
