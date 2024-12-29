import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Set up the trigger words and corresponding sound files
trigger_sounds = {
    "hello": "/Users/student/Documents/soundchat/Snare 2.wav",
    "hi": "/Users/student/Documents/soundchat/Snare 2.wav"
}

# Preload the sounds
sounds = {}
for word, file in trigger_sounds.items():
    sounds[word] = pygame.mixer.Sound(file)

# Keep track of the channels used for playing sounds
playing_sounds = {}  # Mapping from trigger word to channel

turn = 1  # User 1 starts

while True:
    if turn == 1:
        user_input = input("User 1: ")
        turn = 2
    else:
        user_input = input("User 2: ")
        turn = 1

    if user_input.lower() == 'stop':
        # Stop all sounds
        for channel in playing_sounds.values():
            channel.stop()
        playing_sounds.clear()
        print("All sounds stopped.")
    else:
        # Check if any trigger words are in the input
        for word in trigger_sounds.keys():
            if word in user_input.lower():
                if word not in playing_sounds:
                    # Play the sound associated with the trigger word, looping indefinitely
                    sound = sounds[word]
                    channel = sound.play(loops=-1)
                    if channel is not None:
                        playing_sounds[word] = channel
