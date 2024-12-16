document.addEventListener('DOMContentLoaded', function() {
    const parallaxSections = document.querySelectorAll('.parallax-section');
    const parallaxItems = document.querySelectorAll('.parallax-item');
    const scrollAnimateElements = document.querySelectorAll('.scroll-animate');
    
    // Parallax scrolling effect
    function handleParallax() {
        parallaxSections.forEach(section => {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.3;
            const bg = section.querySelector('.parallax-bg');
            if (bg) {
                bg.style.transform = `translateY(${rate}px)`;
            }
        });

        // Handle parallax items
        parallaxItems.forEach(item => {
            const rect = item.getBoundingClientRect();
            const scrolled = window.pageYOffset;
            const rate = (rect.top + scrolled) * 0.1;
            item.style.transform = `translateY(${rate}px)`;
        });

        // Handle scroll animations
        scrollAnimateElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;
            
            if (elementTop < window.innerHeight - elementVisible) {
                element.classList.add('visible');
            }
        });
    }

    // Throttle function to limit the rate at which handleParallax runs
    function throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        }
    }

    // Add scroll event listener with throttling
    window.addEventListener('scroll', throttle(handleParallax, 10));
    
    // Initial call to set initial state
    handleParallax();
});
