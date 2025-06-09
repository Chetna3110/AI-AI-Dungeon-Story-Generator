import tkinter as tk
from tkinter import messagebox
from story_generator import generate_story  # Import from your other file

# Function to run when "Generate Story" button is clicked
def on_generate():
    prompt = prompt_entry.get()
    genre = genre_var.get()

    if not prompt.strip():
        messagebox.showwarning("Input Error", "Please enter a story prompt.")
        return

    full_prompt = f"{genre} story: {prompt}"

    try:
        # Generate 3 story continuations
        stories = generate_story(full_prompt, max_length=150, num_return_sequences=3)

        output_text.delete(1.0, tk.END)
        for i, story in enumerate(stories, 1):
            output_text.insert(tk.END, f"Story {i}:\n{story}\n\n{'-'*60}\n\n")

        # Save the first story to a text file
        with open("generated_story.txt", "w", encoding="utf-8") as f:
            f.write(stories[0])

    except Exception as e:
        messagebox.showerror("Generation Error", f"An error occurred:\n{e}")

# Initialize main window
import tkinter as tk

# ======= Theme Colors =======
BG_COLOR = "#4eb5ec"
FRAME_COLOR = "#4049A8"
BUTTON_COLOR = "#6c5ce7"
BUTTON_HOVER = "#a29bfe"
TEXT_COLOR = "#171b1c"
OUTPUT_BG = "#2a85f4"


# ======= Root Window =======
root = tk.Tk()
root.title("AI Dungeon Story Generator")
root.geometry("720x600")
root.configure(bg=BG_COLOR)

# ======= Prompt Section =======
prompt_frame = tk.Frame(root, bg=BG_COLOR)
prompt_frame.pack(pady=20)

tk.Label(prompt_frame, text="Enter your story prompt:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12)).pack()
prompt_entry = tk.Entry(prompt_frame, width=60, font=("Arial", 12))
prompt_entry.pack(pady=5)

# ======= Genre Selection =======
genre_frame = tk.Frame(root, bg=BG_COLOR)
genre_frame.pack(pady=10)

tk.Label(genre_frame, text="Select Genre:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12)).pack()
genre_var = tk.StringVar(value="Fantasy")
genre_menu = tk.OptionMenu(genre_frame, genre_var, "Fantasy", "Mystery", "Sci-Fi", "Horror", "Adventure")
genre_menu.config(font=("Arial", 11), bg=FRAME_COLOR, fg=TEXT_COLOR)
genre_menu.pack(pady=5)

# ======= Generate Button =======
def on_enter(e):
    generate_btn.config(bg=BUTTON_HOVER)

def on_leave(e):
    generate_btn.config(bg=BUTTON_COLOR)

generate_btn = tk.Button(root, text="Generate Story", command=on_generate,
                         font=("Arial", 12), bg=BUTTON_COLOR, fg="white", padx=10, pady=5)
generate_btn.pack(pady=10)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)

# ======= Output Box =======
output_frame = tk.Frame(root, bg=BG_COLOR)
output_frame.pack(pady=10)

output_text = tk.Text(output_frame, wrap=tk.WORD, height=20, width=80, font=("Georgia", 11),
                      bg=OUTPUT_BG, fg=TEXT_COLOR, borderwidth=2, relief="groove")
output_text.pack()

# ======= Run the App =======
root.mainloop()
