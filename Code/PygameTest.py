import pygame

pygame.mixer.init()

stems = {
    "808" : 'Stems\808-Bass-Scared_Confused.wav',
    "bell-a" : 'Stems\Bell-Anxious.wav',
    "kick-a" : 'Stems\Kick-Aggressive.wav',
    "kick-p" : 'Stems\Kick-Pulse-Tense_Excited.wav',
    "p1" : 'Stems\Percussion1.wav',
    "p2" : 'Stems\Percussion2.wav',
    "p3" : 'Stems\Percussion3.wav',
    "p4" : 'Stems\Percussion4.wav',
    "p6" : 'Stems\Percussion6.wav',
    "snare-t" : 'Stems\Snare-Tense.wav',
    "snare2" : 'Stems\Snare2.wav',
    "snare3" : 'Stems\Snare3-Confused.wav',
    "sa" : 'Stems\Synth-Accent-Tense_Confused.wav',
    "sa1" : 'Stems\Synth-Accent1-Tense_Confused.wav',
    "sa3" : 'Stems\Synth-Accent3_Confused.wav',
    "sa4" : 'Stems\Synth-Accent4_Percussion5-Confused.wav',
    "sa5" : 'Stems\Synth-Accent5-Confused.wav',
}

playing_sounds = {}

# Function to toggle playback with fade-in and fade-out
def toggle_stem(key, volume=1.0, fade_duration=1000):
    if key in stems:
        if key in playing_sounds:  # If the sound is already playing, fade it out
            print(f"Fading out: {key}")
            playing_sounds[key].fadeout(fade_duration)  # Fade out sound
            del playing_sounds[key]
        else:  # If the sound is not playing, fade it in
            try:
                sound = pygame.mixer.Sound(stems[key])  # Load the sound
                sound.set_volume(volume)  # Adjust the volume
                sound.play(loops=-1, fade_ms=fade_duration)  # Play with fade-in
                playing_sounds[key] = sound  # Track the sound
                print(f"Fading in: {key}")
            except pygame.error as e:
                print(f"Error loading sound: {e}")
    else:
        print(f"Key '{key}' not found in stems!")
    display_playing_sounds()

# Function to display currently playing sounds
def display_playing_sounds():
    if playing_sounds:
        print("Currently playing sounds:")
        for key in playing_sounds.keys():
            print(f" - {key}")
    else:
        print("No sounds are currently playing.")

# Main loop for user input
print("Enter a stem key to toggle the sound, or 'vol <key> <value>' to adjust volume, or 'quit' to exit:")
while True:
    user_input = input("> ").strip().lower()
    if user_input == "quit":  # Exit condition
        print("Exiting...")
        break
    elif user_input.startswith("vol "):  # Adjust volume
        parts = user_input.split()
        if len(parts) == 3:
            key = parts[1]
            try:
                volume = float(parts[2])
                if key in playing_sounds:
                    playing_sounds[key].set_volume(volume)
                    print(f"Volume of {key} set to {volume}")
                else:
                    print(f"{key} is not currently playing.")
            except ValueError:
                print("Invalid volume. Please enter a number between 0.0 and 1.0.")
        else:
            print("Invalid volume command. Use 'vol <key> <value>'.")
    else:
        toggle_stem(user_input)

# Ensure all sounds are stopped before quitting
for sound in playing_sounds.values():
    sound.fadeout(1000)  # Fade out all sounds on exit

pygame.mixer.quit()