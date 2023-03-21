import openai
from flask import Flask, request, Response
from gpt import gptUtil

app = Flask(__name__, instance_relative_config=True)

@app.route('/formspecificationtojson', methods=['POST', 'GET'])
def ask():
    form_specification = request.json.get("specification")
    fields = request.json.get("fields")
    if isinstance(form_specification, str) and isinstance(fields, list):
        try:
            form_json = gptUtil.formSpecificationToJson(form_specification, fields)
            response = {
                'form_json' : form_json
            }
            return response
        except Exception as e:
            msg = str({'message': 'internal server error'})
            return Response(msg, status=500, mimetype='application/json')
            
    else:
        msg = str({'message': 'invalid input'})
        return Response(msg, status=400, mimetype='application/json')
        

if __name__ == "__main__":
    app.run(port=5005, debug= True)