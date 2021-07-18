// Constructor para Seguro
function Presupuesto(metros, colores) {
    this.metros = metros;
    this.colores = colores;
}

// Todo lo que se muestra
function Interfaz() {}

// Mensaje que se imprime en el HTML
Interfaz.prototype.mostrarMensaje = function(mensaje) {
    const div = document.createElement('div');


    div.classList.add('mensaje', 'correcto');
    div.classList.add('mt-10');
    div.innerHTML = `${mensaje}`;
    formulario.insertBefore(div, document.querySelector('#resultado')); // Nuevo Nodo y referencia... // Si la referencia no existe se añadira al final

    setTimeout(() => {
        document.querySelector('.mensaje').remove();
    }, 3000);
}

// Imprime el resultado de la cotización
Interfaz.prototype.mostrarResultado = function(presupuesto) {
    const resultado = document.querySelector('#resultado');
    const metros = document.getElementById('metros').value;
    let colores = document.getElementById('colores').value;

    if (colores === '1') {
        let total1 = (presupuesto.metros * 130) + 2500
        const div = document.createElement('div');
        div.classList.add('mt-10')
            // Insertar la informacion
        div.innerHTML = `
          <p class='header'>Tu Resumen: </p>
          <p class="font-bold">Metros: <span class="font-normal"> ${presupuesto.metros} </span> </p>
          <p class="font-bold">Colores: <span class="font-normal"> ${presupuesto.colores} </span> </p>
          <p class="font-bold letra-total-grande"> Total: <span class="font-normal"> $ ${total1} </span> </p> `;
        const spinner = document.querySelector('#cargando');
        spinner.style.display = 'block';
        setTimeout(() => {
            spinner.style.display = 'none';
            resultado.appendChild(div);
        }, 3000);

    } else if (colores === '2') {
        let total2 = (metros * 200) + 5000
        const div = document.createElement('div');
        div.classList.add('mt-10')
            // Insertar la informacion
        div.innerHTML = `
          <p class='header'>Tu Resumen: </p>
          <p class="font-bold">Metros: <span class="font-normal"> ${presupuesto.metros} </span> </p>
          <p class="font-bold">Colores: <span class="font-normal"> ${presupuesto.colores} </span> </p>
          <p class="font-bold letra-total-grande;"> Total: <span class="font-normal"> $ ${total2} </span> </p> `;
        const spinner = document.querySelector('#cargando');
        spinner.style.display = 'block';
        setTimeout(() => {
            spinner.style.display = 'none';
            resultado.appendChild(div);
        }, 3000);

    } else if (colores === '3') {
        let total3 = (metros * 250) + 7500
        const div = document.createElement('div');
        div.classList.add('mt-10')
            // Insertar la informacion
        div.innerHTML = `
          <p class='header'>Tu Resumen: </p>
          <p class="font-bold">Metros: <span class="font-normal"> ${presupuesto.metros} </span> </p>
          <p class="font-bold">Colores: <span class="font-normal"> ${presupuesto.colores} </span> </p>
          <p class="font-bold letra-total-grande;"> Total: <span class="font-normal "> $ ${total3} </span> </p> `;
        const spinner = document.querySelector('#cargando');
        spinner.style.display = 'block';
        setTimeout(() => {
            spinner.style.display = 'none';
            resultado.appendChild(div);
        }, 3000);

    }


}

// Crear instancia de Interfaz
const interfaz = new Interfaz();

const formulario = document.querySelector('#cotizar-estampa');

formulario.addEventListener('submit', e => {
    e.preventDefault();

    // leer la marca seleccionada del select
    const metros = document.querySelector('#metros').value;

    // leer el año seleccionado del <select>
    const colores = document.querySelector('#colores').value




    // Revisamos que los campos no esten vacios
    if (metros === '' || colores === '') {
        // Interfaz imprimiendo un error
        interfaz.mostrarMensaje('Faltan datos, revisar el formulario y prueba de nuevo', 'error');
    } else {
        // Limpiar resultados anteriores
        const resultados = document.querySelector('#resultado div');
        if (resultados != null) {
            resultados.remove();
        }

        // Instanciar seguro y mostrar interfaz
        const presupuesto = new Presupuesto(metros, colores);

        // Mostrar el resultado
        interfaz.mostrarResultado(presupuesto);
        interfaz.mostrarMensaje('Cotizando...', 'exito');
    }
})