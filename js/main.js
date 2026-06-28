document.addEventListener('DOMContentLoaded', function () {
    // --- Theme Switcher Logic ---
    const themeSwitcher = document.getElementById('theme-switcher');
    const html = document.documentElement;

    const applyTheme = (theme) => {
        html.setAttribute('data-theme', theme);
        if (themeSwitcher) {
            themeSwitcher.checked = theme === 'dark';
        }
    };

    const getInitialTheme = () => {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            return savedTheme;
        }
        const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        return prefersDark ? 'dark' : 'light';
    };

    const initialTheme = getInitialTheme();
    applyTheme(initialTheme);

    if (themeSwitcher) {
        themeSwitcher.addEventListener('change', function () {
            const newTheme = this.checked ? 'dark' : 'light';
            applyTheme(newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        if (!localStorage.getItem('theme')) {
            const newTheme = e.matches ? 'dark' : 'light';
            applyTheme(newTheme);
        }
    });

    // --- Navbar Scroll Effect ---
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // --- Scroll-triggered Animations ---
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    // --- Documentation Sidebar Toggle ---
    const sidebarToggle = document.getElementById('doc-sidebar-toggle');
    const sidebar = document.querySelector('.docs-sidebar');
    
    if (sidebarToggle && sidebar) {
        // Create backdrop
        const backdropEl = document.createElement('div');
        backdropEl.className = 'docs-backdrop';
        backdropEl.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            backdrop-filter: blur(4px);
            z-index: 1055;
            display: none;
            opacity: 0;
            transition: opacity 0.3s ease;
        `;
        document.body.appendChild(backdropEl);

        const toggleSidebar = () => {
            const isActive = sidebar.classList.toggle('active');
            if (isActive) {
                backdropEl.style.display = 'block';
                setTimeout(() => backdropEl.style.opacity = '1', 10);
                document.body.style.overflow = 'hidden';
            } else {
                backdropEl.style.opacity = '0';
                setTimeout(() => {
                    backdropEl.style.display = 'none';
                }, 300);
                document.body.style.overflow = '';
            }
        };

        sidebarToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleSidebar();
        });
        
        backdropEl.addEventListener('click', toggleSidebar);

        // Close sidebar on link click (mobile)
        const docLinks = sidebar.querySelectorAll('.docs-nav-link, .docs-nav-menu a');
        docLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 992) {
                    toggleSidebar();
                }
            });
        });
    }

    animatedElements.forEach(element => {
        observer.observe(element);
    });

    // --- Dynamic Reading Progress Bar ---
    const docsContent = document.querySelector('.docs-content');
    if (docsContent) {
        // Create progress container & bar
        const progressContainer = document.createElement('div');
        progressContainer.className = 'scroll-progress-container';
        const progressBar = document.createElement('div');
        progressBar.className = 'scroll-progress-bar';
        progressContainer.appendChild(progressBar);
        document.body.appendChild(progressContainer);

        // Update progress on scroll
        const updateProgressBar = () => {
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
            progressBar.style.width = scrolled + '%';
        };
        window.addEventListener('scroll', updateProgressBar);
        updateProgressBar(); // Run once initially
    }

    // --- Dynamic Read Time Badges ---
    const docSections = document.querySelectorAll('.docs-section');
    docSections.forEach(section => {
        const text = section.innerText || section.textContent || '';
        const wordCount = text.trim().split(/\s+/).filter(w => w.length > 0).length;
        const readTime = Math.max(1, Math.ceil(wordCount / 225)); // ~225 WPM average reading speed
        
        // Find the first heading of the section
        const heading = section.querySelector('h1, h2');
        if (heading && !heading.querySelector('.read-time-badge')) {
            const badge = document.createElement('span');
            badge.className = 'read-time-badge';
            badge.innerHTML = `<i class="far fa-clock"></i> ${readTime} min read`;
            heading.appendChild(badge);
        }
    });

    // --- Code Copy Buttons ---
    const codeBlocks = document.querySelectorAll('.docs-content pre');
    codeBlocks.forEach(pre => {
        // Avoid double wrapping if already processed
        if (pre.parentNode.classList.contains('code-block-wrapper')) return;

        // Wrap pre block in helper container
        const wrapper = document.createElement('div');
        wrapper.className = 'code-block-wrapper';
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);

        // Create copy button
        const copyBtn = document.createElement('button');
        copyBtn.className = 'copy-code-btn';
        copyBtn.type = 'button';
        copyBtn.innerHTML = '<i class="far fa-copy"></i> Copy';
        wrapper.appendChild(copyBtn);

        // Copy click handler
        copyBtn.addEventListener('click', () => {
            const codeEl = pre.querySelector('code');
            const textToCopy = codeEl ? codeEl.innerText : pre.innerText;
            
            navigator.clipboard.writeText(textToCopy).then(() => {
                copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied';
                copyBtn.classList.add('copied');
                setTimeout(() => {
                    copyBtn.innerHTML = '<i class="far fa-copy"></i> Copy';
                    copyBtn.classList.remove('copied');
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy text: ', err);
            });
        });
    });
});