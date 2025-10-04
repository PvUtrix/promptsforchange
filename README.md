# 📚 Prompts for Change

A modern, responsive Telegram Mini App that serves as a comprehensive library for AI prompts, tools, and knowledge. Built with a hybrid markdown + JSON structure for easy content management and production reliability.

## ✨ Features

- **📱 Mobile-First Design**: Optimized for Telegram's mobile interface
- **🔍 Advanced Search**: Search across all articles by title, content, or keywords
- **📂 Category Navigation**: Browse articles by category (Prompts, AI Tools, Business, etc.)
- **📖 Article Reader**: Full-screen modal for reading articles
- **📊 Statistics**: Real-time article counts and filtering stats
- **🎨 Modern UI**: Beautiful gradient design with smooth animations
- **⌨️ Keyboard Shortcuts**: Ctrl/Cmd+K for search, Escape to close modals
- **📋 Copy Functionality**: Copy article content to clipboard
- **🔗 Telegram Integration**: Open articles in your Telegram channel

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Node.js (optional, for npm scripts)

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/prompts-for-change.git
cd prompts-for-change

# Install Python dependencies
pip install pyyaml

# Build the application
npm run build
# or
python3 scripts/build_system.py

# Start local development server
npm run dev
# or
python3 -m http.server 8000
```

## 📁 Project Structure

```
prompts-for-change/
├── content/                    # Source content (markdown files)
│   ├── posts/                 # All posts organized by category
│   │   ├── 01_prompts/        # AI Prompts
│   │   ├── 02_ai_tools/       # AI Tools
│   │   ├── 03_philosophical/  # Philosophical content
│   │   ├── 04_technical_guides/
│   │   ├── 05_startup_business/
│   │   ├── 06_research_analysis/
│   │   ├── 07_automation/
│   │   └── 08_web_development/
│   └── categories.json        # Category definitions
├── scripts/                   # Build and migration scripts
│   ├── build_system.py        # Main build system
│   └── migrate_to_markdown.py # Migration utilities
├── docs/                      # Documentation
├── index.html                 # Main application
├── script.js                  # App logic
├── styles.css                 # Styling
└── package.json              # Project configuration
```

## 🛠️ Development

### Adding New Posts
1. Create a new `.md` file in the appropriate category folder under `content/posts/`
2. Add frontmatter with metadata:

```markdown
---
id: my-post
title: "My Awesome Post"
category: "prompts"
preview: "Short preview text..."
metadata:
  word_count: 150
  read_time: "2 min"
  tags: ["ai", "prompts"]
  # ... additional metadata
---

# My Awesome Post

This is the actual content of the post...
```

3. Run the build system:
```bash
npm run build
```

### Available Scripts
- `npm run build` - Build the application from markdown files
- `npm run dev` - Build and start development server
- `npm run migrate` - Convert JSON posts to markdown (one-time use)
- `npm run start` - Start local server only

## 🎯 Content Categories

### 📝 Prompts
AI prompts and prompt engineering content

### 🤖 AI Tools
AI tools, platforms, and recommendations

### 🧠 Philosophical
Abstract, experimental, and philosophical content

### 🔧 Technical
Technical tutorials and guides

### 💼 Business
Business, entrepreneurship, and startup content

### 🔬 Research
Research, analysis, and deep dives

### ⚙️ Automation
Automation tools and workflows

### 🌐 Web Development
Web development and coding

## 🚀 Deployment

### Static Hosting (Recommended)
The application is built as static files and can be deployed to any static hosting service:

- **GitHub Pages**: Push to main branch, enable Pages
- **Netlify**: Connect repository, auto-deploy
- **Vercel**: Import repository, deploy
- **Any CDN**: Upload built files

### Docker (Optional)
```bash
# Build Docker image
docker build -t prompts-for-change .

# Run container
docker run -p 80:80 prompts-for-change
```

## 🎨 Customization

### Categories
Edit `content/categories.json` to modify categories:

```json
{
  "categories": {
    "my-category": {
      "name": "My Category",
      "description": "Description here",
      "icon": "🎯",
      "color": "#FF6B6B"
    }
  }
}
```

### Styling
Modify CSS variables in `styles.css`:

```css
/* Main gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Category colors */
.category-badge {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

## 📊 Performance

- **Lightweight**: No external dependencies
- **Fast Loading**: Optimized static files with embedded data
- **Mobile Optimized**: Responsive design
- **SEO Friendly**: Semantic HTML structure
- **Accessible**: WCAG compliant design

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### How to Contribute
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Telegram WebApp API for seamless integration
- Modern CSS Grid and Flexbox for responsive design
- Vanilla JavaScript for maximum compatibility
- Open source community for inspiration and tools

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/prompts-for-change/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/prompts-for-change/discussions)

---

**Built with ❤️ for the AI community**