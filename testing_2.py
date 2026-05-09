words = ["eat", "yummy", "eggs", "microphone", "laughed"]

formatted_words = [m.capitalize() if len(m) > 5 else m.lower() for m in words]
print(formatted_words)