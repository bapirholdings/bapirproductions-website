document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contactForm');
    const formStatus = document.getElementById('formStatus');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            // Extract values
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            // In a real scenario, you would send this to a backend server.
            // For this basic code, we'll simulate a success message.
            
            formStatus.innerHTML = `<p style="color: var(--primary-green); margin-top: 1rem; font-weight: bold;">Thank you, ${name}! Your message has been sent successfully. We will get back to you at ${email} shortly.</p>`;
            
            // Clear form
            contactForm.reset();
        });
    }
});

// Formspree Integration
// This connects the library to your specific form ID
window.formspree = window.formspree || function () { 
    (formspree.q = formspree.q || []).push(arguments); 
};

formspree('initForm', { 
    formElement: '#contactForm', 
    formId: 'mykleojk',
    onSuccess: function(data) {
        // The library automatically handles showing the [data-fs-success] div,
        // but you can add custom logic here if needed.
        console.log('Form submitted successfully');
    }
});
