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
});