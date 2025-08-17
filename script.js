document.addEventListener('DOMContentLoaded', () => {
    // Initialize Animate on Scroll (AOS)
    AOS.init({
        duration: 1000,
        easing: 'ease-in-out',
        once: true,
        offset: 50,
    });

    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', e => {
            e.preventDefault();
            const targetId = e.currentTarget.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 60, // Adjust for fixed header
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add shadow to header on scroll
    const header = document.querySelector('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.5)';
        } else {
            header.style.boxShadow = 'none';
        }
    });

    // Handle contact form submission
    const contactForm = document.querySelector('.contact-form form');
    contactForm.addEventListener('submit', e => {
        e.preventDefault();
        // In a real application, you would send this data to a server.
        // For this demo, we'll just show an alert and clear the form.
        alert('Thank you for your message! I will get back to you soon.');
        contactForm.reset();
    });
});
