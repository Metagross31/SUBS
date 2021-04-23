import sched
import time
from gui import *
import functions


def my_after():
    for player__ in (player_1, player_2):
        labels[(player__.name, "power_val")].config(text=str(round(player__.power)))
        labels[(player__.name, "void_val")].config(text=str(round(player__.void)))
        labels[(player__.name, "wells_val")].config(text=str(player__.wells))
        labels[(player__.name, "army_val")].config(text=str(player__.army))
        labels[(player__.name, "void_gain")].config(text="+" + str(round(player__.void_gps() * 2)))
        labels[(player__.name, "wells_gain")].config(text="+" + str(player__.wells))

    if functions.G_FLOWING:
        for player__ in player_1, player_2:
            power_gained_this_step = player__.total_gps() * tick_time_ms / 1000.0
            player__.power += power_gained_this_step
            player__.void -= player__.void_gps() * tick_time_ms / 1000.0

    main_window.win.after(tick_time_ms, my_after)


def main():
    my_after()

    main_window.mainloop()


if __name__ == '__main__':
    main()
