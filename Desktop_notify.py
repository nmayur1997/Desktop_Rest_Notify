from plyer import notification
import time
import random


messages = [
    "🌿 Remember to Rest 🌿\n\n💤 Taking regular breaks helps to improve your mental health and overall productivity. 🌟",
    "✨ Time for a Short Break! ✨\n\n🧠 Boost your concentration and mood by taking a quick rest. You’ve earned it! 😊",
    "🌸 Take a Deep Breath 🌸\n\n💪 A short break can enhance your immune system and reduce stress. 🌿 Stay refreshed!",
    "💤 Don’t Forget to Rest 💤\n\n😌 Relaxing can lead to better mental clarity and a happier you. 🌟 Enjoy your break!",
    "🌟 Quick Rest Reminder 🌟\n\n🍎 A moment of rest helps with metabolism and overall health. Take a pause and rejuvenate! 🌼"
]

if __name__ == '__main__':
    while True:
        
        message = random.choice(messages)
        
        notification.notify(
            title='🌟 Take a Break 🌟',
            message=message,
            timeout=10  
        )
        time.sleep(1800)  # Notify every 30 minutes
