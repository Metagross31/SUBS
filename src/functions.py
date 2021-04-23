G_FLOWING = False


def toggle_flow():
    global G_FLOWING
    if G_FLOWING:
        print("Flow stopped")
    else:
        print("Flow started")

    G_FLOWING = not G_FLOWING


def build(player):
    if player.power < 100:
        print(player.name + " does not have enough power!")
    else:
        player.power -= 100
        player.wells += 1
        print("Well built for " + player.name)


def kick(player):
    if player.wells > 0:
        player.wells -= 1
        print("Well kicked for " + player.name)
    else:
        print(player.name + " has no more wells!")


def cast(player, cost):
    if player.power < cost:
        print(player.name + " does not have enough power!")
    else:
        player.power -= cost
        player.void += cost * 0.9


def spawn(player, cost):
    if player.power < cost:
        print(player.name + " does not have enough power!")
    else:
        player.power -= cost
        player.army += cost


def kill(player, cost):
    if player.army < cost:
        print(player.name + " does not have that many units in their army!")
    else:
        player.army -= cost
        player.void += cost * 0.9
