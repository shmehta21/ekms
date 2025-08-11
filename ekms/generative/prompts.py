

def build_prompt(preset, content):
    templates = {
        "Executive Summary":"Summarize the following document in a concise executive summary:\n\n{content}" ,
        "New-hire explanation": "Explain the following document in simple terms suitable for a new hire:\n\n{content}",
        "Compliance Checklist": "Extract key compliance-related points from the following document and present as a checklist:\n\n{content}"
    }
    return templates[preset].format(content=content)