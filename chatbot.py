import tkinter as tk
from tkinter import Scrollbar, END

# Function for bot response
def bot_reply(event=None):  # 'event' parameter is added for key binding
    user_input = user_entry.get().lower()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(END, f"You: {user_input}\n", "user")
    
    user_entry.delete(0, END)
    
    if "hello" in user_input:
        response = "Bot: Hello! How can I assist you today?\n"
    elif "how are you" in user_input:
        response = "Bot: I'm just a program, but I'm functioning properly! 😊\n"
    elif "bye" in user_input:
        response = "Bot: Goodbye! Have a great day! 👋\n"
    else:
        response = "Bot: Sorry, I don't understand that.\n"
    
    chat_log.insert(END, response, "bot")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(END)

# Main window setup
root = tk.Tk()
root.title("Purple Chatbot")
root.geometry("400x500")
root.resizable(width=False, height=False)

# Colors and Styles
bg_color = "#4B0082"
text_color = "#FFFFFF"
button_color = "#9370DB"
entry_bg = "#D8BFD8"

root.configure(bg=bg_color)

# Chat window (Scrollable)
chat_log = tk.Text(root, bg=bg_color, fg=text_color, font=("Arial", 12), state=tk.DISABLED, wrap=tk.WORD)
chat_log.place(x=6, y=6, width=370, height=400)

scrollbar = Scrollbar(root, command=chat_log.yview)
chat_log['yscrollcommand'] = scrollbar.set
scrollbar.place(x=376, y=6, height=400)

# User entry field
user_entry = tk.Entry(root, bg=entry_bg, fg=text_color, font=("Arial", 12))
user_entry.place(x=6, y=420, width=260, height=30)

# Send button
send_button = tk.Button(root, text="Send", bg=button_color, fg=text_color, font=("Arial", 12), command=bot_reply)
send_button.place(x=275, y=420, width=100, height=30)

# Bind the Enter key to the bot_reply function
root.bind('<Return>', bot_reply)

# Tag configurations for user and bot messages
chat_log.tag_config("user", foreground="#ADFF2F")
chat_log.tag_config("bot", foreground="#FFD700")

root.mainloop()
