import random

bot_responses = {
    'greeting': [
        "Welcome to Red Bus! How can I assist you today?",
        "Hello! How may I help you with your Red Bus experience?",
        "Hi there! How can I make your Red Bus journey better?"
    ],
    'how_are_you': [
        "I'm doing great. How about you?",
        "I'm here to assist you. How can I make your day better?"
    ],
    'bus_booking': [
        "Sure! To book a bus ticket, please provide me with your source and destination locations, travel date, and number of passengers.",
        "I can help you with bus bookings. Let me know your travel details, such as source, destination, date, and number of passengers."
    ],
    'contact': [
        "You can contact Red Bus support through phone, email, or their website's contact form for any inquiries or assistance.",
        "If you have any questions or need support, feel free to reach out to Red Bus customer service."
    ],
    'thank_you': [
        "You're welcome! Let me know if there's anything else I can assist you with.",
        "Thank you for choosing Red Bus! Have a great journey!"
    ],
    'about': [
        "Red Bus is India's largest online bus ticketing platform, offering bus ticket bookings for various routes across the country. With a wide network of bus operators, Red Bus provides convenient and reliable travel services to passengers.",
        "Red Bus is a leading online bus ticketing platform in India, connecting travelers with bus operators for hassle-free bookings. Whether you're planning a short trip or a long journey, Red Bus ensures a comfortable and convenient travel experience."
    ],
    'me': [
        "I am a chatbot designed to assist you with your Red Bus experience. How can I help you today?",
        "I'm an AI-powered virtual assistant here to enhance your Red Bus journey. How can I be of assistance to you today?"
    ],
    'default': [
        "I'm sorry, I didn't understand. Can you please rephrase your question?",
        "Apologies, I couldn't comprehend your message. Could you please provide more context?"
    ]   
}

def generate_response(user_input):
    user_input = user_input.lower()

    if any(greeting in user_input for greeting in ['hi', 'hello', 'hey']):
        return random.choice(bot_responses['greeting'])
    elif "how are you" in user_input:
        return random.choice(bot_responses['how_are_you'])
    elif any(keyword in user_input for keyword in ['book', 'ticket', 'bus']):
        return random.choice(bot_responses['bus_booking'])
    elif any(keyword in user_input for keyword in ['contact', 'help']):
        return random.choice(bot_responses['contact'])
    elif "thank you" in user_input:
        return random.choice(bot_responses['thank_you'])
    elif any(keyword in user_input for keyword in ['bye', 'goodbye']):
        return random.choice(bot_responses['thank_you'])
    elif any(keyword in user_input for keyword in ['about', 'tell me']):
        return random.choice(bot_responses['about'])
    elif any(keyword in user_input for keyword in ['who are you', 'what are you']):
        return random.choice(bot_responses['me'])
    else:
        return random.choice(bot_responses['default'])
    
while True:
    user_input = input("User: ")
    response = generate_response(user_input)
    print("Bot:", response)

    if any(keyword in user_input for keyword in ['bye', 'goodbye']):
        break
