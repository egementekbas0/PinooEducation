let currentIndex = 0;
const images = [
    {% for image in image_data.0.images %}
        "{% static '' %}{{ image }}",
    {% endfor %}
];

let scrollPosition = 0;

function openLightbox(event) {
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.getElementById('lightbox-image');
    const body = document.body;

    scrollPosition = window.pageYOffset;

    body.style.overflow = 'hidden';
    body.style.position = 'fixed';
    body.style.width = '100%';

    lightboxImage.src = images[currentIndex];
    lightbox.style.display = 'flex';

    document.addEventListener('keydown', handleKeyPress);

    event.preventDefault();
}

function closeLightbox() {
    const lightbox = document.getElementById('lightbox');
    const body = document.body;

    lightbox.style.display = 'none';

    body.style.overflow = 'visible';
    body.style.position = 'static';
    body.style.width = 'auto';

    window.scrollTo(0, scrollPosition);

    document.removeEventListener('keydown', handleKeyPress);
}

function handleKeyPress(e) {
    if (e.key === 'Escape') {
        closeLightbox();
    } else if (e.key === 'ArrowRight') {
        showNextImage();
    } else if (e.key === 'ArrowLeft') {
        showPrevImage();
    }
}

function showNextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    updateLightboxImage();
}

function showPrevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateLightboxImage();
}

function updateLightboxImage() {
    const lightboxImage = document.getElementById('lightbox-image');
    lightboxImage.src = images[currentIndex];
}