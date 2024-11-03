// Agregar evento de clic al botón de búsqueda
document.querySelector('button[type="submit"]').addEventListener('click', function(event) {
    event.preventDefault();
    // Mostrar la tabla de resultados
    document.getElementById('tabla-resultados').style.display = 'block';
  });