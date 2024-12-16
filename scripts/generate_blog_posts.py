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
        },
        {
            "sector": "Service Client",
            "title": "Les chatbots IA : Une révolution pour le support client et l'expérience utilisateur",
            "meta_description": "Découvrez comment les chatbots IA transforment le service client. Améliorez la satisfaction client et réduisez les coûts grâce à l'automatisation intelligente.",
            "keywords": "chatbot IA, service client automatisé, support client IA, expérience utilisateur, satisfaction client",
            "featured_image": "/static/images/innovation.svg",
            "content": """
<h2>Le service client à l'ère de l'IA : Un changement de paradigme</h2>
<p>Dans un monde où l'instantanéité est devenue la norme, les entreprises font face à une pression croissante pour fournir un support client 24/7. Les chatbots IA représentent la solution idéale pour relever ce défi.</p>

<h2>3 Innovations IA pour transformer votre service client</h2>
<div class="solution-card mb-4">
    <h3>1. Support client 24/7 intelligent</h3>
    <p>Offrez une assistance continue grâce à :</p>
    <ul>
        <li>Réponses instantanées aux questions fréquentes</li>
        <li>Traitement multilingue des demandes</li>
        <li>Escalade automatique vers les agents humains si nécessaire</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>2. Personnalisation avancée des interactions</h3>
    <p>Améliorez l'expérience client avec :</p>
    <ul>
        <li>Reconnaissance du contexte et de l'historique</li>
        <li>Adaptation du ton selon le profil client</li>
        <li>Suggestions proactives personnalisées</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>3. Analyse prédictive des besoins</h3>
    <p>Anticipez les demandes clients grâce à :</p>
    <ul>
        <li>Détection précoce des problèmes</li>
        <li>Recommandations automatiques de solutions</li>
        <li>Suivi proactif de la satisfaction</li>
    </ul>
</div>

<h2>Résultats concrets pour votre entreprise</h2>
<div class="results-section">
    <ul>
        <li><strong>-70%</strong> de temps de réponse moyen</li>
        <li><strong>+45%</strong> de satisfaction client</li>
        <li><strong>-40%</strong> de coûts de support</li>
    </ul>
</div>

<h2>Transformez votre service client dès aujourd'hui</h2>
<p>Ne laissez pas passer l'opportunité d'optimiser votre service client. Découvrez comment nos solutions IA peuvent révolutionner l'expérience de vos clients.</p>

<div class="cta-section">
    <a href="/formulaire" class="btn btn-primary">Obtenir mon audit gratuit</a>
</div>
"""
        },
        {
            "sector": "Finance",
            "title": "Automatisation des factures et paiements : L'IA pour simplifier votre comptabilité",
            "meta_description": "Optimisez votre gestion financière grâce à l'IA. Découvrez comment automatiser vos factures et paiements pour gagner en efficacité et réduire les erreurs.",
            "keywords": "automatisation comptable, IA finance, facturation automatique, gestion paiements IA, comptabilité digitale",
            "featured_image": "/static/images/innovation.svg",
            "content": """
<h2>La révolution de la comptabilité par l'IA</h2>
<p>La gestion manuelle des factures et des paiements est chronophage et source d'erreurs. L'IA transforme ces processus en les automatisant de manière intelligente.</p>

<h2>3 Solutions IA pour votre gestion financière</h2>
<div class="solution-card mb-4">
    <h3>1. Automatisation du traitement des factures</h3>
    <p>Simplifiez votre comptabilité avec :</p>
    <ul>
        <li>Reconnaissance automatique des documents</li>
        <li>Extraction intelligente des données</li>
        <li>Catégorisation automatique des dépenses</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>2. Gestion intelligente des paiements</h3>
    <p>Optimisez vos flux financiers grâce à :</p>
    <ul>
        <li>Priorisation automatique des paiements</li>
        <li>Détection des anomalies en temps réel</li>
        <li>Réconciliation bancaire automatisée</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>3. Reporting financier automatisé</h3>
    <p>Pilotez votre activité avec précision :</p>
    <ul>
        <li>Génération automatique des rapports</li>
        <li>Tableaux de bord en temps réel</li>
        <li>Prévisions financières basées sur l'IA</li>
    </ul>
</div>

<h2>Impact sur votre performance financière</h2>
<div class="results-section">
    <ul>
        <li><strong>-80%</strong> de temps de traitement</li>
        <li><strong>-95%</strong> d'erreurs de saisie</li>
        <li><strong>+30%</strong> de productivité comptable</li>
    </ul>
</div>

<h2>Optimisez votre gestion financière</h2>
<p>Transformez votre comptabilité en un processus fluide et automatisé. Découvrez comment notre solution IA peut révolutionner votre gestion financière.</p>

<div class="cta-section">
    <a href="/formulaire" class="btn btn-primary">Demander une démonstration</a>
</div>
"""
        },
        {
            "sector": "Logistique",
            "title": "Optimisation des itinéraires de livraison grâce à l'IA : Gagnez en efficacité",
            "meta_description": "Optimisez vos circuits de livraison avec l'IA. Réduisez vos coûts logistiques et améliorez la satisfaction client grâce à des itinéraires intelligents.",
            "keywords": "optimisation logistique, IA transport, itinéraires intelligents, livraison optimisée, efficacité logistique",
            "featured_image": "/static/images/innovation.svg",
            "content": """
<h2>La logistique intelligente : Un enjeu majeur en 2024</h2>
<p>Face à l'augmentation des coûts et des exigences clients, l'optimisation des itinéraires de livraison devient cruciale. L'IA offre des solutions innovantes pour relever ces défis.</p>

<h2>3 Innovations IA pour votre logistique</h2>
<div class="solution-card mb-4">
    <h3>1. Optimisation dynamique des tournées</h3>
    <p>Maximisez l'efficacité de vos livraisons avec :</p>
    <ul>
        <li>Calcul en temps réel des meilleurs itinéraires</li>
        <li>Prise en compte du trafic et des contraintes</li>
        <li>Adaptation automatique aux imprévus</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>2. Prévision de la demande</h3>
    <p>Anticipez les besoins grâce à :</p>
    <ul>
        <li>Analyse prédictive des commandes</li>
        <li>Optimisation des ressources</li>
        <li>Planification intelligente des capacités</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>3. Suivi en temps réel</h3>
    <p>Pilotez votre activité avec précision :</p>
    <ul>
        <li>Tracking GPS intelligent</li>
        <li>Alertes automatiques d'incidents</li>
        <li>Communication client automatisée</li>
    </ul>
</div>

<h2>Résultats prouvés</h2>
<div class="results-section">
    <ul>
        <li><strong>-25%</strong> de coûts de transport</li>
        <li><strong>+35%</strong> de livraisons par jour</li>
        <li><strong>-30%</strong> d'émissions CO2</li>
    </ul>
</div>

<h2>Transformez votre logistique</h2>
<p>Ne laissez pas les coûts logistiques éroder vos marges. Découvrez comment notre solution IA peut optimiser vos opérations de livraison.</p>

<div class="cta-section">
    <a href="/formulaire" class="btn btn-primary">Obtenir mon audit gratuit</a>
</div>
"""
        },
        {
            "sector": "Production",
            "title": "Contrôle qualité automatisé : L'IA et la vision par ordinateur au service de la qualité",
            "meta_description": "Découvrez comment l'IA et la vision par ordinateur révolutionnent le contrôle qualité. Réduisez les erreurs et optimisez votre production grâce à l'automatisation intelligente.",
            "keywords": "contrôle qualité IA, vision par ordinateur, automatisation qualité, inspection automatisée, production intelligente",
            "featured_image": "/static/images/innovation.svg",
            "content": """
<h2>Le contrôle qualité à l'ère de l'IA</h2>
<p>Dans un contexte de production exigeant, la qualité est devenue un enjeu stratégique. L'IA et la vision par ordinateur transforment radicalement les processus de contrôle qualité.</p>

<h2>3 Innovations IA pour votre contrôle qualité</h2>
<div class="solution-card mb-4">
    <h3>1. Inspection visuelle automatisée</h3>
    <p>Détectez les défauts avec précision grâce à :</p>
    <ul>
        <li>Analyse en temps réel des produits</li>
        <li>Détection des micro-défauts</li>
        <li>Classification automatique des anomalies</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>2. Maintenance prédictive</h3>
    <p>Anticipez les problèmes de qualité avec :</p>
    <ul>
        <li>Surveillance continue des équipements</li>
        <li>Prédiction des pannes potentielles</li>
        <li>Optimisation des interventions</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>3. Traçabilité intelligente</h3>
    <p>Suivez votre production de bout en bout :</p>
    <ul>
        <li>Identification unique des produits</li>
        <li>Historique complet de fabrication</li>
        <li>Analyse des tendances qualité</li>
    </ul>
</div>

<h2>Résultats prouvés</h2>
<div class="results-section">
    <ul>
        <li><strong>-90%</strong> de défauts non détectés</li>
        <li><strong>+40%</strong> de productivité</li>
        <li><strong>-60%</strong> de coûts de non-qualité</li>
    </ul>
</div>

<h2>Optimisez votre contrôle qualité</h2>
<p>Ne laissez plus les défauts impacter votre réputation. Découvrez comment notre solution IA peut transformer votre contrôle qualité.</p>

<div class="cta-section">
    <a href="/formulaire" class="btn btn-primary">Demander une démonstration</a>
</div>
"""
        },
        {
            "sector": "IT",
            "title": "Sécurité renforcée : L'IA comme bouclier pour vos données",
            "meta_description": "Protégez vos systèmes IT avec l'intelligence artificielle. Détectez les menaces en temps réel et renforcez votre cybersécurité grâce à l'IA.",
            "keywords": "cybersécurité IA, protection données, détection menaces, sécurité IT, intelligence artificielle sécurité",
            "featured_image": "/static/images/innovation.svg",
            "content": """
<h2>La cybersécurité nouvelle génération</h2>
<p>Face à des menaces toujours plus sophistiquées, l'IA devient indispensable pour protéger efficacement vos systèmes et vos données.</p>

<h2>3 Solutions IA pour votre cybersécurité</h2>
<div class="solution-card mb-4">
    <h3>1. Détection avancée des menaces</h3>
    <p>Protégez votre infrastructure avec :</p>
    <ul>
        <li>Analyse comportementale en temps réel</li>
        <li>Détection des anomalies réseau</li>
        <li>Prévention des intrusions</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>2. Protection des données intelligente</h3>
    <p>Sécurisez vos informations grâce à :</p>
    <ul>
        <li>Cryptage adaptatif</li>
        <li>Classification automatique des données</li>
        <li>Gestion des accès contextuelle</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>3. Réponse automatisée aux incidents</h3>
    <p>Réagissez instantanément avec :</p>
    <ul>
        <li>Isolation automatique des menaces</li>
        <li>Restauration intelligente des systèmes</li>
        <li>Analyse post-incident</li>
    </ul>
</div>

<h2>Impact sur votre sécurité</h2>
<div class="results-section">
    <ul>
        <li><strong>-95%</strong> de faux positifs</li>
        <li><strong>+80%</strong> de menaces détectées</li>
        <li><strong>-60%</strong> de temps de réponse</li>
    </ul>
</div>

<h2>Renforcez votre cybersécurité</h2>
<p>Ne laissez pas votre entreprise vulnérable aux cyberattaques. Découvrez comment notre solution IA peut protéger vos actifs numériques.</p>

<div class="cta-section">
    <a href="/formulaire" class="btn btn-primary">Obtenir mon audit sécurité</a>
</div>
"""
        },
        {
            "sector": "Vente",
            "title": "CRM intelligent : Priorisez vos opportunités et boostez vos ventes avec l'IA",
            "meta_description": "Optimisez votre processus commercial avec l'IA. Identifiez les meilleures opportunités et augmentez vos conversions grâce au CRM intelligent.",
            "keywords": "CRM IA, ventes intelligence artificielle, opportunités commerciales, conversion clients, prospection IA",
            "featured_image": "/static/images/innovation.svg",
            "content": """
<h2>La vente à l'ère de l'intelligence artificielle</h2>
<p>Dans un marché hautement compétitif, l'IA transforme la manière dont les entreprises identifient, qualifient et convertissent leurs opportunités commerciales.</p>

<h2>3 Innovations IA pour vos ventes</h2>
<div class="solution-card mb-4">
    <h3>1. Qualification intelligente des leads</h3>
    <p>Identifiez vos meilleures opportunités avec :</p>
    <ul>
        <li>Scoring prédictif des prospects</li>
        <li>Analyse comportementale</li>
        <li>Prédiction des taux de conversion</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>2. Personnalisation des interactions</h3>
    <p>Adaptez votre approche commerciale grâce à :</p>
    <ul>
        <li>Recommandations produits intelligentes</li>
        <li>Timing optimal de contact</li>
        <li>Personnalisation des messages</li>
    </ul>
</div>

<div class="solution-card mb-4">
    <h3>3. Automatisation du suivi commercial</h3>
    <p>Optimisez votre processus de vente :</p>
    <ul>
        <li>Priorisation automatique des actions</li>
        <li>Génération de devis intelligente</li>
        <li>Prévisions de ventes précises</li>
    </ul>
</div>

<h2>Résultats commerciaux</h2>
<div class="results-section">
    <ul>
        <li><strong>+45%</strong> de taux de conversion</li>
        <li><strong>-30%</strong> de cycle de vente</li>
        <li><strong>+60%</strong> de productivité commerciale</li>
    </ul>
</div>

<h2>Transformez votre approche commerciale</h2>
<p>Ne laissez plus passer d'opportunités. Découvrez comment notre solution IA peut révolutionner votre processus de vente.</p>

<div class="cta-section">
    <a href="/formulaire" class="btn btn-primary">Booster mes ventes</a>
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
