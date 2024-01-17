// Resimlerin dinamik olarak eklenmesi
var imageCount = 39; // Toplam resim sayısı
var imageSlider = document.getElementById('guide-image-slider');
var carouselInner = imageSlider.querySelector('.carousel-inner');

for (var i = 0; i < imageCount; i++) {
  var imageIndex = i.toString().padStart(3, '0'); // 0'dan başlayan numaralandırma
  var imageSrc = '../../assets/bricky/AkilliBuzdolabi/AkilliBuzdolabi_' + imageIndex + '.jpg'; // Resim dosya yolu
  var carouselItem = document.createElement('div');
  carouselItem.className = (i === 0) ? 'carousel-item active' : 'carousel-item';

  var image = document.createElement('img');
  image.className = 'd-block w-100';
  image.src = imageSrc;
  image.alt = 'Image ' + (i + 1);

  carouselItem.appendChild(image);
  carouselInner.appendChild(carouselItem);
}


var imageCount = 27; // Toplam resim sayısı
var imageSlider = document.getElementById('guide-image-slider2');
var carouselInner = imageSlider.querySelector('.carousel-inner');

for (var i = 0; i < imageCount; i++) {
  var imageIndex = i.toString().padStart(3, '0'); // 0'dan başlayan numaralandırma
  var imageSrc = '../../assets/bricky/AkilliBuzdolabi/AkilliBuzdolabiKod_' + imageIndex + '.png'; // Resim dosya yolu
  var carouselItem = document.createElement('div');
  carouselItem.className = (i === 0) ? 'carousel-item active' : 'carousel-item';

  var image = document.createElement('img');
  image.className = 'd-block w-100';
  image.src = imageSrc;
  image.alt = 'Image ' + (i + 1);

  carouselItem.appendChild(image);
  carouselInner.appendChild(carouselItem);
}

// Klavye oklarını kullanarak slayt değiştirme işlevi ekleyelim
document.addEventListener('keydown', function (event) {
  if (event.key === 'ArrowRight') {
    $('#guide-image-slider').carousel('next');
  } else if (event.key === 'ArrowLeft') {
    $('#guide-image-slider').carousel('prev');
  }
});


      // Header elementini seçin
      var header = document.querySelector('.main-header');

// Slayt açıldığında header'ı gizlemek için bir işlev
function hideHeader() {
header.style.display = 'none'; // Header'ı gizle
}

// Slayt kapatıldığında header'ı göstermek için bir işlev
function showHeader() {
header.style.display = 'block'; // Header'ı göster
}

// Slayt açma düğmesine tıklanırsa header'ı gizle
document.querySelector('[data-toggle="modal"]').addEventListener('click', hideHeader);

// Slayt kapatma düğmesine tıklanırsa header'ı göster
document.querySelector('[data-dismiss="modal"]').addEventListener('click', showHeader);


var lastScrollTop = 0; // Son kaydırma konumu

// Header elementini seçin
var header = document.querySelector('.main-header');

// Kaydırma olayını dinleyin
window.addEventListener('scroll', function() {
var scrollTop = window.pageYOffset || document.documentElement.scrollTop;

// Kullanıcı aşağı kaydırıyorsa ve header görünüyorsa, header'ı gizleyin
if (scrollTop > lastScrollTop && header.style.display !== 'none') {
header.style.display = 'none';
} 
// Kullanıcı yukarı kaydırıyorsa, header'ı gösterin
else if (scrollTop < lastScrollTop || scrollTop === 0) {
header.style.display = 'block';
}

lastScrollTop = scrollTop; // Son kaydırma konumunu güncelle
});