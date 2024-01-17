$(document).ready(function () {
    
    var portfolioSlider = $('.portfolio-slider');
    var portfolioOptions = {
        loop: false,
        center: false,
        margin: 100,
        autoplay: true,
        items: 2,
        dots: false,
        nav: false,
        responsiveClass: true,
        responsive: {
            0: {
                items: 2,
                nav: false
            },
            600: {
                items: 2,
                nav: false
            },
            991: {
                items: 2,
                nav: false
            },
            1024: {
                items: 2,
                nav: false
            }
        }
    };

    portfolioSlider.owlCarousel(portfolioOptions);

    portfolioSlider.on('changed.owl.carousel', function (event) {
        if (event.item.index + event.page.size === event.item.count) {
            setTimeout(function () {
                portfolioSlider.trigger('to.owl.carousel', [0, 300]); // Son slayta geldiğinde başa dön
            }, 5000); 
        }
    });

    $('.testimonial').owlCarousel({
        loop:true,
		center:true,
		autoplay:true,
        items:1,
        dots: false,
        margin:10,
        nav:false,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
                nav:false
            },
            600:{
                items:1,
                nav:false
            },
            991:{
                items:1,
                nav:false
            },
            1024:{
                items:1,
                nav:false
            }
        }
    });


    $('.trusted-logos').owlCarousel({
        loop:false,
        items:4,
        dots: false,
        autoplay:false,
        autoplayHoverPause:true,
        nav:false,
        responsiveClass:true,
        responsive:{
            0:{
                items:2,
                nav:false
            },
            600:{
                items:3,
                nav:false
            },
            991:{
                items:3,
                nav:false
            },
            1024:{
                items:4,
                nav:false
            }
        }
    });



    // ... Diğer kodlar burada ...

    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('header').addClass("sticky");
        } else {
            $('header').removeClass("sticky");
        }
    });

    // copyrights Year Auto-update
    function newDate() {
        return new Date().getFullYear();
    }
    document.onload = document.getElementById("autodate").innerHTML = +newDate();
});
