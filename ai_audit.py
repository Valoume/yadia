import json
import os
from openai import OpenAI

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_ai_audit_report(form_data):
    """Generate an AI-powered audit report based on form submissions."""
    try:
        prompt = f"""Analyze the following business information and provide specific AI implementation recommendations:
        Industry: {form_data.get('industry')}
        Current Technologies: {', '.join(form_data.get('current_tech', []))}
        Business Challenges: {form_data.get('challenges')}
        Implementation Goals: {', '.join(form_data.get('goals', []))}
        
        Please provide recommendations in French. Respond in JSON format with the following structure:
        {{
            "summary": "Brief overview of the analysis in French",
            "recommendations": [
                {{
                    "area": "Area of improvement in French",
                    "solution": "Recommended AI solution in French",
                    "impact": "Expected business impact in French",
                    "timeline": "Estimated implementation timeline in French",
                    "priority": "haute/moyenne/basse"
                }}
            ],
            "estimated_roi": "Projected ROI range in French",
            "next_steps": ["Specific action items in French"]
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI implementation expert providing business analysis and recommendations in French."
                },
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        return {
            "error": "Échec de la génération du rapport d'audit",
            "details": str(e)
        }
