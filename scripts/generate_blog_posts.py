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
            "meta_description": "Découvrez comment l'IA révolutionne le recrutement en automatisant le tri des CV et en optimisant la sélection des talents. Guide pratique et résultats concrets.",
            "keywords": "recrutement IA, tri CV automatique, sélection talents, RH intelligence artificielle, optimisation recrutement",
            "featured_image": "/static/images/innovation.svg",
            "content": """
<h2>Les défis actuels du recrutement en 2024</h2>
<p>Dans un marché du travail en constante évolution, les équipes RH font face à des défis majeurs : un volume croissant de candidatures, un besoin de réactivité accru et la nécessité de sélectionner les meilleurs talents. L'intelligence artificielle apporte des solutions concrètes à ces problématiques.</p>

<h2>3 Solutions IA pour transformer votre processus de recrutement</h2>
<div class="solution-card mb-4">
    <h3>1. Analyse intelligente des CV</h3>
    <p>Notre technologie IA analyse automatiquement les CV et les met en correspondance avec vos offres d'emploi, permettant :</p>
    <ul>
        <li>Une réduction de 60% du temps de traitement</li>
        <li>Une meilleure identification des compétences clés</li>
        <li>Une standardisation du processus d'évaluation</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>2. Évaluation objective des candidats</h3>
    <p>L'IA permet une évaluation impartiale basée sur des critères objectifs :</p>
    <ul>
        <li>Analyse des compétences techniques et soft skills</li>
        <li>Prédiction de l'adéquation au poste</li>
        <li>Réduction des biais de recrutement</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>3. Automatisation du suivi candidat</h3>
    <p>Optimisez l'expérience candidat grâce à :</p>
    <ul>
        <li>Des réponses automatisées personnalisées</li>
        <li>Un suivi en temps réel du statut des candidatures</li>
        <li>Des rappels intelligents pour les étapes clés</li>
    </ul>
</div>

<h2>Résultats concrets pour votre entreprise</h2>
<div class="results-section">
    <ul>
        <li><strong>-60%</strong> sur le temps de traitement des candidatures</li>
        <li><strong>+45%</strong> d'amélioration de la qualité des recrutements</li>
        <li><strong>-35%</strong> de réduction des coûts de recrutement</li>
    </ul>
</div>

<h2>Commencez votre transformation RH</h2>
<p>Pour transformer votre processus de recrutement avec l'IA, commencez par un audit gratuit de vos besoins. Nos experts vous guideront vers les solutions les plus adaptées à votre contexte.</p>

<div class="cta-section">
    <a href="/formulaire" class="btn btn-primary">Demander mon audit gratuit</a>
</div>
"""
        },
        {
            "sector": "Marketing",
            "title": "Personnalisation marketing avec l'IA : Optimisez vos campagnes pour chaque client",
            "meta_description": "Maximisez l'impact de vos campagnes marketing grâce à l'IA. Découvrez comment personnaliser chaque interaction client et augmenter vos conversions.",
            "keywords": "marketing IA, personnalisation campagnes, marketing automation, intelligence artificielle marketing, ROI marketing",
            "featured_image": "/static/images/innovation.svg",
            "content": """
<h2>Le marketing personnalisé : un impératif en 2024</h2>
<p>À l'ère du digital, vos clients attendent des expériences sur mesure. Découvrez comment l'IA transforme la personnalisation marketing en réalité accessible.</p>

<h2>3 Innovations IA pour révolutionner votre marketing</h2>
<div class="solution-card mb-4">
    <h3>1. Segmentation client ultra-précise</h3>
    <p>Notre IA analyse en profondeur vos données clients pour :</p>
    <ul>
        <li>Identifier des micro-segments pertinents</li>
        <li>Prédire les comportements d'achat</li>
        <li>Personnaliser les offres en temps réel</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>2. Optimisation du contenu marketing</h3>
    <p>Créez du contenu qui convertit grâce à :</p>
    <ul>
        <li>L'analyse prédictive des tendances</li>
        <li>La génération de contenus personnalisés</li>
        <li>L'optimisation automatique des messages</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>3. Automatisation des campagnes</h3>
    <p>Maximisez l'efficacité de vos campagnes avec :</p>
    <ul>
        <li>Le ciblage intelligent des audiences</li>
        <li>L'optimisation en temps réel des performances</li>
        <li>L'adaptation automatique des messages</li>
    </ul>
</div>

<h2>Résultats prouvés</h2>
<div class="results-section">
    <ul>
        <li><strong>+150%</strong> d'engagement client</li>
        <li><strong>+40%</strong> de taux de conversion</li>
        <li><strong>-30%</strong> de coût d'acquisition</li>
    </ul>
</div>

<h2>Transformez votre marketing dès aujourd'hui</h2>
<p>Découvrez comment l'IA peut révolutionner votre stratégie marketing grâce à notre audit personnalisé gratuit.</p>

<div class="cta-section">
    <a href="/formulaire" class="btn btn-primary">Obtenir mon audit gratuit</a>
</div>
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
