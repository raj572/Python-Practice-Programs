import tkinter as tk
from bardapi import BardCookies

# Initialize BardCookies with your cookie data
cookie_dict = {
    "__Secure-1PSID" : "bQhohkK3gPEj1S0ifgNdCuqXN_4qwruZEEotdISokrCte8evheRlTwYqC_6B-V_o4040Gg.",
    "__Secure-1PSIDTS" : "sidts-CjIB3e41ha6FZZiZjf7TwRWbhjCexnBnTO6EVX8Hr1HA-DMXp75ypPDBqY4w6kUpN49fkxAA",
    "__Secure-1PSIDCC" : "ACA-OxNvKTdZuFaFLml1Ac5V35dV8wRXqgBYiRTIBnzEV9Z-f05pa5z_h7ZJrOQFp-YJSIw6yjkX"
}
bard = BardCookies(cookie_dict=cookie_dict)

# Function to handle user queries and display responses
def handle_query(event=None):
    user_query = query_entry.get()  # Get user input from the entry field
    response = bard.get_answer(user_query)['content']  # Get the response from BardAPI
    response_text.config(state=tk.NORMAL)  # Enable text widget for editing
    response_text.delete(1.0, tk.END)  # Clear previous text
    response_text.insert(tk.END, response)  # Insert new response
    response_text.config(state=tk.DISABLED)  # Disable text widget to make it read-only

# Create the main GUI window
root = tk.Tk()
root.title("BardAPI Chat")

# Set background color to black and font color to aqua
root.configure(bg="black")
root.option_add("*TButton*highlightBackground", "black")
root.option_add("*TButton*highlightColor", "black")
root.option_add("*TButton*background", "black")
root.option_add("*TButton*foreground", "aqua")
root.option_add("*TButton.padding", [5, 5])

# Create GUI components
query_label = tk.Label(root, text="Enter Your Query:", bg="black", fg="aqua")
query_entry = tk.Entry(root, width=50, bg="black", fg="aqua", insertbackground="aqua")
query_button = tk.Button(root, text="Get Response", command=handle_query, bg="black", fg="aqua", width=20, height=2)
response_text = tk.Text(root, wrap=tk.WORD, height=25, width=70,padx=15,pady=15, state=tk.DISABLED, bg="black", fg="aqua")  # Text widget for displaying responses
response_scrollbar = tk.Scrollbar(root, command=response_text.yview)
response_text.config(yscrollcommand=response_scrollbar.set)

# Arrange GUI components
query_label.pack(pady=10)
query_entry.pack()
query_button.pack(pady=10)
response_text.pack(padx=10, pady=5)
response_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Bind the Enter key to trigger the query button
query_entry.bind("<Return>", handle_query)

# Start the GUI main loop
root.mainloop()


