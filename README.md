# 📚 Prompts for Change

A modern, responsive Telegram Mini App that serves as a comprehensive library for AI prompts, tools, and knowledge. Built with vanilla HTML, CSS, and JavaScript for maximum compatibility and performance.

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

### Option 1: Deploy to GitHub Pages
1. Fork this repository
2. Go to Settings → Pages
3. Select source: Deploy from a branch
4. Choose main branch
5. Your app will be available at `https://yourusername.github.io/prompts-for-change`

### Option 2: Deploy to Netlify
1. Connect your GitHub repository to Netlify
2. Set build command: `echo "No build required"`
3. Set publish directory: `/`
4. Deploy

### Option 3: Deploy to Vercel
1. Import your repository to Vercel
2. Set framework preset to "Other"
3. Deploy

### Local Development
```bash
# Clone the repository
git clone https://github.com/yourusername/prompts-for-change.git
cd prompts-for-change

# Start a local server
python -m http.server 8000
# or
npx serve .
# or
php -S localhost:8000

# Open http://localhost:8000 in your browser
```

## 📁 Project Structure

```
prompts-for-change/
├── index.html              # Main HTML file
├── styles.css              # CSS styles and responsive design
├── script.js               # JavaScript functionality and data
├── package.json            # Project metadata
├── Dockerfile              # Docker configuration
├── nginx.conf              # Nginx configuration
├── .gitignore              # Git ignore rules
├── LICENSE                  # MIT License
├── CONTRIBUTING.md          # Contribution guidelines
├── README.md               # This file
└── docs/                   # Documentation
    ├── deployment.md       # Deployment guide
    └── customization.md    # Customization guide
```

## 🎯 Content Categories

### 📝 Prompts
AI prompts and prompt engineering content:
- Limiting beliefs prompts for entrepreneurs
- Google Sheets with useful prompts
- Human-like content generation prompts
- Summarization and learning prompts
- DeepSeek prompt cheat sheets

### 🤖 AI Tools
AI tools, platforms, and recommendations:
- DeepSeek and Qwen recommendations
- Browser automation tools
- AI agents platforms
- Latest AI model releases

### 🧠 Philosophical
Abstract, experimental, and philosophical content:
- DeepSeek philosophical reflections
- Life archetypes and soul prompts
- Music personality analysis
- Society and divine game concepts

### 🔧 Technical
Technical tutorials and guides:
- Data entropy articles
- AI development workflows
- MVP planning guides
- Development best practices

### 💼 Business
Business, entrepreneurship, and startup content:
- Channel introductions
- Innovation portals
- Automation tutorials
- Business commandments
- Development bounties

### 🔬 Research
Research, analysis, and deep dives:
- Climate change analysis
- Sustainable living constitutions
- Remote work vs AI replacement
- AI education mandates
- Future research insights

### ⚙️ Automation
Automation tools and workflows:
- Business automation services
- Virtual assistant development
- Workflow optimization

### 🌐 Web Development
Web development and coding:
- Website creation guides
- QR code generators
- Development streams
- Cost-effective solutions

## 🛠️ Customization

### Adding New Articles
Edit the `articlesData` object in `script.js`:

```javascript
const articlesData = {
    "prompts": [
        {
            id: "unique-post-id",
            title: "Your Article Title",
            category: "prompts",
            content: "Full article content...",
            preview: "Short preview text...",
            readTime: "2 min"
        }
        // ... more articles
    ]
    // ... more categories
};
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

### Telegram Integration
Update the Telegram link in the modal:

```javascript
tg.openLink(`https://t.me/promptsforchange`);
```

## 🐳 Docker Deployment

### Build and Run
```bash
# Build the Docker image
docker build -t prompts-for-change .

# Run the container
docker run -p 80:80 prompts-for-change
```

### Docker Compose
```yaml
version: '3.8'
services:
  prompts-for-change:
    build: .
    ports:
      - "80:80"
    restart: unless-stopped
```

## 📊 Performance

- **Lightweight**: No external dependencies
- **Fast Loading**: Optimized static files
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
- **Email**: For security issues or private matters

---

**Built with ❤️ for the AI community**
