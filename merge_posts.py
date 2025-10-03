#!/usr/bin/env python3
"""
Script to merge parsed Telegram posts with existing metadata structure
"""

import json
from datetime import datetime

def merge_posts():
    """Merge parsed posts with existing metadata structure"""
    
    # Read existing metadata structure
    with open('posts_metadata.json', 'r', encoding='utf-8') as f:
        existing_data = json.load(f)
    
    # Read parsed posts
    with open('parsed_posts.json', 'r', encoding='utf-8') as f:
        parsed_posts = json.load(f)
    
    # Update metadata
    existing_data['metadata']['total_posts'] = len(parsed_posts)
    existing_data['metadata']['updated'] = datetime.now().strftime('%Y-%m-%d')
    
    # Replace posts array with all parsed posts
    existing_data['posts'] = parsed_posts
    
    # Save complete enhanced metadata
    with open('posts_metadata_complete.json', 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Merged {len(parsed_posts)} posts into complete metadata structure")
    print(f"📊 Categories: {len(existing_data['categories'])}")
    print(f"📝 Total posts: {len(parsed_posts)}")
    
    # Count posts by category
    category_counts = {}
    for post in parsed_posts:
        category = post['category']
        category_counts[category] = category_counts.get(category, 0) + 1
    
    print("\n📈 Posts by category:")
    for category, count in sorted(category_counts.items()):
        print(f"  {category}: {count} posts")
    
    return existing_data

if __name__ == "__main__":
    complete_data = merge_posts()
    print("\n🎉 Complete enhanced metadata structure created!")
    print("📁 Saved to: posts_metadata_complete.json")
