// Calendly Integration
function initCalendly() {
    // Initialize Calendly buttons
    document.querySelectorAll('[data-calendly]').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            Calendly.initPopupWidget({
                url: 'https://calendly.com/valentin-chevaux/30min',
                text: 'Schedule time with us',
                color: '#153739',
                textColor: '#ffffff',
                branding: true
            });
        });
    });
}

// Initialize Calendly when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    if (typeof Calendly !== 'undefined') {
        initCalendly();
    } else {
        // If Calendly hasn't loaded yet, wait for it
        const calendlyScript = document.querySelector('script[src*="calendly"]');
        if (calendlyScript) {
            calendlyScript.addEventListener('load', initCalendly);
        }
    }
});

// Initialize AOS
AOS.init({
    duration: 800,
    easing: 'ease-in-out',
    once: true
});

// Sticky Navigation
window.addEventListener('scroll', function() {
    const nav = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        nav.classList.add('navbar-scrolled');
    } else {
        nav.classList.remove('navbar-scrolled');
    }
});

// Form Validation
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
});

// Micro-interactions
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('mouseover', function() {
        this.style.transform = 'scale(1.05)';
    });
    
    button.addEventListener('mouseout', function() {
        this.style.transform = 'scale(1)';
    });
});

// FAQ Accordion
document.querySelectorAll('.accordion-button').forEach(button => {
    button.addEventListener('click', function() {
        const icon = this.querySelector('.accordion-icon');
        icon.classList.toggle('rotated');
    });
});

// E-book Modal
const ebookModal = document.getElementById('ebookModal');
if (ebookModal) {
    const modalInstance = new bootstrap.Modal(ebookModal);
    
    document.querySelectorAll('.ebook-cta').forEach(button => {
        button.addEventListener('click', function() {
            modalInstance.show();
        });
    });
}

// Image Lazy Loading
document.addEventListener('DOMContentLoaded', function() {
    const lazyImages = document.querySelectorAll('img[loading="lazy"]');
    
    if ('loading' in HTMLImageElement.prototype) {
        lazyImages.forEach(img => {
            img.src = img.dataset.src;
        });
    } else {
        // Fallback for browsers that don't support lazy loading
        const lazyLoadScript = document.createElement('script');
        lazyLoadScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/lozad.js/1.16.0/lozad.min.js';
        document.body.appendChild(lazyLoadScript);
        
        lazyLoadScript.onload = function() {
            const observer = lozad('.lazy');
            observer.observe();
        };
    }
});

// Form Submission Handler
const handleFormSubmit = async (form, endpoint) => {
    const formData = new FormData(form);
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            body: formData
        });
        
        if (response.ok) {
            showAlert('Success!', 'Your submission has been received.', 'success');
            form.reset();
        } else {
            throw new Error('Submission failed');
        }
    } catch (error) {
        showAlert('Error', 'Something went wrong. Please try again.', 'error');
    }
};

// Alert Helper
const showAlert = (title, message, type) => {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        <strong>${title}</strong> ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.querySelector('.alert-container').appendChild(alertDiv);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
};
