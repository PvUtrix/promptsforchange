# Contributing to Prompts for Change

Thank you for your interest in contributing to Prompts for Change! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues
- Use the GitHub issue tracker to report bugs or request features
- Provide clear descriptions and steps to reproduce issues
- Include relevant system information when applicable

### Suggesting Content
- Submit new prompts, AI tools, or knowledge articles
- Ensure content is original or properly attributed
- Follow the existing content structure and format

### Code Contributions
- Fork the repository
- Create a feature branch (`git checkout -b feature/amazing-feature`)
- Make your changes
- Test your changes thoroughly
- Submit a pull request with a clear description

## 📝 Content Guidelines

### Adding New Articles
1. **Choose the right category**:
   - `prompts/` - AI prompts and prompt engineering
   - `ai-tools/` - AI tools, platforms, and recommendations
   - `philosophical/` - Abstract and philosophical content
   - `technical/` - Technical guides and tutorials
   - `business/` - Business and startup content
   - `research/` - Research and analysis
   - `automation/` - Automation tools and workflows
   - `web-dev/` - Web development content

2. **Content Structure**:
   ```javascript
   {
       id: "unique-post-id",
       title: "Clear, descriptive title",
       category: "category-name",
       content: "Full article content...",
       preview: "Short preview text...",
       readTime: "X min"
   }
   ```

3. **Quality Standards**:
   - Content should be valuable and actionable
   - Use clear, concise language
   - Include proper attribution for external sources
   - Ensure content is original or properly licensed

### Code Standards
- Follow existing code style and conventions
- Add comments for complex functionality
- Ensure mobile responsiveness
- Test across different browsers and devices

## 🚀 Development Setup

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/prompts-for-change.git
   cd prompts-for-change
   ```

2. Start a local server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx serve .
   
   # Using PHP
   php -S localhost:8000
   ```

3. Open `http://localhost:8000` in your browser

### Testing
- Test all functionality in the browser
- Verify mobile responsiveness
- Check search and filtering features
- Test modal interactions and keyboard shortcuts

## 📋 Pull Request Process

1. **Before submitting**:
   - Ensure your changes don't break existing functionality
   - Test thoroughly on different devices
   - Update documentation if needed

2. **Pull request template**:
   - Describe what changes you made
   - Explain why the changes were necessary
   - Include screenshots for UI changes
   - Reference any related issues

3. **Review process**:
   - All PRs will be reviewed by maintainers
   - Address feedback promptly
   - Be open to suggestions and improvements

## 🎯 Areas for Contribution

### High Priority
- [ ] Content organization and categorization
- [ ] Search functionality improvements
- [ ] Mobile UI/UX enhancements
- [ ] Performance optimizations
- [ ] Accessibility improvements

### Medium Priority
- [ ] New content categories
- [ ] Advanced filtering options
- [ ] Article bookmarking system
- [ ] Export functionality
- [ ] Analytics integration

### Low Priority
- [ ] Theme customization
- [ ] Offline support
- [ ] Multi-language support
- [ ] User authentication
- [ ] Comment system

## 📚 Documentation

### Code Documentation
- Comment complex functions and algorithms
- Document API endpoints and data structures
- Include usage examples where helpful

### Content Documentation
- Maintain the README.md with current information
- Update deployment guides as needed
- Document new features and changes

## 🐛 Bug Reports

When reporting bugs, please include:
- **Description**: What happened?
- **Steps to reproduce**: How can we reproduce it?
- **Expected behavior**: What should happen?
- **Actual behavior**: What actually happened?
- **Environment**: Browser, device, OS version
- **Screenshots**: If applicable

## 💡 Feature Requests

When suggesting features:
- **Problem**: What problem does this solve?
- **Solution**: How should it work?
- **Alternatives**: What other approaches have you considered?
- **Additional context**: Any other relevant information

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Email**: For security issues or private matters

## 🏆 Recognition

Contributors will be:
- Listed in the project's contributors section
- Mentioned in release notes for significant contributions
- Invited to join the maintainer team for consistent contributors

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Prompts for Change! 🚀
