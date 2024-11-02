function showPreview() {
    const fileInput = document.getElementById('fileInput');
    const previewImage = document.getElementById('previewImage');
    const file = fileInput.files[0];

    if (file && !file.type.startsWith('image/')) {
        alert('Будь ласка, виберіть зображення.');
        fileInput.value = '';
        previewImage.style.display = 'none';
        return;
    }

    const reader = new FileReader();

    reader.onload = function(e) {
        previewImage.src = e.target.result;
        previewImage.style.display = 'block';
    };

    if (file) {
        reader.readAsDataURL(file);
    }
}

async function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Будь ласка, завантажте зображення.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload/', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Не вдалося завантажити зображення.');
        }

        const blob = await response.blob();
        const outputImage = document.getElementById('outputImage');
        outputImage.src = URL.createObjectURL(blob);
        outputImage.style.display = 'block';
    } catch (error) {
        alert(error.message);
    }
}
