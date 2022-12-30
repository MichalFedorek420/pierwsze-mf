class TV():
    def __init__(self):
        self.is_on=False
        self.channel_no=1
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on:
            print(f"TV is on and the channel is {self.channel_no}")
        else:
            print("TV is off")
    def set_channel(self,new_channel_no):
        self.channel_no=new_channel_no
tv=TV()
tv.turn_on()
tv.show_status()
tv.set_channel(20)
tv.show_status()
atrybuty niebieski
obikety filoetowy
