from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/analyze_string', methods=['POST'])

def srting_analist(): 
    data = request.get_json()
    text = data.get('texto', '')
    

    palindrome = text == text[::-1]

    histogram = dict()
    for e in text:
        histogram[e] = histogram.get(e, 0) + 1

    response = {
        'is_palindrome': palindrome,
        'histogram': histogram
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
