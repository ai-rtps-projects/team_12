import tkinter as tk

# State variables
stage = "start"
selected_movie = ""
selected_seat = ""
payment_method = ""

def chatbot_response(user_input):
    global stage, selected_movie, selected_seat, payment_method
    user_input = user_input.lower()

    if stage == "start":
        if "book" in user_input:
            stage = "movie"
            return "🎬 Choose a movie: Leo / Jawan / Avengers"
        else:
            return "Type 'book' to start ticket booking."

    elif stage == "movie":
        selected_movie = user_input
        stage = "seat"
        return f"Nice choice! '{selected_movie.title()}' selected.\nAvailable seats: A1, A2, B1, B2\nPlease choose your seat."

    elif stage == "seat":
        selected_seat = user_input.upper()
        stage = "payment"
        return f"Seat {selected_seat} selected.\nChoose payment method: UPI / Card / NetBanking"

    elif stage == "payment":
        payment_method = user_input.upper()
        stage = "done"
        return (f"💳 Payment via {payment_method} successful!\n"
                f"🎟 Ticket Booked!\nMovie: {selected_movie.title()}\nSeat: {selected_seat}")

    elif stage == "done":
        return "Booking already completed. Type 'book' to start again."

# Send message
def send_message():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return
    
    chat_box.insert(tk.END, "You: " + user_msg + "\n")
    response = chatbot_response(user_msg)
    chat_box.insert(tk.END, "Bot: " + response + "\n\n")
    
    entry.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Ticket Booking Chatbot")

chat_box = tk.Text(root, height=20, width=50)
chat_box.pack()

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT)

root.mainloop()
