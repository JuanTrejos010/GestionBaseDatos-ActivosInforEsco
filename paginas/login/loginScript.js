
const form = document.getElementById('usuario');
const alertBox = document.getElementById('alerta');
const toggleBtn = document.getElementById('togglePwd');
const passwordInput = document.getElementById('password');
const demoBtn = document.getElementById('demo');


function showAlert(type, text){
alertBox.innerHTML = `<div class="${type==='error'?'error':'success'}">${text}</div>`;
}


// Toggle password visibility
toggleBtn.addEventListener('click', ()=>{
const shown = passwordInput.type === 'text';
passwordInput.type = shown ? 'password' : 'text';
toggleBtn.textContent = shown ? 'Mostrar' : 'Ocultar';
toggleBtn.setAttribute('aria-label', shown ? 'Mostrar contraseña' : 'Ocultar contraseña');
});


// Demo autocompleta
demoBtn.addEventListener('click', ()=>{
document.getElementById('email').value = 'estudiante@liceo.com';
passwordInput.value = 'Estu1234!';
showAlert('success', 'Credenciales de demo cargadas. Presiona "Iniciar sesión".');
});


// Validación simple de email
function validarEmail(email){
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}


form.addEventListener('submit', (e) => {
  e.preventDefault();
  alertBox.innerHTML = '';

  const email = form.email.value.trim();
  const pwd = form.password.value;

  // Validaciones del lado del cliente
  if (!email || !pwd) {
    showAlert('error','Por favor completa todos los campos.');
    return;
  }

  if (!validarEmail(email)) {
    showAlert('error','Introduce un correo electrónico válido.');
    return;
  }

  // Aquí podrías enviar al backend con fetch()
  fetch('/login', {
    method: 'POST',
    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    body: new URLSearchParams({email, password: pwd})
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      showAlert('success', `¡Bienvenido, ${email.split('@')[0]}!`);
      location.href = '/interfaz';
    } else {
      showAlert('error', 'Credenciales incorrectas.');
    }
  })
  .catch(err => showAlert('error', 'Error en el servidor.'));
});



    //location.href="/interfaz"

