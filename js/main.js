document.addEventListener('DOMContentLoaded', function() {
    // Typing effect for hero section
    const typingElement = document.querySelector('.hero-section .lead');
    if (typingElement) {
        const text = typingElement.innerText;
        typingElement.innerText = '';
        let i = 0;
        function typeWriter() {
            if (i < text.length) {
                typingElement.innerHTML += text.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            }
        }
        typeWriter();
    }

    // Fade-in animation on scroll
    const fadeElems = document.querySelectorAll('.card, .feature-box, .testimonial-card');
    const fadeInObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeIn 1s forwards';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    fadeElems.forEach(elem => {
        elem.style.opacity = '0';
        fadeInObserver.observe(elem);
    });

    // Asset card description toggle
    const assetCards = document.querySelectorAll('.asset-card');
    assetCards.forEach(card => {
        const button = card.querySelector('button');
        const description = card.querySelector('.asset-description');
        button.addEventListener('click', (e) => {
            e.stopPropagation();
            if (description.style.display === 'block') {
                description.style.display = 'none';
                button.innerHTML = '<i class="fas fa-info-circle me-2"></i>Show Description';
            } else {
                description.style.display = 'block';
                button.innerHTML = '<i class="fas fa-info-circle me-2"></i>Hide Description';
            }
        });
    });
});

// Add fadeIn animation to CSS
const style = document.createElement('style');
style.innerHTML = `
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
`;
document.head.appendChild(style);