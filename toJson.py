import json
def json_exporter(output):
    output = output.replace("```", "").strip()

    try:
        data = json.loads(output)
        return data
    except json.JSONDecodeError:
        print("Model did not return valid JSON:")
        print(repr(output))
        return None