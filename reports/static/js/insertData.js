const fileInput = document.getElementById('file-input')
const btnSubmit = document.getElementById('btn-submit')
const helpVisual = document.getElementById('help-visual')

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {

        helpVisual.innerHTML = `Archivo: ${fileInput.files[0].name} `
        helpVisual.classList.remove('hidden')
        btnSubmit.classList.remove('disable')
    } else {
        helpVisual.classList.remove('hidden')
        btnSubmit.classList.add('disable')
    }
})

//practicamente lo mismo porque se consulta el endpoint sin enviar el formulario,
//ya que se envia desde js los datos al dar click y validar una cosas
