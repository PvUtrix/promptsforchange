#!/usr/bin/env python3
"""
Script to parse Telegram export JSON and convert to enhanced metadata format
"""

import json
import re
from datetime import datetime
from typing import Dict, List, Any

def extract_text_from_entities(text_entities):
    """Extract plain text from Telegram text entities"""
    if isinstance(text_entities, str):
        return text_entities
    
    if isinstance(text_entities, list):
        result = ""
        for entity in text_entities:
            if isinstance(entity, dict):
                if entity.get("type") == "plain":
                    result += entity.get("text", "")
                elif entity.get("type") == "bold":
                    result += entity.get("text", "")
                elif entity.get("type") == "text_link":
                    result += entity.get("text", "")
                else:
                    result += entity.get("text", "")
            else:
                result += str(entity)
        return result
    
    return str(text_entities)

def detect_language(text):
    """Simple language detection based on character patterns"""
    if not text:
        return "en"
    
    # Count Cyrillic characters
    cyrillic_count = len(re.findall(r'[а-яё]', text.lower()))
    
    # Count Latin characters
    latin_count = len(re.findall(r'[a-z]', text.lower()))
    
    if cyrillic_count > latin_count:
        return "ru"
    else:
        return "en"

def categorize_content(text, title=""):
    """Categorize content based on keywords and patterns"""
    text_lower = (text + " " + title).lower()
    
    # AI Tools keywords
    if any(keyword in text_lower for keyword in ["deepseek", "chatgpt", "claude", "grok", "qwen", "ai model", "нейронка", "ии"]):
        return "ai-tools"
    
    # Prompts keywords
    if any(keyword in text_lower for keyword in ["prompt", "промпт", "act as", "acting as", "you are"]):
        return "prompts"
    
    # Technical keywords
    if any(keyword in text_lower for keyword in ["data", "entropy", "technical", "code", "programming", "api", "database"]):
        return "technical"
    
    # Business keywords
    if any(keyword in text_lower for keyword in ["startup", "business", "replit", "n8n", "automation", "cost", "portal"]):
        return "business"
    
    # Philosophical keywords
    if any(keyword in text_lower for keyword in ["consciousness", "сознание", "philosophy", "meaning", "life", "душа", "смысл"]):
        return "philosophical"
    
    # Research keywords
    if any(keyword in text_lower for keyword in ["research", "analysis", "climate", "war", "constitution", "rules"]):
        return "research"
    
    # Automation keywords
    if any(keyword in text_lower for keyword in ["automation", "workflow", "agent", "browser"]):
        return "automation"
    
    # Web development keywords
    if any(keyword in text_lower for keyword in ["website", "web", "development", "html", "css", "javascript"]):
        return "web-dev"
    
    return "business"  # Default category

def generate_title(text, post_id):
    """Generate a title from text content"""
    if not text:
        return f"Post {post_id}"
    
    # Take first line or first 50 characters
    lines = text.split('\n')
    first_line = lines[0].strip()
    
    if len(first_line) > 50:
        return first_line[:47] + "..."
    
    return first_line or f"Post {post_id}"

def calculate_read_time(word_count):
    """Calculate read time based on word count"""
    if word_count < 50:
        return "1 min"
    elif word_count < 150:
        return "2 min"
    elif word_count < 300:
        return "3 min"
    elif word_count < 500:
        return "5 min"
    elif word_count < 800:
        return "8 min"
    else:
        return "10+ min"

def extract_tags(text, title=""):
    """Extract relevant tags from content"""
    text_lower = (text + " " + title).lower()
    tags = []
    
    # Common tag patterns
    tag_patterns = {
        "ai": ["ai", "ии", "artificial intelligence"],
        "prompts": ["prompt", "промпт"],
        "automation": ["automation", "автоматизация", "workflow"],
        "business": ["business", "startup", "entrepreneur"],
        "technical": ["technical", "code", "programming", "data"],
        "philosophy": ["philosophy", "consciousness", "сознание", "meaning"],
        "research": ["research", "analysis", "study"],
        "tutorial": ["tutorial", "guide", "how to"],
        "tools": ["tool", "platform", "service"],
        "free": ["free", "бесплатно", "open source"],
        "deepseek": ["deepseek"],
        "n8n": ["n8n"],
        "replit": ["replit"],
        "chatgpt": ["chatgpt"],
        "claude": ["claude"],
        "grok": ["grok"],
        "qwen": ["qwen"]
    }
    
    for tag, keywords in tag_patterns.items():
        if any(keyword in text_lower for keyword in keywords):
            tags.append(tag)
    
    return tags[:5]  # Limit to 5 tags

def parse_telegram_export():
    """Parse the Telegram export and convert to enhanced metadata format"""
    
    # Read the Telegram export
    with open('result.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    posts = []
    post_counter = 1
    
    for message in data.get('messages', []):
        # Skip service messages and empty messages
        if message.get('type') != 'message' or not message.get('text'):
            continue
        
        # Extract text content
        text_content = extract_text_from_entities(message.get('text', ''))
        
        if not text_content or len(text_content.strip()) < 10:
            continue
        
        # Skip very short messages
        if len(text_content.strip()) < 20:
            continue
        
        # Generate post ID
        post_id = f"post{post_counter}"
        post_counter += 1
        
        # Generate title
        title = generate_title(text_content, post_id)
        
        # Detect language
        language = detect_language(text_content)
        
        # Categorize content
        category = categorize_content(text_content, title)
        
        # Calculate word count
        word_count = len(text_content.split())
        
        # Generate preview (first 150 characters)
        preview = text_content[:150] + "..." if len(text_content) > 150 else text_content
        
        # Extract tags
        tags = extract_tags(text_content, title)
        
        # Determine difficulty
        if word_count < 100:
            difficulty = "beginner"
        elif word_count < 300:
            difficulty = "intermediate"
        else:
            difficulty = "advanced"
        
        # Determine content type
        content_type = "message"
        if "prompt" in text_content.lower() or "промпт" in text_content.lower():
            content_type = "prompt"
        elif "tutorial" in text_content.lower() or "guide" in text_content.lower():
            content_type = "tutorial"
        elif "analysis" in text_content.lower() or "research" in text_content.lower():
            content_type = "analysis"
        elif "recommendation" in text_content.lower() or "recommend" in text_content.lower():
            content_type = "recommendation"
        
        # Parse date
        date_str = message.get('date', '2024-01-01')
        if 'T' in date_str:
            date_str = date_str.split('T')[0]
        
        # Create post object
        post = {
            "id": post_id,
            "title": title,
            "category": category,
            "content": text_content,
            "preview": preview,
            "metadata": {
                "word_count": word_count,
                "read_time": calculate_read_time(word_count),
                "language": language,
                "content_type": content_type,
                "difficulty": difficulty,
                "tags": tags,
                "source": {
                    "type": "original",
                    "url": f"https://t.me/promptsforchange/{message.get('id', post_counter)}",
                    "author": "Paul (Tango.Vision)"
                },
                "engagement": {
                    "views": 0,
                    "likes": 0,
                    "shares": 0
                },
                "timestamps": {
                    "created": date_str,
                    "updated": date_str,
                    "published": date_str
                },
                "analysis": {
                    "summary": f"Content from Telegram channel message {message.get('id', post_counter)}",
                    "key_points": [],
                    "related_posts": []
                }
            }
        }
        
        posts.append(post)
    
    return posts

if __name__ == "__main__":
    posts = parse_telegram_export()
    print(f"Parsed {len(posts)} posts from Telegram export")
    
    # Save to file
    with open('parsed_posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    
    print("Saved parsed posts to parsed_posts.json")
