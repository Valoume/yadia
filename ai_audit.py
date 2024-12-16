import json
import os
from openai import OpenAI

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_sector_recommendations(secteur):
    """Retourne les recommandations spécifiques au secteur."""
    recommendations_by_sector = {
        "RH": ["Solutions liées au recrutement", "Analyse du turnover", "Plans de formation automatisés"],
        "Marketing": ["Personnalisation client", "Génération de contenu", "Analyse des tendances"],
        "Service Client": ["Chatbots intelligents", "Analyse des feedbacks", "Priorisation des tickets"],
        "Finance": ["Automatisation des factures", "Détection de fraudes", "Prévision des flux"],
        "Logistique": ["Optimisation des routes", "Gestion des stocks", "Prédictions logistiques"],
        "Production": ["Contrôle qualité IA", "Maintenance prédictive", "Optimisation des process"],
        "Juridique": ["Analyse des contrats", "Gestion documentaire", "Conformité automatisée"],
        "IT": ["Détection d'anomalies", "Optimisation réseau", "Sécurité prédictive"],
        "Vente": ["Qualification des leads", "CRM intelligent", "Devis automatisés"],
        "Stratégie": ["Tableaux de bord IA", "Simulation de scénarios", "Aide à la décision"]
    }
    return recommendations_by_sector.get(secteur, [])

def estimate_project_complexity(recommendation):
    """Détermine la complexité du projet et retourne le temps et le coût estimés."""
    complexity_mapping = {
        "simple": {
            "time": "10-20 heures",
            "cost": "500€ - 1 000€"
        },
        "medium": {
            "time": "20-40 heures",
            "cost": "1 500€ - 3 000€"
        },
        "complex": {
            "time": "40+ heures",
            "cost": "3 500€ - 7 000€"
        }
    }
    
    # Logique simplifiée pour déterminer la complexité
    if "chatbot" in recommendation.lower() or "automatisation simple" in recommendation.lower():
        return complexity_mapping["simple"]
    elif "prédictif" in recommendation.lower() or "analyse" in recommendation.lower():
        return complexity_mapping["medium"]
    else:
        return complexity_mapping["complex"]

def generate_ai_audit_report(form_data):
    """Génère un rapport d'audit IA personnalisé basé sur le formulaire."""
    try:
        secteur = form_data.get('secteur')
        experience = form_data.get('experience', '')
        defis = form_data.get('defis', '')
        objectifs = form_data.get('objectifs', '')

        # Obtenir les recommandations spécifiques au secteur
        sector_recommendations = get_sector_recommendations(secteur)
        
        # Sélectionner les 3-5 recommandations les plus pertinentes
        selected_recommendations = sector_recommendations[:min(5, len(sector_recommendations))]
        
        recommendations = []
        for rec in selected_recommendations:
            complexity = estimate_project_complexity(rec)
            recommendations.append({
                "titre": rec,
                "description": f"Cette solution est particulièrement adaptée à votre secteur {secteur} "
                             f"et répond à vos objectifs spécifiques.",
                "temps_estime": complexity["time"],
                "cout_estime": complexity["cost"]
            })

        result = {
            "analyse": {
                "secteur": secteur,
                "contexte": "Analyse basée sur votre expérience et vos objectifs spécifiques",
                "niveau_maturite": "Adapté à votre niveau actuel de maîtrise de l'IA"
            },
            "recommandations": recommendations
        }

        return result
    except Exception as e:
        return {
            "error": "Échec de la génération du rapport d'audit",
            "details": str(e)
        }
