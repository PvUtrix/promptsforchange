#!/usr/bin/env python3
"""
Migration script to convert existing JSON posts to markdown files
"""

import json
import yaml
from pathlib import Path
from typing import Dict, Any

def migrate_json_to_markdown():
    """Convert existing JSON posts to markdown files"""
    
    # Load existing data
    json_files = [
        "parsed_posts.json",
        "posts_metadata_complete.json"
    ]
    
    posts_data = None
    
    for json_file in json_files:
        if Path(json_file).exists():
            print(f"📂 Loading data from {json_file}")
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            if isinstance(data, list):
                # Direct posts array
                posts_data = data
            elif isinstance(data, dict) and 'posts' in data:
                # Posts in metadata structure
                posts_data = data['posts']
            else:
                print(f"⚠️  Unknown data structure in {json_file}")
                continue
            
            print(f"✅ Found {len(posts_data)} posts")
            break
    
    if not posts_data:
        print("❌ No posts data found!")
        return
    
    # Create content directory structure
    content_dir = Path("content")
    posts_dir = content_dir / "posts"
    posts_dir.mkdir(parents=True, exist_ok=True)
    
    # Category mapping
    category_dirs = {
        "prompts": "01_prompts",
        "ai-tools": "02_ai_tools", 
        "philosophical": "03_philosophical",
        "technical": "04_technical_guides",
        "business": "05_startup_business",
        "research": "06_research_analysis",
        "automation": "07_automation",
        "web-development": "08_web_development"
    }
    
    # Process each post
    for post in posts_data:
        try:
            # Get category directory
            category = post.get('category', 'uncategorized')
            category_dir = category_dirs.get(category, f"99_{category}")
            post_dir = posts_dir / category_dir
            post_dir.mkdir(exist_ok=True)
            
            # Create markdown file
            post_id = post.get('id', 'unknown')
            md_file = post_dir / f"{post_id}.md"
            
            # Prepare frontmatter
            frontmatter = {
                'id': post.get('id'),
                'title': post.get('title'),
                'category': post.get('category'),
                'preview': post.get('preview'),
                'metadata': post.get('metadata', {})
            }
            
            # Write markdown file
            with open(md_file, 'w', encoding='utf-8') as f:
                # Write frontmatter
                f.write('---\n')
                yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
                f.write('---\n\n')
                
                # Write content
                content = post.get('content', '')
                f.write(content)
            
            print(f"✅ Created {md_file}")
            
        except Exception as e:
            print(f"❌ Error processing post {post.get('id', 'unknown')}: {e}")
    
    print(f"\n🎉 Migration complete! Check {posts_dir} for your markdown files.")

if __name__ == "__main__":
    migrate_json_to_markdown()
