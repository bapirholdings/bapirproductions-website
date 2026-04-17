document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contactForm');
    const formStatus = document.getElementById('formStatus');

    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault(); // Stop the page from refreshing

            // Create a FormData object from the form fields
            const formData = new FormData(contactForm);

            try {
                // Send the data to Formspree via AJAX/Fetch
                const response = await fetch(contactForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Accept': 'application/json'
                    }
                });

                if (response.ok) {
                    // Success: Show the message and reset form
                    const name = document.getElementById('name').value;
                    const email = document.getElementById('email').value;
                    
                    formStatus.innerHTML = `<p style="color: var(--primary-green); margin-top: 1rem; font-weight: bold;">
                        Thank you, ${name}! Your message has been sent successfully. 
                        We will get back to you at ${email} shortly.
                    </p>`;
                    
                    contactForm.reset();
                } else {
                    // Error: Handle server-side issues
                    formStatus.innerHTML = `<p style="color: red; margin-top: 1rem;">Oops! There was a problem submitting your form.</p>`;
                }
            } catch (error) {
                // Error: Handle network issues
                formStatus.innerHTML = `<p style="color: red; margin-top: 1rem;">Error: Could not connect to the server. Please check your internet.</p>`;
            }
        });
    }
});