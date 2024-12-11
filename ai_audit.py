import json
import os
from openai import OpenAI

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_ai_audit_report(form_data):
    """Generate an AI-powered audit report based on form submissions with company analysis."""
    try:
        prompt = f"""Analysez d'abord l'entreprise suivante et fournissez des recommandations d'implémentation IA adaptées au poste spécifique :

        Entreprise: {form_data.get('company-name')}
        Secteur: {form_data.get('industry')}
        Poste Actuel: {form_data.get('current-job')}
        Technologies Actuelles: {', '.join(form_data.get('current_tech', []))}
        Défis Business: {form_data.get('challenges')}
        Objectifs d'Implémentation: {', '.join(form_data.get('goals', []))}
        
        Répondez en français au format JSON avec la structure suivante:
        {{
            "analyse_entreprise": {{
                "présentation": "Description détaillée de l'entreprise basée sur le secteur et les informations fournies",
                "objectifs_stratégiques": "Analyse des objectifs stratégiques de l'entreprise",
                "positionnement_marché": "Positionnement sur le marché et avantages concurrentiels potentiels"
            }},
            "analyse_poste": {{
                "description": "Analyse du poste et de ses responsabilités principales",
                "défis_quotidiens": "Défis spécifiques liés au poste",
                "potentiel_optimisation": "Potentiel d'optimisation par l'IA"
            }},
            "recommandations": [
                {{
                    "domaine": "Domaine d'amélioration spécifique au poste",
                    "solution": "Solution IA recommandée avec détails d'implémentation",
                    "impact": "Impact attendu sur les performances du poste",
                    "délai": "Délai estimé de mise en œuvre",
                    "priorité": "haute/moyenne/basse",
                    "adaptation_poste": "Comment la solution s'adapte spécifiquement au poste"
                }}
            ],
            "gains_productivité": {{
                "temps_économisé": "Estimation des gains de temps hebdomadaires",
                "répartition_tâches": {{
                    "automatisation_complete": "Pourcentage des tâches automatisables à 100%",
                    "intervention_humaine": "Pourcentage des tâches nécessitant intervention humaine",
                    "collaboration_ia": "Pourcentage des tâches en mode collaboratif IA-humain"
                }},
                "impact_performance": "Impact global sur la performance du poste"
            }},
            "prochaines_étapes": [
                "Réservez votre consultation gratuite pour approfondir ces recommandations",
                "Téléchargez notre guide d'implémentation IA personnalisé (29,99€)"
            ]
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
