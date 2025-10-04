// Enhanced Telegram Mini App with Metadata Support
let tg = window.Telegram?.WebApp;

// Initialize the app
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Telegram WebApp (only if available)
    if (tg) {
        tg.ready();
        tg.expand();
        tg.enableClosingConfirmation();
    } else {
        console.log('Telegram WebApp not available - running in local mode');
    }
    
    // Load posts data and initialize
    loadPostsData();
    
    // Fallback: try to load data after a delay if initial load fails
    setTimeout(() => {
        if (!postsData) {
            console.log('Retrying to load posts data...');
            loadPostsData();
        }
    }, 2000);
});

// Global variables
let currentCategory = 'all';
let searchQuery = '';
let allPosts = [];
let postsData = null;
let sortByDate = false;

// Load posts data from JSON
async function loadPostsData() {
    try {
        console.log('Loading posts data...');
        const response = await fetch('posts_metadata.json?t=' + Date.now());
        console.log('Response status:', response.status);
        console.log('Response headers:', response.headers);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const text = await response.text();
        console.log('Response text length:', text.length);
        console.log('First 100 chars:', text.substring(0, 100));
        
        postsData = JSON.parse(text);
        console.log('Parsed posts data:', postsData);
        
        // Flatten all posts into a single array
        allPosts = postsData.posts;
        console.log('All posts loaded:', allPosts.length);
        
        // Initialize the application
        initializeApp();
    } catch (error) {
        console.error('Error loading posts data:', error);
        showError('Failed to load posts data: ' + error.message);
    }
}

// Initialize the application
function initializeApp() {
    if (!postsData) return;
    
    // Render initial posts
    renderPosts();
    
    // Setup event listeners
    setupEventListeners();
    
    // Initialize search
    initializeSearch();
}

// Setup event listeners
function setupEventListeners() {
    // Navigation tabs
    document.querySelectorAll('.nav-tab').forEach(tab => {
        tab.addEventListener('click', function() {
            const category = this.dataset.category;
            switchCategory(category);
        });
    });
    
    // Search functionality
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');
    const searchContainer = document.getElementById('searchContainer');
    const searchCloseBtn = document.getElementById('searchCloseBtn');
    
    searchBtn.addEventListener('click', function() {
        searchContainer.style.display = searchContainer.style.display === 'none' ? 'flex' : 'none';
        if (searchContainer.style.display === 'flex') {
            searchInput.focus();
        }
    });
    
    searchCloseBtn.addEventListener('click', function() {
        searchContainer.style.display = 'none';
        searchInput.value = '';
        searchQuery = '';
        filterPosts();
    });
    
    searchInput.addEventListener('input', function() {
        searchQuery = this.value.toLowerCase();
        filterPosts();
    });
    
    // Sort functionality
    const sortBtn = document.getElementById('sortBtn');
    sortBtn.addEventListener('click', function() {
        sortByDate = !sortByDate;
        this.classList.toggle('active', sortByDate);
        this.title = sortByDate ? 'Sort by default order' : 'Sort by date';
        this.textContent = sortByDate ? '📋' : '📅';
        filterPosts();
    });
    
    // Modal functionality
    const modal = document.getElementById('articleModal');
    const closeModal = document.getElementById('closeModal');
    const openInTelegram = document.getElementById('openInTelegram');
    const copyContent = document.getElementById('copyContent');
    
    closeModal.addEventListener('click', function() {
        modal.classList.remove('show');
    });
    
    // About modal functionality
    const aboutBtn = document.getElementById('aboutBtn');
    const aboutModal = document.getElementById('aboutModal');
    const closeAboutModal = document.getElementById('closeAboutModal');
    const closeAboutBtn = document.getElementById('closeAboutBtn');
    
    aboutBtn.addEventListener('click', function() {
        updateAboutInfo();
        aboutModal.classList.add('show');
    });
    
    closeAboutModal.addEventListener('click', function() {
        aboutModal.classList.remove('show');
    });
    
    closeAboutBtn.addEventListener('click', function() {
        aboutModal.classList.remove('show');
    });
    
    openInTelegram.addEventListener('click', function() {
        if (currentPost && currentPost.metadata.source.url) {
        if (tg) {
                tg.openLink(currentPost.metadata.source.url);
            } else {
                window.open(currentPost.metadata.source.url, '_blank');
            }
        }
    });
    
    copyContent.addEventListener('click', function() {
        const content = document.getElementById('modalContent').textContent;
        navigator.clipboard.writeText(content).then(() => {
            if (tg) {
                tg.showAlert('Content copied to clipboard!');
            } else {
                alert('Content copied to clipboard!');
            }
        });
    });
    
    // Close modal when clicking outside
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.classList.remove('show');
        }
    });
    
    // Close about modal when clicking outside
    aboutModal.addEventListener('click', function(e) {
        if (e.target === aboutModal) {
            aboutModal.classList.remove('show');
        }
    });
}

// Initialize search with focus
function initializeSearch() {
    setTimeout(() => {
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            searchInput.focus();
        }
    }, 100);
}

// Switch category
function switchCategory(category) {
    currentCategory = category;
    
    // Update active tab
    document.querySelectorAll('.nav-tab').forEach(tab => {
        tab.classList.remove('active');
    });
    document.querySelector(`[data-category="${category}"]`).classList.add('active');
    
    // Filter and render posts
    filterPosts();
}

// Filter posts based on category and search
function filterPosts() {
    let filteredPosts = allPosts;
    
    // Filter by category
    if (currentCategory !== 'all') {
        filteredPosts = filteredPosts.filter(post => post.category === currentCategory);
    }
    
    // Filter by search query
    if (searchQuery) {
        filteredPosts = filteredPosts.filter(post => 
            post.title.toLowerCase().includes(searchQuery) ||
            post.content.toLowerCase().includes(searchQuery) ||
            post.preview.toLowerCase().includes(searchQuery) ||
            post.metadata.tags.some(tag => tag.toLowerCase().includes(searchQuery))
        );
    }
    
    // Sort posts
    if (sortByDate) {
        filteredPosts = filteredPosts.sort((a, b) => {
            const dateA = new Date(a.metadata.timestamps.created);
            const dateB = new Date(b.metadata.timestamps.created);
            return dateB - dateA; // Newest first
        });
    }
    
    
    // Render posts
    renderPosts(filteredPosts);
}

// Render posts
function renderPosts(posts = null) {
    const postsGrid = document.getElementById('articlesGrid');
    const noResults = document.getElementById('noResults');
    
    if (!posts) {
        posts = currentCategory === 'all' ? allPosts : allPosts.filter(post => post.category === currentCategory);
    }
    
    if (posts.length === 0) {
        postsGrid.innerHTML = '';
        noResults.style.display = 'block';
        return;
    }
    
    noResults.style.display = 'none';
    
    postsGrid.innerHTML = posts.map(post => `
        <div class="article-card" onclick="openPost('${post.id}')">
            <div class="article-header">
                <div class="article-title-section">
                    <h3 class="article-title">${post.title}</h3>
                    <div class="article-meta">
                        <span class="category-badge" style="background: ${getCategoryColor(post.category)}">
                            ${getCategoryIcon(post.category)} ${getCategoryDisplayName(post.category)}
                        </span>
                        <span class="post-id">${post.id}</span>
                    </div>
                </div>
            </div>
            <div class="article-preview">${post.preview}</div>
            <div class="article-footer">
                <div class="article-stats">
                    <span class="read-time">⏱️ ${post.metadata.read_time}</span>
                    <span class="difficulty-badge difficulty-${post.metadata.difficulty}">
                        ${getDifficultyIcon(post.metadata.difficulty)} ${post.metadata.difficulty}
                    </span>
                    <span class="language-badge">${getLanguageFlag(post.metadata.language)}</span>
                </div>
                <div class="article-tags">
                    ${post.metadata.tags.slice(0, 3).map(tag => `<span class="tag">#${tag}</span>`).join('')}
                    ${post.metadata.tags.length > 3 ? `<span class="tag-more">+${post.metadata.tags.length - 3}</span>` : ''}
                </div>
            </div>
        </div>
    `).join('');
}

// Open post modal
let currentPost = null;

function openPost(postId) {
    currentPost = allPosts.find(post => post.id === postId);
    
    if (!currentPost) return;
    
    // Update modal content
    document.getElementById('modalTitle').textContent = currentPost.title;
    document.getElementById('modalCategory').textContent = getCategoryDisplayName(currentPost.category);
    document.getElementById('modalPostId').textContent = currentPost.id;
    document.getElementById('modalContent').textContent = currentPost.content;
    
    // Update modal metadata
    updateModalMetadata(currentPost);
    
    // Show modal
    document.getElementById('articleModal').classList.add('show');
    
    // Track view
    trackPostView(currentPost);
    
    // Send view event to Telegram
    if (tg) {
        tg.HapticFeedback.impactOccurred('medium');
    }
}

// Update modal metadata display
function updateModalMetadata(post) {
    const modalMeta = document.getElementById('modalMetadata');
    if (!modalMeta) return;
    
    modalMeta.innerHTML = `
        <div class="modal-meta-grid">
            <div class="meta-item">
                <span class="meta-label">Read Time:</span>
                <span class="meta-value">${post.metadata.read_time}</span>
            </div>
            <div class="meta-item">
                <span class="meta-label">Difficulty:</span>
                <span class="meta-value difficulty-${post.metadata.difficulty}">
                    ${getDifficultyIcon(post.metadata.difficulty)} ${post.metadata.difficulty}
                </span>
            </div>
            <div class="meta-item">
                <span class="meta-label">Language:</span>
                <span class="meta-value">${getLanguageFlag(post.metadata.language)} ${post.metadata.language.toUpperCase()}</span>
            </div>
            <div class="meta-item">
                <span class="meta-label">Word Count:</span>
                <span class="meta-value">${post.metadata.word_count}</span>
            </div>
        </div>
        <div class="modal-tags">
            <span class="meta-label">Tags:</span>
            <div class="tags-container">
                ${post.metadata.tags.map(tag => `<span class="tag">#${tag}</span>`).join('')}
            </div>
        </div>
        ${post.metadata.analysis.key_points.length > 0 ? `
            <div class="key-points">
                <span class="meta-label">Key Points:</span>
                <ul>
                    ${post.metadata.analysis.key_points.map(point => `<li>${point}</li>`).join('')}
                </ul>
            </div>
        ` : ''}
    `;
}

// Get category display name
function getCategoryDisplayName(category) {
    if (!postsData || !postsData.categories) return category;
    return postsData.categories[category]?.name || category;
}

// Get category icon
function getCategoryIcon(category) {
    if (!postsData || !postsData.categories) return '📄';
    return postsData.categories[category]?.icon || '📄';
}

// Get category color
function getCategoryColor(category) {
    if (!postsData || !postsData.categories) return 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
    return postsData.categories[category]?.color || '#667eea';
}

// Get difficulty icon
function getDifficultyIcon(difficulty) {
    const icons = {
        'beginner': '🟢',
        'intermediate': '🟡',
        'advanced': '🔴'
    };
    return icons[difficulty] || '⚪';
}

// Get language flag
function getLanguageFlag(language) {
    const flags = {
        'en': '🇺🇸',
        'ru': '🇷🇺',
        'es': '🇪🇸',
        'fr': '🇫🇷',
        'de': '🇩🇪'
    };
    return flags[language] || '🌐';
}


// Update About modal information
function updateAboutInfo() {
    if (!postsData) return;
    
    // Update stats
    document.getElementById('aboutTotalPosts').textContent = postsData.metadata.total_posts;
    document.getElementById('aboutCategories').textContent = Object.keys(postsData.categories).length;
    
    // Count unique languages
    const languages = new Set(allPosts.map(post => post.metadata.language));
    document.getElementById('aboutLanguages').textContent = languages.size;
    
    // Update version (current commit hash)
    document.getElementById('appVersion').textContent = 'c3ef838';
    
    // Update last updated date
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('lastUpdated').textContent = today;
}

// Track post view
function trackPostView(post) {
    // Increment view count
    if (post.metadata.engagement) {
        post.metadata.engagement.views = (post.metadata.engagement.views || 0) + 1;
    }
    
    // Store in localStorage for analytics
    const analytics = JSON.parse(localStorage.getItem('postAnalytics') || '{}');
    analytics[post.id] = analytics[post.id] || { views: 0, likes: 0, shares: 0 };
    analytics[post.id].views++;
    localStorage.setItem('postAnalytics', JSON.stringify(analytics));
}

// Show error message
function showError(message) {
    const articlesGrid = document.getElementById('articlesGrid');
    articlesGrid.innerHTML = `
        <div class="error-message">
            <div class="error-icon">⚠️</div>
            <h3>Error</h3>
            <p>${message}</p>
        </div>
    `;
}

// Handle Telegram WebApp events
if (tg) {
    tg.onEvent('mainButtonClicked', function() {
        // Handle main button click if needed
    });
    
    tg.onEvent('backButtonClicked', function() {
        const modal = document.getElementById('articleModal');
        if (modal.classList.contains('show')) {
            modal.classList.remove('show');
        } else {
            tg.close();
        }
    });
} else {
    // Fallback for non-Telegram environments
    console.log('Telegram WebApp events not available');
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Escape key to close modal
    if (e.key === 'Escape') {
        const modal = document.getElementById('articleModal');
        if (modal.classList.contains('show')) {
            modal.classList.remove('show');
        }
    }
    
    // Ctrl/Cmd + K for search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        document.getElementById('searchInput').focus();
    }
});

// Initialize search on page load
document.addEventListener('DOMContentLoaded', function() {
    // Focus search input on load
    setTimeout(() => {
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            searchInput.focus();
        }
    }, 100);
});
