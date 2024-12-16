import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db
from models.blog import BlogPost
import slugify

def generate_seo_blog_posts():
    posts = [
        {
            "sector": "RH",
            "title": "Optimisez votre recrutement avec l'IA : Tri des CV et sélection des talents simplifiée",
            "meta_description": "Découvrez comment l'IA révolutionne le recrutement en automatisant le tri des CV et en optimisant la sélection des talents. Solutions concrètes et retour sur investissement.",
            "keywords": "recrutement IA, tri CV automatique, sélection talents, RH intelligence artificielle, optimisation recrutement",
            "content": """
<h2>Les défis actuels du recrutement</h2>
<p>Dans un marché du travail de plus en plus compétitif, les équipes RH font face à des défis majeurs : un volume croissant de candidatures, un besoin de réactivité accru et la nécessité de sélectionner les meilleurs talents. L'intelligence artificielle apporte des solutions concrètes à ces problématiques.</p>

<h2>Comment l'IA transforme le processus de recrutement</h2>
<p>L'IA révolutionne chaque étape du recrutement :</p>
<ul>
    <li>Analyse automatique des CV et matching avec les offres</li>
    <li>Évaluation objective des compétences</li>
    <li>Prédiction de l'adéquation candidat-poste</li>
</ul>

<h2>Bénéfices concrets pour votre entreprise</h2>
<p>L'implémentation de l'IA dans votre processus de recrutement permet :</p>
<ul>
    <li>Réduction de 60% du temps de traitement des candidatures</li>
    <li>Amélioration de la qualité des recrutements</li>
    <li>Réduction des biais de sélection</li>
</ul>

<h2>Par où commencer ?</h2>
<p>Pour transformer votre processus de recrutement avec l'IA, commencez par un audit gratuit de vos besoins. Nos experts vous guideront vers les solutions les plus adaptées à votre contexte.</p>
"""
        },
        {
            "sector": "Marketing",
            "title": "Personnalisation marketing avec l'IA : Des campagnes sur-mesure pour chaque client",
            "meta_description": "Apprenez à utiliser l'IA pour créer des campagnes marketing personnalisées qui augmentent l'engagement et les conversions. Guide complet et études de cas.",
            "keywords": "marketing IA, personnalisation campagnes, marketing automation, intelligence artificielle marketing",
            "content": """
<h2>L'ère du marketing personnalisé</h2>
<p>Les consommateurs attendent aujourd'hui des expériences personnalisées. L'IA permet de répondre à cette attente en analysant les données clients pour créer des campagnes vraiment pertinentes.</p>

<h2>Solutions IA pour le marketing</h2>
<ul>
    <li>Segmentation client avancée</li>
    <li>Personnalisation en temps réel</li>
    <li>Optimisation des contenus</li>
    <li>Prédiction des comportements</li>
</ul>

<h2>Résultats mesurables</h2>
<p>Les entreprises utilisant l'IA en marketing constatent :</p>
<ul>
    <li>+150% d'engagement client</li>
    <li>+40% de taux de conversion</li>
    <li>-30% de coût d'acquisition</li>
</ul>

<h2>Commencez votre transformation</h2>
<p>Découvrez comment l'IA peut révolutionner votre marketing grâce à notre audit personnalisé gratuit.</p>
"""
        }
    ]

    with app.app_context():
        for post_data in posts:
            post = BlogPost(
                title=post_data["title"],
                slug=slugify.slugify(post_data["title"]),
                content=post_data["content"],
                sector=post_data["sector"],
                meta_description=post_data["meta_description"],
                keywords=post_data["keywords"]
            )
            db.session.add(post)
        
        try:
            db.session.commit()
            print("Blog posts generated successfully!")
        except Exception as e:
            print(f"Error generating blog posts: {e}")
            db.session.rollback()

if __name__ == "__main__":
    generate_seo_blog_posts()
