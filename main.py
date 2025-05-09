import tkinter as tk #for GUI
from tkinter import messagebox #for pop-up window
import webbrowser  #for opening URLs for toolkit link


#dictionary about common apps and what kind of access they request by default
app_data = {
    "tiktok": {"tracks_location": True, "accesses_contacts": True, "uses_microphone": True},
    "instagram": {"tracks_location": True, "accesses_contacts": False, "uses_microphone": True},
    "signal": {"tracks_location": False, "accesses_contacts": False, "uses_microphone": False},
    "facebook": {"tracks_location": True, "accesses_contacts": True, "uses_microphone": True},
    "snapchat": {"tracks_location": True, "accesses_contacts": False, "uses_microphone": True},
}

#PASSWORD CHECK - is your password strong?
def check_password():          #funciton for when user clicks "check password"
    password = entry_password.get()
    weak_passwords = ["password", "123456", "qwerty", "iloveyou", "admin", "spot", "abc123", "baseball", "1111111", "7654321"]
    score = 0 #tracks risk level
    feedback = []

    if password.lower() in weak_passwords:
        feedback.append("❌ This is a commonly used password.")
        score += 2 #if the password is in the weak list, add 2 points to risk and explain why.

    if len(password) < 8:
        feedback.append("⚠️ Your password is short. Use at least 8 characters.")
        score += 1 #warns if the password is short.

    if password.isnumeric() or password.isalpha():
        feedback.append("⚠️ Mix letters, numbers, and symbols.")
        score += 1 #if it’s only letters or only numbers, encourage more variety.

    if score == 0:
        feedback.append("✅ Your password seems reasonably strong.") #no problems!
    
    feedback.append(f"🔐 Password Risk Score: {score}/4")
    messagebox.showinfo("Password Check", "\n".join(feedback)) #this adds up the final score and shows all feedback in a pop-up window



#WEBSITE CHECK
def check_website():          #gets website URL input from user
    url = entry_website.get()
    score = 0
    feedback = []

#basic security check: does the URL start with "https://"?
    if not url.startswith("https://"):
        feedback.append("🚨 Site is not secure (missing HTTPS).")
        score += 2
    else:
        feedback.append("✅ Website uses HTTPS.")
    
    feedback.append(f"🌐 Website Risk Score: {score}/2")
    messagebox.showinfo("Website Check", "\n".join(feedback))

#APP SCANNER
def scan_app():
    app = entry_app.get().strip().lower() #changed this so that caps and lowercase dont matter
    feedback = []

    if app in app_data:
        data = app_data[app]
        score = 0
        if data["tracks_location"]:
            feedback.append("📍 This app tracks your location.")
            score += 1
        if data["accesses_contacts"]:
            feedback.append("📇 This app accesses your contacts.")
            score += 1
        if data["uses_microphone"]:
            feedback.append("🎤 This app uses your microphone.")
            score += 1
        feedback.append(f"🔒 Privacy Risk Score: {score}/3")
    else:
        feedback.append("⚠️ Sorry, I don’t have data on that app yet.")
    
    messagebox.showinfo("App Scan", "\n".join(feedback)) #show results in pop-up window

#TOOLKIT
def open_toolkit():
    webbrowser.open("https://understandingyourdigitalself.my.canva.site/")

#MAIN UI
root = tk.Tk()
root.title("Digital Privacy Risk Scanner")
root.geometry("800x400")
root.resizable(False, False)


title = tk.Label(root, text="🛡️ Digital Privacy Risk Scanner", font=("Helvetica", 16, "bold"))
title.pack(pady=10)


desc = tk.Label(root, text="This tool runs entirely on your computer. No data is stored or shared.",
                font=("Helvetica", 10), wraplength=480)
desc.pack(pady=5)


#PASSWORD SECTION
frame_password = tk.Frame(root)
frame_password.pack(pady=10)

tk.Label(frame_password, text="🔐 Enter Password:").grid(row=0, column=0, padx=5)
entry_password = tk.Entry(frame_password, width=30, show="*")
entry_password.grid(row=0, column=1, padx=5)
tk.Button(frame_password, text="Check Password", command=check_password).grid(row=0, column=2, padx=5)


#WEBSITE SECTION
frame_website = tk.Frame(root)
frame_website.pack(pady=10)

tk.Label(frame_website, text="🌐 Enter Website URL:").grid(row=0, column=0, padx=5)
entry_website = tk.Entry(frame_website, width=30)
entry_website.grid(row=0, column=1, padx=5)
tk.Button(frame_website, text="Check Website", command=check_website).grid(row=0, column=2, padx=5)


#APP SECTION
frame_app = tk.Frame(root)
frame_app.pack(pady=10)

tk.Label(frame_app, text="📱 Enter App Name:").grid(row=0, column=0, padx=5)
entry_app = tk.Entry(frame_app, width=30)
entry_app.grid(row=0, column=1, padx=5)
tk.Button(frame_app, text="Scan App", command=scan_app).grid(row=0, column=2, padx=5)

#LINK TO TOOLKIT
tk.Button(root, text="📖 View Full Privacy Toolkit", command=open_toolkit, fg="blue", cursor="hand2").pack(pady=5)

#FOOTER
footer = tk.Label(root, text="Designed by Avery Crower • Educational Use Only", font=("Helvetica", 8))
footer.pack(side="bottom", pady=15)


root.mainloop()
