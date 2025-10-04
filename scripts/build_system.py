#!/usr/bin/env python3
"""
Build system for Prompts for Change
Converts markdown files to JSON and generates the final application
"""

import os
import json
import yaml
import glob
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

class PostBuilder:
    def __init__(self, content_dir: str = "../content", output_dir: str = ".."):
        self.content_dir = Path(content_dir)
        self.output_dir = Path(output_dir)
        self.posts_dir = self.content_dir / "posts"
        
    def load_categories(self) -> Dict[str, Any]:
        """Load category definitions"""
        categories_file = self.content_dir / "categories.json"
        if categories_file.exists():
            with open(categories_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Default categories based on your current structure
        return {
            "metadata": {
                "version": "2.0",
                "created": datetime.now().isoformat(),
                "description": "Category definitions for Prompts for Change"
            },
            "categories": {
                "prompts": {
                    "name": "AI Prompts",
                    "description": "Effective prompts for various AI applications",
                    "icon": "🤖",
                    "color": "#3B82F6"
                },
                "ai-tools": {
                    "name": "AI Tools", 
                    "description": "AI platforms, models, and tools",
                    "icon": "🛠️",
                    "color": "#10B981"
                },
                "philosophical": {
                    "name": "Philosophical",
                    "description": "Deep thoughts and philosophical explorations", 
                    "icon": "🧠",
                    "color": "#8B5CF6"
                },
                "technical": {
                    "name": "Technical Guides",
                    "description": "Technical tutorials and guides",
                    "icon": "⚙️", 
                    "color": "#F59E0B"
                },
                "business": {
                    "name": "Startup & Business",
                    "description": "Business insights and entrepreneurship",
                    "icon": "💼",
                    "color": "#EF4444"
                },
                "research": {
                    "name": "Research & Analysis", 
                    "description": "Research findings and analysis",
                    "icon": "📊",
                    "color": "#06B6D4"
                },
                "automation": {
                    "name": "Automation",
                    "description": "Automation tools and workflows",
                    "icon": "🔄",
                    "color": "#8B5CF6"
                },
                "web-development": {
                    "name": "Web Development",
                    "description": "Web development and coding",
                    "icon": "🌐",
                    "color": "#10B981"
                }
            }
        }
    
    def parse_markdown_post(self, file_path: Path) -> Dict[str, Any]:
        """Parse a markdown file with frontmatter"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split frontmatter and content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter_text = parts[1].strip()
                markdown_content = parts[2].strip()
                
                # Parse YAML frontmatter
                try:
                    frontmatter = yaml.safe_load(frontmatter_text)
                except yaml.YAMLError as e:
                    print(f"Error parsing frontmatter in {file_path}: {e}")
                    frontmatter = {}
            else:
                frontmatter = {}
                markdown_content = content
        else:
            frontmatter = {}
            markdown_content = content
        
        # Extract basic info
        post_id = frontmatter.get('id', file_path.stem)
        title = frontmatter.get('title', 'Untitled')
        category = frontmatter.get('category', 'uncategorized')
        preview = frontmatter.get('preview', markdown_content[:200] + '...')
        metadata = frontmatter.get('metadata', {})
        
        return {
            "id": post_id,
            "title": title,
            "category": category,
            "content": markdown_content,
            "preview": preview,
            "metadata": metadata
        }
    
    def load_all_posts(self) -> List[Dict[str, Any]]:
        """Load all markdown posts from the posts directory"""
        posts = []
        
        if not self.posts_dir.exists():
            print(f"Posts directory {self.posts_dir} does not exist")
            return posts
        
        # Find all markdown files
        for md_file in self.posts_dir.rglob("*.md"):
            try:
                post = self.parse_markdown_post(md_file)
                posts.append(post)
                print(f"Loaded post: {post['id']} - {post['title']}")
            except Exception as e:
                print(f"Error loading {md_file}: {e}")
        
        # Sort posts by ID
        posts.sort(key=lambda x: x['id'])
        return posts
    
    def generate_metadata_json(self, posts: List[Dict[str, Any]], categories: Dict[str, Any]) -> Dict[str, Any]:
        """Generate the complete metadata JSON"""
        return {
            "metadata": {
                "version": "2.0",
                "created": datetime.now().isoformat(),
                "total_posts": len(posts),
                "categories": len(categories.get('categories', {})),
                "description": "Enhanced posts structure with comprehensive metadata for Prompts for Change channel",
                "updated": datetime.now().isoformat()
            },
            "categories": categories.get('categories', {}),
            "posts": posts
        }
    
    def embed_data_in_html(self, metadata: Dict[str, Any]) -> str:
        """Embed the metadata directly in the HTML file"""
        html_file = self.output_dir / "index.html"
        
        if not html_file.exists():
            print(f"HTML file {html_file} not found")
            return ""
        
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Find the script tag and add embedded data
        script_tag = f"""
    <script>
        // Embedded posts data
        window.embeddedPostsData = {json.dumps(metadata, indent=2)};
    </script>
"""
        
        # Insert before the closing head tag
        if '</head>' in html_content:
            html_content = html_content.replace('</head>', f'{script_tag}</head>')
        else:
            # If no head tag, add before body
            html_content = html_content.replace('<body>', f'{script_tag}<body>')
        
        return html_content
    
    def build(self):
        """Main build process"""
        print("🚀 Starting build process...")
        
        # Load categories
        categories = self.load_categories()
        print(f"📂 Loaded {len(categories.get('categories', {}))} categories")
        
        # Load all posts
        posts = self.load_all_posts()
        print(f"📝 Loaded {len(posts)} posts")
        
        if not posts:
            print("❌ No posts found! Make sure markdown files are in content/posts/")
            return
        
        # Generate metadata
        metadata = self.generate_metadata_json(posts, categories)
        
        # Save metadata JSON
        metadata_file = self.output_dir / "posts_metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        print(f"💾 Saved metadata to {metadata_file}")
        
        # Embed data in HTML
        html_with_data = self.embed_data_in_html(metadata)
        if html_with_data:
            with open(self.output_dir / "index.html", 'w', encoding='utf-8') as f:
                f.write(html_with_data)
            print("🔗 Embedded data in HTML")
        
        print("✅ Build complete!")

def main():
    builder = PostBuilder()
    builder.build()

if __name__ == "__main__":
    main()
