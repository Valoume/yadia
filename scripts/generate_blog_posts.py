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
            "sector": "RH",
            "title": "Prévenir le turnover avec l'IA : Analyse prédictive pour fidéliser vos équipes",
            "meta_description": "Réduisez le turnover grâce à l'IA. Découvrez comment l'analyse prédictive peut vous aider à identifier les risques et fidéliser vos talents.",
            "keywords": "turnover IA, rétention talents, analyse prédictive RH, fidélisation employés, satisfaction collaborateurs",
            "featured_image": "/static/images/innovation.svg",
            "content": """
<h2>Le turnover : un défi majeur pour les entreprises en 2024</h2>
<p>La rétention des talents est devenue un enjeu critique pour les entreprises. Le coût d'un départ peut représenter jusqu'à 200% du salaire annuel. L'IA offre des solutions innovantes pour anticiper et prévenir ces départs.</p>

<h2>3 Applications de l'IA pour la rétention des talents</h2>
<div class="solution-card mb-4">
    <h3>1. Détection précoce des signaux de désengagement</h3>
    <p>Notre IA analyse en continu les indicateurs clés pour identifier les risques :</p>
    <ul>
        <li>Analyse des patterns de communication</li>
        <li>Suivi des variations de performance</li>
        <li>Évaluation du niveau d'engagement</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>2. Analyse prédictive des facteurs de risque</h3>
    <p>Identifiez les causes profondes du turnover :</p>
    <ul>
        <li>Cartographie des facteurs de stress</li>
        <li>Analyse des parcours professionnels</li>
        <li>Évaluation de la satisfaction au travail</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>3. Recommandations personnalisées</h3>
    <p>Des actions concrètes pour fidéliser chaque collaborateur :</p>
    <ul>
        <li>Plans de développement sur mesure</li>
        <li>Suggestions d'évolution de carrière</li>
        <li>Ajustements des conditions de travail</li>
    </ul>
</div>

<h2>Impact mesurable sur votre organisation</h2>
<div class="results-section">
    <ul>
        <li><strong>-40%</strong> de turnover non désiré</li>
        <li><strong>+35%</strong> de satisfaction employés</li>
        <li><strong>-25%</strong> de coûts de recrutement</li>
    </ul>
</div>

<h2>Agissez maintenant pour fidéliser vos talents</h2>
<p>Ne laissez pas le turnover impacter votre performance. Découvrez comment notre solution IA peut vous aider à construire une stratégie de rétention efficace.</p>

<div class="cta-section">
    <a href="/formulaire" class="btn btn-primary">Obtenir mon audit personnalisé</a>
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
        },
        {
            "sector": "Marketing",
            "title": "Génération de contenu automatisée : Boostez votre production avec l'IA",
            "meta_description": "Optimisez votre production de contenu marketing grâce à l'IA. Découvrez comment automatiser et améliorer la qualité de vos contenus tout en gagnant du temps.",
            "keywords": "génération contenu IA, marketing contenu, automation contenus, production automatisée, efficacité marketing",
            "featured_image": "/static/images/innovation.svg",
            "content": """
<h2>La révolution du content marketing par l'IA</h2>
<p>La création de contenu de qualité est chronophage et coûteuse. L'IA transforme radicalement ce processus en permettant une production massive de contenus personnalisés et optimisés.</p>

<h2>3 Solutions IA pour votre stratégie de contenu</h2>
<div class="solution-card mb-4">
    <h3>1. Génération intelligente de contenus</h3>
    <p>Créez rapidement des contenus pertinents avec :</p>
    <ul>
        <li>Rédaction automatisée d'articles</li>
        <li>Création de newsletters personnalisées</li>
        <li>Adaptation multilingue instantanée</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>2. Optimisation SEO en temps réel</h3>
    <p>Maximisez votre visibilité grâce à :</p>
    <ul>
        <li>Analyse des tendances de recherche</li>
        <li>Suggestions de mots-clés pertinents</li>
        <li>Optimisation continue des contenus</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>3. Personnalisation à grande échelle</h3>
    <p>Adaptez vos contenus à chaque audience :</p>
    <ul>
        <li>Segmentation automatique des lecteurs</li>
        <li>Adaptation du ton et du style</li>
        <li>Recommandations de contenus ciblés</li>
    </ul>
</div>

<h2>Des résultats qui parlent d'eux-mêmes</h2>
<div class="results-section">
    <ul>
        <li><strong>x5</strong> production de contenu</li>
        <li><strong>+80%</strong> de trafic organique</li>
        <li><strong>-60%</strong> de temps de production</li>
    </ul>
</div>

<h2>Révolutionnez votre content marketing</h2>
<p>Découvrez comment notre solution IA peut transformer votre stratégie de contenu et démultiplier votre impact marketing.</p>

<div class="cta-section">
    <a href="/formulaire" class="btn btn-primary">Demander une démonstration</a>
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
