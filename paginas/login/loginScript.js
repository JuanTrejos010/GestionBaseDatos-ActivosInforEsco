
const form = document.getElementById('usuario');
const alertBox = document.getElementById('alerta');
const toggleBtn = document.getElementById('togglePwd');
const passwordInput = document.getElementById('password');
const demoBtn = document.getElementById('demo');


// Simulación simple de usuarios — en producción esto no debe estar en el front-end.
const users = [
{email:'estudiante@liceo.com', password:'Estu1234!'},
{email:'docente@liceo.com', password:'Docente2025'}
];


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


form.addEventListener('submit'), (e)=>{
e.preventDefault();
alertBox.innerHTML = '';
}

const email = form.email.value.trim();
const pwd = form.password.value;


// Validaciones del lado del cliente
if(!email || !pwd){
showAlert('error','Por favor completa todos los campos.');
return;
}


if(!validarEmail(email)){
showAlert('error','Introduce un correo electrónico válido.');
return;
}


// Simular proceso de autenticación
const found = users.find(u => u.email.toLowerCase() === email.toLowerCase() && u.password === pwd);
if(found){
// En una app real redirigirías o establecerías token recibido del servidor
showAlert('success', `¡Bienvenido, ${email.split('@')[0]}! Has iniciado sesión correctamente.`);
// ejemplo: localStorage si marcó "recuérdame"
if(form.remember.checked){
localStorage.setItem('rememberedUser', email);
}};