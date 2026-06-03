class VideoGame:
    def __init__(self, name, hours_played):
        self.name = name
        self.hours_played = hours_played
    
    
    def __str__(self):
        return f"{self.name} - {self.hours_played}"
    
    def __add__(self, another):
        hours = self.hours_played + another.hours_played
        return VideoGame("Combined", hours)
    
g1 = VideoGame("Minecraft", 120)
g2 = VideoGame("Terraria", 80)

print(g1)
total = g1 + g2
print(total)
