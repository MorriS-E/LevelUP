import random
from tkinter import *

class Player:

    def __init__(self, name, level, xp_gained, xp_to_gain):
        self.name = name
        self.level = level
        self.xp_gained = xp_gained
        self.xp_to_gain = xp_to_gain

    def save(self):
        file = open("playerData.txt", 'w')
        xp_obtained_str = self.xp_gained
        xp_needed_str = self.xp_to_gain
        level_str = self.level
        file.write(str(xp_obtained_str)+"\n")
        file.write(str(xp_needed_str)+"\n")
        file.write(str(level_str)+"\n")
        file.close()

        # counter_saveFile = open("counterData.txt", 'w')
        # for j in range(len(items)):
        #     content = items[j].count
        #     file.write(str(content)+"\n")
        # counter_saveFile.close()

        with open("counterData.txt", 'r+') as file:
            for j in range(len(items)):
                content = items[j].count
                file.write(str(content)+"\n")

    def load(self):
        file = open("playerData.txt", 'r')
        with open("playerData.txt") as f:
            lines = f.readlines()
        self.xp_gained = int(lines[0])
        self.xp_to_gain = int(lines[1])
        self.level = int(lines[2])
        self.create_xp_label()[0].config(text=self.xp_gained)
        self.create_xp_label()[1].config(text=self.xp_to_gain)
        self.create_xp_label()[2].config(text=self.level)
        file.close()

        counter_loadFile = open("counterData.txt", 'r')
        with open("counterData.txt") as c:
            counter_lines = c.readlines()

        for k in range(len(items)):
            items[k].count = int(counter_lines[k])
            items[k].create_label().config(text=items[k].count)
        counter_loadFile.close()

    def experience_change(self):
        if self.level < 5:
            self.xp_to_gain += 150
        elif 5 <= self.level < 10:
            self.xp_to_gain += 550
        elif self.level > 10:
            self.xp_to_gain += 1100
        self.xp_to_gain += 10

    def level_up(self):
        if self.xp_gained >= self.xp_to_gain:
            self.level += 1
            self.experience_change()
            self.create_xp_label()[1].config(text=f'/{self.xp_to_gain}')

    def create_xp_label(self):
        level_lbl = Label(root, text="Level: ")
        level_lbl.grid(row=0, column=0)
        level_num = Label(root, text=self.level)
        level_num.grid(row=0, column=1)

        xp_lbl = Label(root, text="XP: ")
        xp_lbl.grid(row=1, column=0)
        xp_res = Label(root, text=f'{self.xp_gained}')
        xp_res.grid(row=1, column=1)
        xp_ned = Label(root, text=f'/{self.xp_to_gain}')
        xp_ned.grid(row=1, column=2)

        save_button = Button(root, text="save", command=self.save)
        save_button.grid(row=24, column=0)
        load_button = Button(root, text="load", command=self.load)
        load_button.grid(row=24, column=2)
        return [xp_res, xp_ned, level_num]


class Item:

    def __init__(self, name, xp_value, grid_row, count):
        self.name = name
        self.xp_value = xp_value
        self.grid_row = grid_row
        self.count = count

    def create_label(self):
        item = Label(root, text=f'{self.name} ({self.xp_value} XP)')
        item.grid(row=self.grid_row, column=0)
        item_minus_button = Button(root, text='-', command=lambda: self.minus())
        item_minus_button.grid(row=self.grid_row, column=1)
        item_counter = Label(root, text=0)
        item_counter.grid(row=self.grid_row, column=2)
        item_plus_button = Button(root, text='+', command=lambda: self.add())
        item_plus_button.grid(row=self.grid_row, column=3)
        return item_counter

    def double_points(self):
        if player.level % 5 == 0:
            self.xp_value *= 2

    def minus(self):
        if self.count != 0:
            self.count -= 1
            player.xp_gained -= self.xp_value
        self.create_label().config(text=self.count)
        player.create_xp_label()[0].config(text=f'{player.xp_gained}')

    def add(self):
        self.count += 1
        if player.level % 5 == 0:
            player.xp_gained += self.xp_value * 2
        else:
            player.xp_gained += self.xp_value
        self.create_label().config(text=self.count)
        player.create_xp_label()[0].config(text=f'{player.xp_gained}')
        player.level_up()


if __name__ == '__main__':

    root = Tk()
    player = Player("EXP: ", 1, 0, 100)
    player.create_xp_label()

    items = [
        Item("Dishes", 1, 2, 0),
        Item("1 Minute Cardio", 5, 3, 0),
        Item("Make Meal", 10, 4, 0),
        Item("Put in Laundry", 10, 5, 0),
        Item("Hang Laundry", 10, 6, 0),
        Item("Put Away Laundry", 10, 7, 0),
        Item("Hoover per room", 15, 8, 0),
        Item("Strength Exercise (5 reps)", 5, 9, 0),
        Item("Open Curtains", 1, 10, 0),
        Item("Make Bed", 1, 11, 0),
        Item("Go to the Shops", 20, 12, 0),
        Item("Take out Rubbish", 5, 13, 0),
        Item("Take out Recycling", 5, 14, 0),
        Item("Showering", 15, 15, 0),
        Item("Brushing Teeth", 10, 16, 0),
        Item("Learn 5 Korean Words", 5, 17, 0),
        Item("Review Korean Words After 24hrs", 5, 18, 0),
        Item("1 Minute Gaming Before 6pm", -1, 19, 0),
        Item("Ordering Simple Things", -10, 20, 0),
        Item("Eating Junk Food", -10, 21, 0),
        Item("Ordering Takeaways", -20, 22, 0),
        Item("Eating After 6pm", -20, 23, 0),

    ]

    for i in range(len(items)):
        items[i].create_label()

    root.mainloop()
