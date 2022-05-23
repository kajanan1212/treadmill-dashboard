from tkinter import *
import math
from tkinter import messagebox


def speed_(RPM, RADIUS):
    # SPEED CALCULATION
    _speed_ = ((2 * math.pi * RPM) / 60) * (RADIUS)
    return _speed_


def convertInto_m(length, unit):
    # GET LENGTH IN m or cm or inch AND CONVERT INTO m
    if unit == 'm':
        _LENGTH_ = float(length)
    elif unit == 'cm':
        _LENGTH_ = float(length) / 100
    else:
        _LENGTH_ = float(length) * 0.0254
    return _LENGTH_


def convertInto_kg(mass, unit):
    # GET THE WEIGHT FROM USER IN kg or lb AND CONVERT INTO kg
    if unit == 'kg':
        _weight_ = float(mass)
    else:
        _weight_ = float(mass) * 0.453592
    return _weight_


def convertFrom_m(length, unit):
    # CONVERT FROM m
    if unit == 'm':
        _LENGTH_ = float(length)
    else:
        _LENGTH_ = float(length) * 0.001
    return _LENGTH_


def convertFrom_mps(speed, unit):
    # CONVERT FROM mps
    if unit == 'mps':
        _SPEED_ = float(speed)
    else:
        _SPEED_ = float(speed) * 3.6
    return _SPEED_


def distance_(speed, TIME):
    # DISTANCE CALCULATION
    distance__ = speed * TIME
    return distance__


def calcMet(speed):
    # MET CALCULATION
    if speed > 1.65405:  # 1.65405 ms-1 = 3.7 mph
        _MET_ = (0.2 * speed * 60) + (1.8 * speed * 0.01) + 3.5
    else:
        _MET_ = (0.1 * speed * 60) + (0.9 * speed * 0.01) + 3.5
    return _MET_


def calories_burnt(MET, weight, TIME):
    # CALORIES CALCULATION
    caloriesburnt_ = (MET * weight * 3.5) / 200 * TIME / 60
    return caloriesburnt_


def step_taken(stride_length, height, distance):
    # NUMBER OF STEP TAKEN
    steptaken_ = distance / (stride_length * height)
    return steptaken_


def calculate_display():
    global TIME
    global speed
    global distance
    global MET
    global caloriesburnt
    global steptaken

    if isReset:
        # Calculation part
        speed = speed_(rpm, radius)
        distance = distance_(speed, TIME)
        MET = calcMet(speed)
        caloriesburnt = calories_burnt(MET, weight, TIME)
        steptaken = step_taken(stride_length, height, distance)

        TIME += 1

        # display the current values
        # speed
        outputLabelSpeed = Label(bottomFrame, width=10, text="%8.2f" % convertFrom_mps(speed, unitSpeed.get()),
                                 font=("digital7", 20, "bold"), bg="DarkSlateGray3", fg="RoyalBlue4")
        outputLabelSpeed.grid(row=0, column=1)
        # distance
        outputLabelDistance = Label(bottomFrame, width=10, text="%8.3f" % convertFrom_m(distance, unitDistance.get()),
                                    font=("digital7", 20, "bold"), bg="DarkSlateGray3", fg="RoyalBlue4")
        outputLabelDistance.grid(row=1, column=1)
        # caloriesburnt
        outputLabelCaloriesburnt = Label(bottomFrame, width=10, text="%i" % round(caloriesburnt),
                                         font=("digital7", 20, "bold"), bg="DarkSlateGray3", fg="RoyalBlue4")
        outputLabelCaloriesburnt.grid(row=2, column=1)
        # steptaken
        outputLabelSteptaken = Label(bottomFrame, width=10, text="%i" % int(steptaken), font=("digital7", 20, "bold"),
                                     bg="DarkSlateGray3", fg="RoyalBlue4")
        outputLabelSteptaken.grid(row=3, column=1)

        # LOOP
        outputLabelSteptaken.after(1000, calculate_display)  # runing time is not considered
    return


# If button click->
isReset = False


def click():
    global isReset
    global radius
    global weight
    global height
    global rpm
    global TIME
    global stride_length
    global speed
    global distance
    global MET
    global caloriesburnt
    global steptaken

    if isReset:
        btnTxt = "Calculate"
        Button(btnFrame, text=btnTxt, width="10", font=("Comic Sans MS", 15, "bold"), bg="DarkSlateGray4", fg="white",
               command=click).grid(row=0, column=0)
        isReset = False

        # Reset the variables
        [TIME, stride_length, radius, weight, height, rpm, speed, distance, MET, caloriesburnt, steptaken] = [0, 0.414,
                                                                                                              0, 0, 0,
                                                                                                              0, 0, 0,
                                                                                                              0, 0, 0]

        # Clear the entries(Top frame reset)
        entryRpm.delete(0, END)
        entryRadius.delete(0, END)
        entryWeight.delete(0, END)
        entryHeight.delete(0, END)
        unitR.set("cm")
        unitW.set("kg")
        unitH.set("cm")

        # Bottom frame reset
        rowNo = 0
        for text1 in ["%8.2f" % 0, "%8.3f" % 0, "%i" % 0, "%i" % 0]:
            Label(bottomFrame, width=10, text=text1, font=("digital7", 20, "bold"), bg="DarkSlateGray3",
                  fg="RoyalBlue4").grid(row=rowNo, column=1)
            rowNo += 1
        unitSpeed.set("mps")
        unitDistance.set("m")

    else:
        btnTxt = "Reset"
        Button(btnFrame, text=btnTxt, width="10", font=("Comic Sans MS", 15, "bold"), bg="DarkSlateGray4", fg="white",
               command=click).grid(row=0, column=0)
        isReset = True

        # Define variables in required unit
        TIME = 0
        stride_length = 0.414
        try:
            radius = convertInto_m(entryRadius.get(), unitR.get())
            weight = convertInto_kg(entryWeight.get(), unitW.get())
            height = convertInto_m(entryHeight.get(), unitH.get())
            rpm = float(entryRpm.get())

            calculate_display()
        except:
            messagebox.showinfo("ERROR !",
                                "Step 1 : Click the Reset button.\n\nStep 2 : Insert informations "
                                "correctly.")


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Create a main window
root = Tk()
root.title("Treadmill Calculator")
# root.iconbitmap() if you like you may set icon -> (.ico)
root.geometry("750x560")
root.resizable(False, False)
root.configure(bg="DarkSlateGray3")

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Heading
Label(root, text="TREADMILL DASHBOARD", font=("Comic Sans MS", 30, "bold", "italic"), bg="DarkSlateGray3",
      fg="RoyalBlue3").pack()

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Top frame
topFrame = LabelFrame(root, padx=10, pady=10, bg="DarkSlateGray3")
topFrame.pack(padx=20, pady=20)

# First row in top frame(rpm)
Label(topFrame, text="THE RATE AT WITH THE MOTOR IS ROTATING", fg="RoyalBlue4", font=("verdana", 12, "bold"),
      bg="DarkSlateGray3").grid(row=0, column=0, sticky=W)
entryRpm = Entry(topFrame, width=9, borderwidth=0, font=("verdana", 12))
entryRpm.grid(row=0, column=1)
Label(topFrame, text="rpm", font=("verdana", 12), bg="DarkSlateGray3").grid(row=0, column=2, sticky=W)

# Second row in top frame(radius)
Label(topFrame, text="THE RADIUS OF THE MOTOR SHAFT", fg="RoyalBlue4", font=("verdana", 12, "bold"),
      bg="DarkSlateGray3").grid(row=1, column=0, sticky=W)
entryRadius = Entry(topFrame, width=9, borderwidth=0, font=("verdana", 12))
entryRadius.grid(row=1, column=1)
unitR = StringVar()
unitR.set("cm")
Radiobutton(topFrame, text="m", variable=unitR, value="m", font=("verdana", 12), bg="DarkSlateGray3").grid(row=1,
                                                                                                           column=2)
Radiobutton(topFrame, text="cm", variable=unitR, value="cm", font=("verdana", 12), bg="DarkSlateGray3").grid(row=1,
                                                                                                             column=3)
Radiobutton(topFrame, text="inch", variable=unitR, value="inch", font=("verdana", 12), bg="DarkSlateGray3").grid(row=1,
                                                                                                                 column=4)

# Third row in top frame(weight)
Label(topFrame, text="THE WEIGHT", fg="RoyalBlue4", font=("verdana", 12, "bold"), bg="DarkSlateGray3").grid(row=2,
                                                                                                            column=0,
                                                                                                            sticky=W)
entryWeight = Entry(topFrame, width=9, borderwidth=0, font=("verdana", 12))
entryWeight.grid(row=2, column=1)
unitW = StringVar()
unitW.set("kg")
Radiobutton(topFrame, text="kg", variable=unitW, value="kg", font=("verdana", 12), bg="DarkSlateGray3").grid(row=2,
                                                                                                             column=2)
Radiobutton(topFrame, text="lb", variable=unitW, value="lb", font=("verdana", 12), bg="DarkSlateGray3").grid(row=2,
                                                                                                             column=3)

# Fourth row in top frame(height)
Label(topFrame, text="THE HEIGHT", fg="RoyalBlue4", font=("verdana", 12, "bold"), bg="DarkSlateGray3").grid(row=3,
                                                                                                            column=0,
                                                                                                            sticky=W)
entryHeight = Entry(topFrame, width=9, borderwidth=0, font=("verdana", 12))
entryHeight.grid(row=3, column=1)
unitH = StringVar()
unitH.set("cm")
Radiobutton(topFrame, text="m", variable=unitH, value="m", font=("verdana", 12), bg="DarkSlateGray3").grid(row=3,
                                                                                                           column=2)
Radiobutton(topFrame, text="cm", variable=unitH, value="cm", font=("verdana", 12), bg="DarkSlateGray3").grid(row=3,
                                                                                                             column=3)
Radiobutton(topFrame, text="inch", variable=unitH, value="inch", font=("verdana", 12), bg="DarkSlateGray3").grid(row=3,
                                                                                                                 column=4)

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Button frame
btnFrame = LabelFrame(root, padx=0, pady=0, bg="white")
btnFrame.pack(padx=10, pady=10)
Button(btnFrame, text="Calculate", width="10", font=("Comic Sans MS", 15, "bold"), bg="DarkSlateGray4", fg="white",
       command=click).grid(row=0, column=0)

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Bottom frame
bottomFrame = LabelFrame(root, text="Results", padx=5, pady=5, bg="DarkSlateGray3",
                         font=("Comic Sans MS", 27, "bold", "italic"), fg="RoyalBlue3")
bottomFrame.pack(padx=10, pady=10)

# Bottom frame rows
rowNo = 0
for (text1, text2) in [("SPEED", "%8.2f" % 0), ("DISTANCE", "%8.3f" % 0), ("CALORIES BURNT", "%i" % 0),
                       ("STEP TAKEN", "%i" % 0)]:
    Label(bottomFrame, text=text1, font=("verdana", 12, "bold"), fg="RoyalBlue4", bg="DarkSlateGray3").grid(row=rowNo,
                                                                                                            column=0,
                                                                                                            sticky=W)
    Label(bottomFrame, width=10, text=text2, font=("digital7", 20, "bold"), bg="DarkSlateGray3", fg="RoyalBlue4").grid(
        row=rowNo, column=1)
    rowNo += 1

unitSpeed = StringVar()
unitSpeed.set("mps")
Radiobutton(bottomFrame, text="m/s", variable=unitSpeed, value="mps", font=("verdana", 12), bg="DarkSlateGray3").grid(
    row=0, column=2)
Radiobutton(bottomFrame, text="km/h", variable=unitSpeed, value="km/h", font=("verdana", 12), bg="DarkSlateGray3").grid(
    row=0, column=3)

unitDistance = StringVar()
unitDistance.set("m")
Radiobutton(bottomFrame, text="m", variable=unitDistance, value="m", font=("verdana", 12), bg="DarkSlateGray3").grid(
    row=1, column=2)
Radiobutton(bottomFrame, text="km", variable=unitDistance, value="km", font=("verdana", 12), bg="DarkSlateGray3").grid(
    row=1, column=3)

Label(bottomFrame, text="cal", font=("verdana", 12), bg="DarkSlateGray3").grid(row=2, column=2)

root.mainloop()
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
