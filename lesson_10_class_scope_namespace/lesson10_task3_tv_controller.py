# Lesson 10
# Task 3. TV controller
# Create a simple prototype of a TV controller in Python. It’ll use
# the following commands:
#   first_channel() - turns on the first channel from the list.
#   last_channel() - turns on the last channel from the list.
#   turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
#   next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
#   previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
#   current_channel() - returns the name of the current channel.
#   is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.

# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.
'''
CHANNELS = ["BBC", "Discovery", "TV1000"]
class TVController:
    pass
controller = TVController(CHANNELS)

controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"
'''
CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels_list):
        self.channel_curr = 0 # В коде используется (channel_curr) - 1
        self.channels_list = channels_list

    def first_channel(self):
        return CHANNELS[0] #TODO: Попробовать убрать return в ф-циях которым он не нужен

    def last_channel(self):
        return CHANNELS[-1]

    def turn_channel(self, n):
        self.channel_curr = n - 1
        if len(CHANNELS) >= self.channel_curr > 0:
            return CHANNELS[self.channel_curr]
        else:
            return CHANNELS[self.channel_curr * 0]

    def next_channel(self):
        if self.channel_curr < (len(CHANNELS) - 1):
            self.channel_curr += 1
            return CHANNELS[self.channel_curr]
        else:
            return CHANNELS[self.channel_curr * 0]

    def previous_channel(self):
        if self.channel_curr >= -(len(CHANNELS)):
            self.channel_curr -= 1
            return CHANNELS[self.channel_curr]
        else:
            return CHANNELS[self.channel_curr * 0]

    def current_channel(self):
        return f'{CHANNELS[self.channel_curr]}'

    def is_exist(self, name_or_num):
        if isinstance(name_or_num, int) and name_or_num <= len(CHANNELS):
            return "Yes"
        elif isinstance(name_or_num, str) and name_or_num in CHANNELS:
            return "Yes"
        else:
            return "No"


if __name__ == '__main__':
    controller = TVController(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    # assert controller.turn_channel(2) == "Discovery"       # Turning check
    # assert controller.turn_channel(3) == "TV1000"          # Turning check
    assert controller.next_channel() == "Discovery"
    # assert controller.next_channel() == "TV1000"           # Cycling check
    # assert controller.next_channel() == "BBC"              # Cycling check
    assert controller.previous_channel() == "BBC"
    # assert controller.previous_channel() == "TV1000"       # Cycling check
    # assert controller.previous_channel() == "Discovery"    # Cycling check
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("BBC") == "Yes"
