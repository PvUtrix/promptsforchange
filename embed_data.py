#!/usr/bin/env python3

"""
Script to embed posts_metadata.json directly into the HTML file
This ensures the data is always available even if the JSON file isn't served
"""

import json
import re

def embed_data():
    try:
        # Read the JSON data
        with open('posts_metadata.json', 'r', encoding='utf-8') as f:
            posts_data = json.load(f)
        
        print(f"📊 Loaded {posts_data['metadata']['total_posts']} posts")
        
        # Read the HTML file
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Create the embedded data script
        embedded_script = f"""
<script>
// Embedded posts data - fallback when JSON file is not accessible
window.embeddedPostsData = {json.dumps(posts_data, ensure_ascii=False, indent=2)};
console.log('📊 Embedded posts data loaded:', window.embeddedPostsData.metadata.total_posts, 'posts');
</script>
"""
        
        # Insert the embedded data before the closing </head> tag
        if '</head>' in html_content:
            html_content = html_content.replace('</head>', f'{embedded_script}\n</head>')
        else:
            # If no </head> tag, add before </body>
            html_content = html_content.replace('</body>', f'{embedded_script}\n</body>')
        
        # Write the updated HTML
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("✅ Data embedded successfully into index.html")
        print("📁 File size:", len(html_content), "bytes")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Make sure posts_metadata.json exists")
    except json.JSONDecodeError as e:
        print(f"❌ JSON Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    embed_data()
