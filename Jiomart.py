import random

bot_responses = {
    'greeting': [
        "Welcome to Jio Mart! How can I assist you today?",
        "Hello! How may I help you with your Jio Mart experience?",
        "Hi there! What can I do for you today?"
    ],
    'how_are_you': [
        "I'm doing great. How about you?",
        "I'm here to assist you. How can I make your day better?"
    ],
    'product_inquiry': [
        "At Jio Mart, we offer a wide range of products. Is there anything specific you're looking for?",
        "Sure! Let me know what product you are interested in, and I'll provide you with the details."
    ],
    'contact': [
        "You can contact us through phone, email, or our website's contact form for any inquiries or feedback.",
        "If you have any questions or need assistance, feel free to reach out to our customer support."
    ],
    'thank_you': [
        "You're welcome! Let me know if there's anything else I can assist you with.",
        "Thank you for choosing Jio Mart! Have a great day!"
    ],
    'about': [
        "JioMart is India's online shopping destination for Mobiles, Electronics, Grocery, Fashion, Home & Kitchen, Furniture, Jewellery, Beauty, and more.It provides Great offers, Pay on Delivery, Low Prices, easy returns,Top Brands and delivery to select locations.",
        "JioMart is a leading Indian online shopping platform offering a vast range of products, including Mobiles, Electronics, Grocery, Fashion, Home & Kitchen, Furniture, Jewellery, Beauty, and more. It provides great offers, low prices, easy returns, and reliable delivery to customers across the country.",
    ],
    'me': [
        "I am a chatbot designed to assist you with your Jio Mart experience. How can I help you today?",
        "I'm an AI-powered virtual assistant here to enhance your Jio Mart experience. How can I be of assistance to you today?"
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
    elif any(keyword in user_input for keyword in ['product', 'item', 'buy']):
        return random.choice(bot_responses['product_inquiry'])
    elif any(keyword in user_input for keyword in ['contact', 'feedback', 'help']):
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
