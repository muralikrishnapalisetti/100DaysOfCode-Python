# 📅 Day 8 – Secret Auction 🏷️

Today, I built a fun and interactive **Secret Auction** program in Python using **dictionaries**! 🧠💰  
Each user submits a hidden bid, and at the end, the highest bidder is revealed as the winner.

---

## 📌 What I Learned:

✅ How to use **Python dictionaries**:
- `bids[name] = amount` to add new entries  
- `.keys()`, `.values()`, `.items()` for accessing data  
- `pop()`, `popitem()`, `del`, `clear()` for removing data  

✅ Built and used a **custom function** to find the highest bidder  
✅ Practiced **while loops**, **user input**, and **dictionary iteration**  
✅ Used a simple `clear_screen()` trick (`"\n" * 100`) to simulate clearing the terminal

---

## 🚀 Project Features:

- Accepts **multiple user bids** using a loop  
- Clears screen between entries to **maintain secrecy**  
- Finds and prints the **highest bidder** and their **winning amount**  
- Real-world auction simulation using core Python concepts

---

## 📁 File:

- `secret_auction.py` – Main Python file containing all logic

---

## 🖥️ Sample Output:

Welcome to the Secret Auction Program!

What is your name?: Alice

What is your bid price (₹)?: 500

Are there any other users who want to bid? Type 'yes' or 'no': yes

What is your name?: Bob

What is your bid price (₹)?: 800

Are there any other users who want to bid? Type 'yes' or 'no': no

The winner is Bob with a bid of ₹800!
