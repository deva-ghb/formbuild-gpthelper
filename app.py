import openai
from flask import Flask, request
from gpt import gptUtil

app = Flask(__name__, instance_relative_config=True)

@app.route('/formspecificationtojson', methods=['POST', 'GET'])
def ask():
    form_specification = request.json.get("specification")
    fields = request.json.get("fields")
    if isinstance(form_specification, str) and isinstance(fields, list):
        form_json = gptUtil.formSpecificationToJson(form_specification, fields)
        response = {
            'form_json' : form_json
        }
    return response

if __name__ == "__main__":
    app.run(port=5005, debug= True)