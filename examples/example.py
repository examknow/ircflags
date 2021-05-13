from ircflags import Flags

flags = Flags("access.json", "ABCDefg")

flags.setFlags("lunchd", "+AeBf")
print(flags.getFlags("lunchd"))
flags.setFlags("lunchd", "+C", channel="#test")
print(flags.getFlags("lunchd", channel="#test"))
flags.setFlags("lunchd", "+*", channel="#test")
print(flags.getFlags("lunchd", channel="#test"))
flags.setFlags("lunchd", "-*", channel="#test")
print(flags.getFlags("lunchd", channel="#test"))
