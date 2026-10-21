def battery_bars(percent):
    match percent:
        case _ if percent == 100:
            return "[#####]"
        case _ if 80<=percent:
            return "[####.]"
        case _ if 60<=percent<80:
            return "[###..]"
        case _ if 40<=percent<60:
            return "[##...]"
        case _ if 20<=percent<40:
            return "[#....]"
        case _ if percent<20:
            return "[.....]"



battery_bars(100)  # => "[#####]"
battery_bars(70)   # => "[###..]"
battery_bars(20)   # => "[#....]"
battery_bars(19)   # => "[.....]"
battery_bars(0)    # => "[.....]"