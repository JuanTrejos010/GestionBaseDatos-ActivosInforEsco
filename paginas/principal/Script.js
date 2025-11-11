//Elementos
const form = document.getElementById('recordForm');
const idField = document.getElementById('id');
const marcaField = document.getElementById('marca');
const modeloField = document.getElementById('modelo');
const estadoField = document.getElementById('estado');
const fechaField = document.getElementById('fecha_compra');
const descripcionField = document.getElementById('Descripción');
const salaField = document.getElementById('id_sala');
const tableBody = document.querySelector('#recordsTable tbody');
const searchInput = document.getElementById('search');
const exportBtn = document.getElementById('exportBtn');
const importFile = document.getElementById('importFile');
const clearBtn = document.getElementById('clearBtn');
const resetBtn = document.getElementById('resetBtn');
const formTitle = document.getElementById('form-title');

// Cargar tabla al inicio
window.addEventListener('DOMContentLoaded', renderTable);

/* 
* CRUD
*/

//Llamando los datos de equipos
async function renderTable(filter = '') {
  const response = await fetch('/equipos/buscar');
  const data = await response.json(); // viene desde PostgreSQL
  const list = data.filter(r => {
    if (!filter) return true;
    const q = filter.toLowerCase();
    return r.marca.toLowerCase().includes(q) || r.modelo.toLowerCase().includes(q);
  });

  const tableBody = document.querySelector('#recordsTable tbody');
  tableBody.innerHTML = '';

  list.forEach(r => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${r.id_equipo}</td>
      <td>${r.nombre}</td>
      <td>${r.marca}</td>
      <td>${r.modelo}</td>
      <td>${r.id_sala}</td>
      <td>
        <button onclick="editRecord(${r.id_equipo})">Editar</button>
        <button onclick="deleteRecord(${r.id_equipo})">Borrar</button>
      </td>`;
    tableBody.appendChild(tr);
  });
}

async function addRecord() {
  const marca = document.getElementById('marca').value;
  const modelo = document.getElementById('modelo').value;
  const fecha_compra = document.getElementById('fecha_compra').value;
  const id_sala = document.getElementById('id_sala').value;

  const response = await fetch('/equipos/nuevo', {
    method: 'POST',
    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    body: new URLSearchParams({ marca, modelo, fecha_compra, id_sala })
  });

  const data = await response.json();
  alert(data.mensaje || 'Equipo registrado');
  renderTable();
}

async function deleteRecord(id) {
  if (!confirm('¿Eliminar este registro?')) return;
  const response = await fetch('/equipos/eliminar', {
    method: 'POST',
    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    body: new URLSearchParams({ id_equipo: id })
  });
  const data = await response.json();
  alert(data.mensaje);
  renderTable();
}

// Helpers
function uid(){ return 'id-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2,8); }
function escapeHtml(text){ return String(text).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }


// Editar (llenar formulario)
/*
window.editRecord = function(id){
  const r = db.find(x=>x.id===id); if(!r) return;
  idField.value = r.id; nameField.value = r.name; emailField.value = r.email; roleField.value = r.role || '';
  formTitle.textContent = 'Editar registro';
  saveBtnText('Actualizar');
}*/


function saveBtnText(text){ document.getElementById('saveBtn').textContent = text; }


// Form submit
form.addEventListener('submit', (e)=>{
  e.preventDefault();

  const name = nameField.value.trim();
  const email = emailField.value.trim();
  const role = roleField.value.trim();

  if(!name || !email)
    { 
        alert('Nombre y correo son obligatorios');
        return;
    }

  const existingId = idField.value;
  if(existingId){ updateRecord(existingId, { name, email, role }); }
  else{ addRecord({ id: uid(), name, email, role }); }

  form.reset();
  idField.value = '';
  formTitle.textContent = 'Agregar registro';
  saveBtnText('Guardar');
});


form.reset(); 
formTitle.textContent = 'Agregar registro';
saveBtnText('Guardar');
renderTable();