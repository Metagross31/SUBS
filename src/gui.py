from tkinter import *
from player import Player
from window import Window
from functions import toggle_flow, build, kick, cast, spawn, kill

main_window = Window(1350, 650, "Skylords Ultimate Battle Simulator", "#272727")

for i in (3, 5):
    main_window.win.grid_columnconfigure(i, minsize=main_window.size_x/9)

labels = {}
buttons = {}
labels["title"] = Label(main_window.win, text="SUBS - Skylords Ultimate Battle Simulator", bg=main_window.bg_colour,
                        fg="white", font="Calibri 20 bold")

spacing = 6
ticks_per_second = 10
tick_time_ms = 100

player_1 = Player("Player 1", 100, 100, 2, 0)
player_2 = Player("Player 2", 100, 100, 2, 0)

for i, player_ in enumerate((player_1, player_2)):
    labels[(player_.name, "name")] = Label(main_window.win, text=player_.name, bg=main_window.bg_colour, fg="white",
                                           font="Calibri 12 bold").grid(row=1 + spacing * i, column=0, padx=20, pady=5,
                                                                        sticky=W)

    # Power labels
    labels[(player_.name, "power")] = Label(main_window.win, text="Power:", bg=main_window.bg_colour, fg="white",
                                            font="Calibri 12").grid(row=2 + spacing * i, column=0, padx=20, pady=5,
                                                                    sticky=W)

    labels[(player_.name, "power_val")] = Label(main_window.win, bg=main_window.bg_colour,
                                                fg="white", font="Calibri 12")
    labels[(player_.name, "power_val")].grid(row=2 + spacing * i, column=1, padx=20, pady=5, sticky=W)

    # Void labels
    labels[(player_.name, "void")] = Label(main_window.win, text="Void:", bg=main_window.bg_colour, fg="white",
                                           font="Calibri 12").grid(row=3 + spacing * i, column=0, padx=20, pady=5,
                                                                   sticky=W)

    labels[(player_.name, "void_val")] = Label(main_window.win, bg=main_window.bg_colour,
                                               fg="white", font="Calibri 12")
    labels[(player_.name, "void_val")].grid(row=3 + spacing * i, column=1, padx=20, pady=5, sticky=W)

    labels[(player_.name, "void_gain")] = Label(main_window.win, bg=main_window.bg_colour, fg="white",
                                                font="Calibri 12")
    labels[(player_.name, "void_gain")].grid(row=3 + spacing * i, column=2, padx=20, pady=5, sticky=W)

    # Well labels
    labels[(player_.name, "wells")] = Label(main_window.win, text="Wells:", bg=main_window.bg_colour, fg="white",
                                            font="Calibri 12").grid(row=4 + spacing * i, column=0, padx=20, pady=5,
                                                                    sticky=W)

    labels[(player_.name, "wells_val")] = Label(main_window.win, bg=main_window.bg_colour,
                                                fg="white", font="Calibri 12")

    labels[(player_.name, "wells_val")].grid(row=4 + spacing * i, column=1, padx=20, pady=5, sticky=W)

    labels[(player_.name, "wells_gain")] = Label(main_window.win, bg=main_window.bg_colour, fg="white",
                                                 font="Calibri 12")
    labels[(player_.name, "wells_gain")].grid(row=4 + spacing * i, column=2, padx=20, pady=5, sticky=W)

    # Army labels
    labels[(player_.name, "army")] = Label(main_window.win, text="Army:", bg=main_window.bg_colour, fg="white",
                                           font="Calibri 12").grid(row=5 + spacing * i, column=0, padx=20, pady=5,
                                                                   sticky=W)

    labels[(player_.name, "army_val")] = Label(main_window.win, bg=main_window.bg_colour,
                                               fg="white", font="Calibri 12")
    labels[(player_.name, "army_val")].grid(row=5 + spacing * i, column=1, padx=20, pady=5, sticky=W)

buttons["toggle_flow"] = Button(main_window.win, text='Toggle powerflow',
                                command=toggle_flow)
buttons["toggle_flow"].grid(row=spacing, column=1, padx=(20, 0), sticky=W)

buttons[(player_1.name, "build")] = Button(main_window.win, text='Build Well',
                                           command=lambda: build(player_1)).grid(row=4, column=3,
                                                                                 padx=(20, 0), sticky=W)

buttons[(player_2.name, "build")] = Button(main_window.win, text='Build Well',
                                           command=lambda: build(player_2)).grid(row=4 + spacing, column=3,
                                                                                 padx=(20, 0), sticky=W)

buttons[(player_1.name, "kick")] = Button(main_window.win, text='Kick Well',
                                          command=lambda: kick(player_1)).grid(row=5, column=3,
                                                                               padx=(20, 0), sticky=W)

buttons[(player_2.name, "build")] = Button(main_window.win, text='Kick Well',
                                           command=lambda: kick(player_2)).grid(row=5 + spacing, column=3,
                                                                                padx=(20, 0), sticky=W)

labels["Spells"] = Label(main_window.win, text="Spells:", bg=main_window.bg_colour, fg="white",
                         font="Calibri 12 bold").grid(row=1, column=4, sticky=W)

for i, player_ in enumerate((player_1, player_2)):
    labels[(player_.name, "80spell")] = Label(main_window.win, text="80", bg=main_window.bg_colour, fg="white",
                         font="Calibri 12")
    labels[(player_.name, "80spell")].grid(row=2 + i * spacing, column=4, sticky=W)
    labels[(player_.name, "75spell")] = Label(main_window.win, text="75", bg=main_window.bg_colour, fg="white",
                                              font="Calibri 12")
    labels[(player_.name, "75spell")].grid(row=3 + i * spacing, column=4, sticky=W)
    labels[(player_.name, "55spell")] = Label(main_window.win, text="55", bg=main_window.bg_colour, fg="white",
                                              font="Calibri 12")
    labels[(player_.name, "55spell")].grid(row=4 + i * spacing, column=4, sticky=W)
    labels[(player_.name, "25spell")] = Label(main_window.win, text="25", bg=main_window.bg_colour, fg="white",
                                              font="Calibri 12")
    labels[(player_.name, "25spell")].grid(row=5 + i * spacing, column=4, sticky=W)

buttons[(player_1.name, "80spell")] = Button(main_window.win, text="cast", command=lambda: cast(player_1, 80))
buttons[(player_1.name, "80spell")].grid(row=2, column=5, sticky=W)
buttons[(player_1.name, "75spell")] = Button(main_window.win, text="cast", command=lambda: cast(player_1, 75))
buttons[(player_1.name, "75spell")].grid(row=3, column=5, sticky=W)
buttons[(player_1.name, "55spell")] = Button(main_window.win, text="cast", command=lambda: cast(player_1, 55))
buttons[(player_1.name, "55spell")].grid(row=4, column=5, sticky=W)
buttons[(player_1.name, "25spell")] = Button(main_window.win, text="cast", command=lambda: cast(player_1, 25))
buttons[(player_1.name, "25spell")].grid(row=5, column=5, sticky=W)
buttons[(player_2.name, "80spell")] = Button(main_window.win, text="cast", command=lambda: cast(player_2, 80))
buttons[(player_2.name, "80spell")].grid(row=2 + spacing, column=5, sticky=W)
buttons[(player_2.name, "75spell")] = Button(main_window.win, text="cast", command=lambda: cast(player_2, 75))
buttons[(player_2.name, "75spell")].grid(row=3 + spacing, column=5, sticky=W)
buttons[(player_2.name, "55spell")] = Button(main_window.win, text="cast", command=lambda: cast(player_2, 55))
buttons[(player_2.name, "55spell")].grid(row=4 + spacing, column=5, sticky=W)
buttons[(player_2.name, "25spell")] = Button(main_window.win, text="cast", command=lambda: cast(player_2, 25))
buttons[(player_2.name, "25spell")].grid(row=5 + spacing, column=5, sticky=W)

labels["Units"] = Label(main_window.win, text="Units and buildings:", bg=main_window.bg_colour, fg="white",
                        font="Calibri 12 bold").grid(row=1, column=6, sticky=W)

for i, player_ in enumerate((player_1, player_2)):
    labels[(player_.name, "100unit")] = Label(main_window.win, text="100", bg=main_window.bg_colour, fg="white",
                                              font="Calibri 12")
    labels[(player_.name, "100unit")].grid(row=2 + i * spacing, column=6, sticky=W)
    labels[(player_.name, "70unit")] = Label(main_window.win, text="70", bg=main_window.bg_colour, fg="white",
                                              font="Calibri 12")
    labels[(player_.name, "70unit")].grid(row=3 + i * spacing, column=6, sticky=W)
    labels[(player_.name, "60unit")] = Label(main_window.win, text="60", bg=main_window.bg_colour, fg="white",
                                              font="Calibri 12")
    labels[(player_.name, "60unit")].grid(row=4 + i * spacing, column=6, sticky=W)
    labels[(player_.name, "50unit")] = Label(main_window.win, text="50", bg=main_window.bg_colour, fg="white",
                                              font="Calibri 12")
    labels[(player_.name, "50unit")].grid(row=5 + i * spacing, column=6, sticky=W)

buttons[(player_1.name, "100spawn")] = Button(main_window.win, text="spawn", command=lambda: spawn(player_1, 100))
buttons[(player_1.name, "100spawn")].grid(row=2, column=7, sticky=W)
buttons[(player_1.name, "100kill")] = Button(main_window.win, text="kill", command=lambda: kill(player_1, 100))
buttons[(player_1.name, "100kill")].grid(row=2, column=8, sticky=W)

buttons[(player_1.name, "70spawn")] = Button(main_window.win, text="spawn", command=lambda: spawn(player_1, 70))
buttons[(player_1.name, "70spawn")].grid(row=3, column=7, sticky=W)
buttons[(player_1.name, "70kill")] = Button(main_window.win, text="kill", command=lambda: kill(player_1, 70))
buttons[(player_1.name, "70kill")].grid(row=3, column=8, sticky=W)

buttons[(player_1.name, "60spawn")] = Button(main_window.win, text="spawn", command=lambda: spawn(player_1, 60))
buttons[(player_1.name, "60spawn")].grid(row=4, column=7, sticky=W)
buttons[(player_1.name, "60kill")] = Button(main_window.win, text="kill", command=lambda: kill(player_1, 60))
buttons[(player_1.name, "60kill")].grid(row=4, column=8, sticky=W)

buttons[(player_1.name, "50spawn")] = Button(main_window.win, text="spawn", command=lambda: spawn(player_1, 50))
buttons[(player_1.name, "50spawn")].grid(row=5, column=7, sticky=W)
buttons[(player_1.name, "50kill")] = Button(main_window.win, text="kill", command=lambda: kill(player_1, 50))
buttons[(player_1.name, "50kill")].grid(row=5, column=8, sticky=W)

buttons[(player_2.name, "100spawn")] = Button(main_window.win, text="spawn", command=lambda: spawn(player_2, 100))
buttons[(player_2.name, "100spawn")].grid(row=2 + spacing, column=7, sticky=W)
buttons[(player_2.name, "100kill")] = Button(main_window.win, text="kill", command=lambda: kill(player_2, 100))
buttons[(player_2.name, "100kill")].grid(row=2 + spacing, column=8, sticky=W)

buttons[(player_2.name, "70spawn")] = Button(main_window.win, text="spawn", command=lambda: spawn(player_2, 70))
buttons[(player_2.name, "70spawn")].grid(row=3 + spacing, column=7, sticky=W)
buttons[(player_2.name, "70kill")] = Button(main_window.win, text="kill", command=lambda: kill(player_2, 70))
buttons[(player_2.name, "70kill")].grid(row=3 + spacing, column=8, sticky=W)

buttons[(player_2.name, "60spawn")] = Button(main_window.win, text="spawn", command=lambda: spawn(player_2, 60))
buttons[(player_2.name, "60spawn")].grid(row=4 + spacing, column=7, sticky=W)
buttons[(player_2.name, "60kill")] = Button(main_window.win, text="kill", command=lambda: kill(player_2, 60))
buttons[(player_2.name, "60kill")].grid(row=4 + spacing, column=8, sticky=W)

buttons[(player_2.name, "50spawn")] = Button(main_window.win, text="spawn", command=lambda: spawn(player_2, 50))
buttons[(player_2.name, "50spawn")].grid(row=5 + spacing, column=7, sticky=W)
buttons[(player_2.name, "50kill")] = Button(main_window.win, text="kill", command=lambda: kill(player_2, 50))
buttons[(player_2.name, "50kill")].grid(row=5 + spacing, column=8, sticky=W)
