import os
from dotenv import load_dotenv
load_dotenv()
import openai
import json
from typing import List

# set the key
openai.api_key = os.environ.get("OPENAI_API_KEY")


def formSpecificationToJson(form_specification : str, fields_accepted : List):
    # form_specification = "form for appliation of driving license"

    # fields_accepted = ["text" , "date" , "textarea" , "radio", "dropdown"]

    fields_accepted_string = ", ".join(fields_accepted)

    example = """
    {'header' : "Title",
    "sections": ["section name":[
        { "fieldname" : "name of the field", "fieldtype": "type of the field"},
        { "fieldname" : "name of the field", "fieldtype": "type of the field"}]],
    "footer" : { 
        "fieldName": "name of the field",
        "fieldtype": "type of the field"
    }
    }
    """

    prompt = f"""
    can you generate for the specification {form_specification} in the json format.
    currently there are following fields types in form as mention here : {fields_accepted_string}.
    an example form would look like below:
    {example}
    give entire response as a valid JSON and include sections from the specification 
    """


    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": prompt}
            ]
    )

    tokens_used = completion['usage']['total_tokens']

    gpt_response = completion["choices"][0]["message"]["content"]

    form_fields_json = json.loads(gpt_response)

    return form_fields_json



if __name__ == '__main__':
    form_json = formSpecificationToJson(form_specification= "form for appliation of driving license",
                            fields_accepted = ["text" , "date" , "textarea" , "radio", "dropdown"]
                            )
    print(form_json)