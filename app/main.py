import sys
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from llm import PRDGenerator

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to GenPRD Flask API!'


@app.route('/api/generate-prd', methods=['POST'])
def generate_prd():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        prd_generator = PRDGenerator()
        results = prd_generator.generate_prd(data)  # Using the correct method name

        if "error" in results:
            return jsonify(results), 500

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    host = os.environ.get('HOST', '0.0.0.0')
    
    app.run(host=host, port=port, debug=False)