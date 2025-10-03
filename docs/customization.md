# 🎨 Customization Guide

This guide covers how to customize the Prompts for Change Telegram Mini App to match your brand and requirements.

## 🎯 Overview

The app is built with vanilla HTML, CSS, and JavaScript, making it easy to customize without complex build processes. All customization can be done by editing the source files directly.

## 🎨 Visual Customization

### Color Scheme

#### Primary Colors
Edit the CSS variables in `styles.css`:

```css
:root {
    /* Primary gradient */
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    
    /* Secondary colors */
    --secondary-color: #f8f9fa;
    --accent-color: #28a745;
    --warning-color: #ffc107;
    --danger-color: #dc3545;
    
    /* Text colors */
    --text-primary: #333333;
    --text-secondary: #666666;
    --text-muted: #999999;
    
    /* Background colors */
    --bg-primary: #ffffff;
    --bg-secondary: #f8f9fa;
    --bg-dark: #343a40;
}
```

#### Category Colors
Customize category-specific colors:

```css
.category-badge.prompts {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.category-badge.ai-tools {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.category-badge.philosophical {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.category-badge.technical {
    background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
}

.category-badge.business {
    background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
}

.category-badge.research {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
}

.category-badge.automation {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
}

.category-badge.web-dev {
    background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
}
```

### Typography

#### Font Family
```css
:root {
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-size-base: 16px;
    --font-size-sm: 14px;
    --font-size-lg: 18px;
    --font-size-xl: 24px;
    --font-size-2xl: 32px;
}
```

#### Font Weights
```css
:root {
    --font-weight-light: 300;
    --font-weight-normal: 400;
    --font-weight-medium: 500;
    --font-weight-semibold: 600;
    --font-weight-bold: 700;
}
```

### Layout and Spacing

#### Grid System
```css
:root {
    --grid-gap: 1rem;
    --container-padding: 1rem;
    --section-margin: 2rem;
    --border-radius: 8px;
    --border-radius-lg: 12px;
}
```

#### Responsive Breakpoints
```css
/* Mobile first approach */
@media (min-width: 768px) {
    :root {
        --container-padding: 2rem;
        --grid-gap: 1.5rem;
    }
}

@media (min-width: 1024px) {
    :root {
        --container-padding: 3rem;
        --grid-gap: 2rem;
    }
}
```

## 📱 Content Customization

### Adding New Articles

#### Article Structure
```javascript
{
    id: "unique-post-id",
    title: "Your Article Title",
    category: "category-name",
    content: "Full article content...",
    preview: "Short preview text...",
    readTime: "X min",
    tags: ["tag1", "tag2"], // Optional
    author: "Author Name", // Optional
    date: "2024-01-01" // Optional
}
```

#### Adding to Categories
```javascript
const articlesData = {
    "your-category": [
        {
            id: "new-article",
            title: "New Article",
            category: "your-category",
            content: "Content here...",
            preview: "Preview here...",
            readTime: "2 min"
        }
    ]
};
```

### Category Management

#### Adding New Categories
1. **Update Navigation:**
   ```html
   <button class="nav-tab" data-category="new-category">New Category</button>
   ```

2. **Add Category Data:**
   ```javascript
   const articlesData = {
       "new-category": [
           // articles here
       ]
   };
   ```

3. **Update Category Display:**
   ```javascript
   function getCategoryDisplayName(category) {
       const names = {
           'new-category': 'New Category',
           // ... other categories
       };
       return names[category] || category;
   }
   ```

4. **Add Category Styling:**
   ```css
   .category-badge.new-category {
       background: linear-gradient(135deg, #your-color-1, #your-color-2);
   }
   ```

### Search Customization

#### Search Filters
```javascript
// Add custom search filters
function customSearchFilter(article, searchTerm) {
    // Custom search logic
    return article.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
           article.content.toLowerCase().includes(searchTerm.toLowerCase()) ||
           article.tags.some(tag => tag.toLowerCase().includes(searchTerm.toLowerCase()));
}
```

#### Search Suggestions
```javascript
// Add search suggestions
const searchSuggestions = [
    "AI prompts",
    "Business automation",
    "Technical guides",
    "Research analysis"
];
```

## 🔧 Functionality Customization

### Keyboard Shortcuts

#### Custom Shortcuts
```javascript
document.addEventListener('keydown', function(e) {
    // Custom shortcut: Ctrl/Cmd + S for search
    if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        document.getElementById('searchInput').focus();
    }
    
    // Custom shortcut: Ctrl/Cmd + N for new article
    if ((e.ctrlKey || e.metaKey) && e.key === 'n') {
        e.preventDefault();
        // Add new article functionality
    }
});
```

### Modal Customization

#### Custom Modal Actions
```javascript
// Add custom buttons to modal
function addCustomModalButtons(article) {
    const modalFooter = document.querySelector('.modal-footer');
    
    // Add custom button
    const customButton = document.createElement('button');
    customButton.className = 'btn btn-custom';
    customButton.textContent = 'Custom Action';
    customButton.onclick = () => {
        // Custom action logic
        console.log('Custom action for:', article.title);
    };
    
    modalFooter.appendChild(customButton);
}
```

### Analytics Integration

#### Google Analytics
```html
<!-- Add to <head> section -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

#### Custom Analytics
```javascript
// Track article views
function trackArticleView(article) {
    // Custom analytics tracking
    if (typeof gtag !== 'undefined') {
        gtag('event', 'article_view', {
            'article_id': article.id,
            'article_title': article.title,
            'category': article.category
        });
    }
}
```

## 🌐 Telegram Integration

### Bot Configuration

#### Web App Setup
```javascript
// Initialize Telegram WebApp
const tg = window.Telegram.WebApp;

// Configure app
tg.ready();
tg.expand();

// Set up main button
tg.MainButton.setText('Open in Channel');
tg.MainButton.show();
```

#### Custom Telegram Actions
```javascript
// Custom Telegram button actions
tg.MainButton.onClick(() => {
    // Open article in Telegram channel
    tg.openLink(`https://t.me/promptsforchange`);
});

// Back button handling
tg.BackButton.onClick(() => {
    if (modalOpen) {
        closeModal();
    } else {
        tg.close();
    }
});
```

### Theme Integration

#### Telegram Theme Detection
```javascript
// Detect Telegram theme
function applyTelegramTheme() {
    const tg = window.Telegram.WebApp;
    const theme = tg.colorScheme;
    
    if (theme === 'dark') {
        document.body.classList.add('dark-theme');
    } else {
        document.body.classList.add('light-theme');
    }
}
```

#### Dark Theme CSS
```css
.dark-theme {
    --bg-primary: #1a1a1a;
    --bg-secondary: #2d2d2d;
    --text-primary: #ffffff;
    --text-secondary: #cccccc;
    --text-muted: #999999;
}

.dark-theme .article-card {
    background: var(--bg-secondary);
    border: 1px solid #333333;
}

.dark-theme .modal {
    background: rgba(0, 0, 0, 0.8);
}
```

## 📊 Performance Optimization

### Lazy Loading

#### Image Lazy Loading
```javascript
// Lazy load images
const images = document.querySelectorAll('img[data-src]');
const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.classList.remove('lazy');
            observer.unobserve(img);
        }
    });
});

images.forEach(img => imageObserver.observe(img));
```

#### Content Lazy Loading
```javascript
// Lazy load article content
function loadArticleContent(articleId) {
    // Load content only when needed
    return fetch(`/api/articles/${articleId}`)
        .then(response => response.json())
        .then(data => data.content);
}
```

### Caching

#### Service Worker
```javascript
// Register service worker for caching
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js')
        .then(registration => console.log('SW registered'))
        .catch(error => console.log('SW registration failed'));
}
```

#### Local Storage
```javascript
// Cache articles in localStorage
function cacheArticle(article) {
    const cached = JSON.parse(localStorage.getItem('cached_articles') || '{}');
    cached[article.id] = article;
    localStorage.setItem('cached_articles', JSON.stringify(cached));
}
```

## 🔒 Security Considerations

### Content Security Policy

#### CSP Headers
```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               script-src 'self' 'unsafe-inline' https://telegram.org; 
               style-src 'self' 'unsafe-inline'; 
               img-src 'self' data: https:;">
```

### Input Sanitization

#### Sanitize User Input
```javascript
// Sanitize search input
function sanitizeInput(input) {
    return input
        .replace(/[<>]/g, '') // Remove HTML tags
        .replace(/javascript:/gi, '') // Remove javascript: protocol
        .trim();
}
```

## 🧪 Testing

### Unit Testing

#### Test Structure
```javascript
// Example test for search functionality
function testSearch() {
    const articles = [
        { id: '1', title: 'Test Article', content: 'Test content' }
    ];
    
    const results = searchArticles(articles, 'test');
    assert(results.length === 1);
    assert(results[0].id === '1');
}
```

### Integration Testing

#### Test Deployment
```bash
# Test local deployment
python -m http.server 8000

# Test Docker deployment
docker build -t test-app .
docker run -p 80:80 test-app
```

## 📈 Monitoring

### Error Tracking

#### Error Reporting
```javascript
// Custom error reporting
window.addEventListener('error', function(e) {
    // Send error to monitoring service
    fetch('/api/errors', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            message: e.message,
            filename: e.filename,
            lineno: e.lineno,
            colno: e.colno,
            stack: e.error?.stack
        })
    });
});
```

### Performance Monitoring

#### Performance Metrics
```javascript
// Track performance metrics
function trackPerformance() {
    const navigation = performance.getEntriesByType('navigation')[0];
    
    const metrics = {
        loadTime: navigation.loadEventEnd - navigation.loadEventStart,
        domContentLoaded: navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart,
        firstPaint: performance.getEntriesByName('first-paint')[0]?.startTime,
        firstContentfulPaint: performance.getEntriesByName('first-contentful-paint')[0]?.startTime
    };
    
    // Send metrics to analytics
    console.log('Performance metrics:', metrics);
}
```

## 🚀 Deployment Customization

### Environment Variables

#### Configuration
```javascript
// Environment-specific configuration
const config = {
    development: {
        apiUrl: 'http://localhost:3000',
        debug: true
    },
    production: {
        apiUrl: 'https://api.yourdomain.com',
        debug: false
    }
};

const env = process.env.NODE_ENV || 'development';
const currentConfig = config[env];
```

### Build Optimization

#### Minification
```javascript
// Minify CSS and JS for production
function minifyAssets() {
    // Use tools like UglifyJS, CleanCSS
    // Or build tools like Webpack, Rollup
}
```

---

**Need help with customization?** Check the [main README](../README.md) or open an issue on GitHub.
