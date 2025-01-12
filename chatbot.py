from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def simple_chatbot(user_query):
    responses = {
        "How much has the revenue of Microsoft, Tesla, and Apple grown over the past few years?": 
            "Microsoft's revenue grew by 15.68%, Tesla by 18.78%, and Apple by 2.02% over the last fiscal years.",
        
        "Which company made the most profit in 2023: Apple, Microsoft, or Tesla?": 
            "In FY2023, Apple had the highest net income at 96.9 billion dollars, followed by Microsoft at 72.3 billion dollars and Tesla at 14.9 billion dollars.",
        
        "Has Apple’s cash flow increased or decreased over the past few years?": 
            "Apple's cash flow decreased by 17.15% in FY2023 but increased by 6.97% in FY2024.",
        
        "Is Microsoft’s financial health improving? How do its assets compare to its debts?": 
            "Microsoft's assets-to-liabilities ratio improved to 2.10 in FY2024, up from 1.56 in FY2022.",
        
        "As Tesla’s revenue grows, does its profit also increase?": 
            "Tesla's revenue and net income show a positive correlation, with both increasing over the last three fiscal years."
    }
    return responses.get(user_query, "Sorry, I can only provide information on predefined queries.")

# Serve the frontend interface
@app.route('/')
def home():
    return render_template('index.html')

# Handle chatbot queries
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('query')
    response = simple_chatbot(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)