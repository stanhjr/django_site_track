// FOR BANNER SLIDER
$('.banner-slider').slick({
    dots: true,
    infinite: true,
    autoplay: true,
    arrows: false,
    fade: true,
    speed: 1000,
    prevArrow: '<i class="material-icons dandik">chevron_right</i>',
    nextArrow: '<i class="material-icons bamdik">chevron_left</i>',
    slidesToShow: 1,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                dots: false,
            }
        },
        {
            breakpoint: 576,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
                dots: false,
            }
        }
    ]
});


// FOR FEATURE SLIDER
$('.product-feature-slider').slick({
    dots: false,
    infinite: true,
    autoplay: true,
    arrows: true,
    fade: false,
    speed: 1000,
    prevArrow: '<i class="material-icons dandik">chevron_right</i>',
    nextArrow: '<i class="material-icons bamdik">chevron_left</i>',
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 576,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
            }
        }
    ]
});


// FOR INVENTORY FEATURE SLIDER
$('.inventory-feature-slider').slick({
    dots: false,
    infinite: true,
    autoplay: true,
    arrows: true,
    fade: false,
    speed: 1000,
    prevArrow: '<i class="material-icons dandik">chevron_right</i>',
    nextArrow: '<i class="material-icons bamdik">chevron_left</i>',
    slidesToShow: 2,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 576,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
            }
        }
    ]
});


// FOR REIEW SLIDER
$('.review-slider').slick({
    dots: false,
    infinite: true,
    autoplay: false,
    arrows: true,
    fade: false,
    speed: 1000,
    prevArrow: '<i class="material-icons dandik">chevron_right</i>',
    nextArrow: '<i class="material-icons bamdik">chevron_left</i>',
    slidesToShow: 1,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
            }
        },
        {
            breakpoint: 576,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
            }
        }
    ]
});


// FOR BLOG SLIDER
$('.blog-slider').slick({
    dots: false,
    infinite: true,
    autoplay: false,
    arrows: true,
    fade: false,
    speed: 1000,
    prevArrow: '<i class="material-icons dandik">chevron_right</i>',
    nextArrow: '<i class="material-icons bamdik">chevron_left</i>',
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 576,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
            }
        }
    ]
});


// PRODUCT SINGLE SLIDER
$('.product-single-slider').slick({
    dots: false,
    infinite: true,
    autoplay: false,
    arrows: true,
    fade: false,
    speed: 1000,
    centerMode: true,
    centerPadding: '250px',
    slidesToShow: 1,
    slidesToScroll: 1,
    prevArrow: '<i class="material-icons dandik">chevron_right</i>',
    nextArrow: '<i class="material-icons bamdik">chevron_left</i>',
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                centerPadding: '200px',
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                centerPadding: '130px',
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                centerPadding: '40px',
            }
        },
        {
            breakpoint: 576,
            settings: {
                arrows: false,
                slidesToShow: 1,
                slidesToScroll: 1,
                centerPadding: '0px',
                dots: true,
            }
        }
    ]
});


// FOR PRODUCT RELATED SLIDER   
$('.related-slider').slick({
    dots: false,
    infinite: true,
    autoplay: false,
    arrows: true,
    fade: false,
    speed: 1000,
    prevArrow: '<i class="material-icons dandik">chevron_right</i>',
    nextArrow: '<i class="material-icons bamdik">chevron_left</i>',
    slidesToShow: 4,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 576,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
            }
        }
    ]
});


// FOR PRICING PLAN SLIDER
$('.price-slider').slick({
    dots: false,
    infinite: true,
    autoplay: false,
    arrows: true,
    fade: false,
    speed: 1000,
    prevArrow: '<i class="material-icons dandik">chevron_right</i>',
    nextArrow: '<i class="material-icons bamdik">chevron_left</i>',
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 576,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        }
    ]
});