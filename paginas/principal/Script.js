// DB simple usando localStorage
const STORAGE_KEY = 'mi_db_local_v1';
let db = [];


// Elementos
const form = document.getElementById('recordForm');
const idField = document.getElementById('id');
const nameField = document.getElementById('name');
const emailField = document.getElementById('email');
const roleField = document.getElementById('role');
const tableBody = document.querySelector('#recordsTable tbody');
const searchInput = document.getElementById('search');
const exportBtn = document.getElementById('exportBtn');
const importFile = document.getElementById('importFile');
const clearBtn = document.getElementById('clearBtn');
const resetBtn = document.getElementById('resetBtn');
const formTitle = document.getElementById('form-title');


// Cargar DB desde localStorage
function loadDB(){
    const raw = localStorage.getItem(STORAGE_KEY);
    db = raw ? JSON.parse(raw) : [];
}


function saveDB(){
    localStorage.setItem(STORAGE_KEY, JSON.stringify(db));
}


function renderTable(filter = ''){
    tableBody.innerHTML = '';
    const list = db.filter(r => {
    if(!filter) return true;
    const q = filter.toLowerCase();
    return r.name.toLowerCase().includes(q) || r.email.toLowerCase().includes(q);
    });
    list.forEach(r => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
    <td>${r.id}</td>
    <td>${escapeHtml(r.name)}</td>
    <td>${escapeHtml(r.email)}</td>
    <td>${escapeHtml(r.role || '')}</td>
    <td class="actions">
    <button class="small-btn" onclick="editRecord('${r.id}')">Editar</button>
    <button class="small-btn" onclick="deleteRecord('${r.id}')">Borrar</button>
    </td>`;
    tableBody.appendChild(tr);
    });
}


// Helpers
function uid(){ return 'id-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2,8); }
function escapeHtml(text){ return String(text).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }


// CRUD
function addRecord(obj){ db.push(obj); saveDB(); renderTable(searchInput.value); }
function updateRecord(id, data){ const i = db.findIndex(x=>x.id===id); if(i>-1){ db[i] = {...db[i], ...data}; saveDB(); renderTable(searchInput.value);} }
function deleteRecord(id){ if(confirm('Eliminar registro?')){ db = db.filter(x=>x.id!==id); saveDB(); renderTable(searchInput.value);} }


// Editar (llenar formulario)
window.editRecord = function(id){
const r = db.find(x=>x.id===id); if(!r) return;
idField.value = r.id; nameField.value = r.name; emailField.value = r.email; roleField.value = r.role || '';
formTitle.textContent = 'Editar registro';
saveBtnText('Actualizar');
}


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


form.reset(); idField.value = ''; formTitle.textContent = 'Agregar registro'; saveBtnText('Guardar');
loadDB(); renderTable();