import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db
from models.blog import BlogPost
import slugify
from datetime import datetime

def generate_seo_blog_posts():
    print("Starting blog post generation...")
    
    # Only include Finance and Logistique posts
    finance_logistique_posts = [
        {
            "sector": "Finance",
            "title": "La Révolution de la Comptabilité par l'IA : Automatisation et Précision en 2024",
            "meta_description": "Découvrez comment l'IA transforme la comptabilité traditionnelle en processus automatisés et précis. Guide complet avec études de cas et ROI détaillé.",
            "keywords": "automatisation comptable, IA finance, facturation automatique, comptabilité digitale, gestion financière IA",
            "featured_image": "/static/images/innovation.svg",
            "content": open("Pasted-La-R-volution-de-la-Comptabilit-par-l-IA-Automatisation-et-Pr-cision-en-2024-La-comptabilit-tra-1734365004379.txt").read()
        },
        {
            "sector": "Logistique",
            "title": "Optimisation Logistique en 2024 : L'IA pour Transformer Vos Opérations",
            "meta_description": "Découvrez comment l'IA révolutionne la logistique en 2024. Solutions concrètes pour optimiser vos livraisons, réduire vos coûts et améliorer votre performance environnementale.",
            "keywords": "optimisation logistique, IA transport, supply chain intelligente, efficacité livraison, logistique durable",
            "featured_image": "/static/images/innovation.svg",
            "content": open("Pasted-Optimisation-Logistique-en-2024-L-IA-pour-Transformer-Vos-Op-rations-En-2024-la-logistique-intel-1734364865757.txt").read()
        }
    ]

    with app.app_context():
        try:
            # First, clean up existing posts in these sectors
            existing_posts = BlogPost.query.filter(BlogPost.sector.in_(['Finance', 'Logistique'])).all()
            for post in existing_posts:
                db.session.delete(post)
            db.session.commit()
            print(f"Cleaned up {len(existing_posts)} existing posts")

            # Now create new posts
            for post_data in finance_logistique_posts:
                try:
                    # Generate a unique slug
                    base_slug = slugify.slugify(post_data["title"])
                    unique_slug = base_slug
                    counter = 1
                    while BlogPost.query.filter_by(slug=unique_slug).first() is not None:
                        unique_slug = f"{base_slug}-{counter}"
                        counter += 1

                    # Format content with proper markers
                    content_lines = post_data["content"].split('\n')
                    formatted_content = []
                    
                    for line in content_lines:
                        line = line.strip()
                        if line:
                            if line.startswith('1.') or line.startswith('2.') or line.startswith('3.'):
                                # Convert numbered sections to markdown headers
                                formatted_content.append(f"\n# {line.split('.', 1)[1].strip()}\n")
                            elif line.startswith('•'):
                                # Keep bullet points
                                formatted_content.append(line)
                            elif any(metric in line for metric in ['-80%', '-95%', '+30%', '-25%', '+35%']):
                                # Format metrics
                                formatted_content.append(f"\n{line}\n")
                            else:
                                formatted_content.append(line)
                    
                    formatted_content = '\n'.join(formatted_content)
                    
                    new_post = BlogPost(
                        title=post_data["title"],
                        slug=unique_slug,
                        content=formatted_content,
                        sector=post_data["sector"],
                        meta_description=post_data["meta_description"],
                        keywords=post_data["keywords"],
                        created_at=datetime.utcnow(),
                        updated_at=datetime.utcnow(),
                        reading_time=1,
                        featured_image=post_data["featured_image"]
                    )
                    db.session.add(new_post)
                    db.session.commit()
                    print(f"Created post: {post_data['title']}")
                except Exception as e:
                    print(f"Error creating post {post_data['title']}: {str(e)}")
                    db.session.rollback()

        except Exception as e:
            print(f"Error generating blog posts: {str(e)}")
            db.session.rollback()
            raise

if __name__ == "__main__":
    generate_seo_blog_posts()