document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('login-form');
    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const email = document.getElementById('email');
        const password = document.getElementById('password');

        if (!email.checkValidity()) {
            email.reportValidity();
            return;
        }

        if (!password.checkValidity()) {
            password.reportValidity();
            return;
        }

        // Aquí puedes procesar el formulario, por ejemplo, enviar los datos al servidor.
        console.log('Formulario válido:', { email: email.value, password: password.value });
    });

    // Personaliza los mensajes de validación si es necesario.
    email.setCustomValidity('Por favor, ingrese un correo electrónico válido.');
    password.setCustomValidity('Por favor, ingrese una contraseña válida.');
});